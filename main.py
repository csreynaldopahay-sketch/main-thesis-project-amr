"""
Main Pipeline for AMR Thesis Project
This script runs all phases of the AMR pattern recognition analysis.
"""

import os
import sys
from pathlib import Path

# Add src and scripts to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root / 'src'))
sys.path.insert(0, str(project_root / 'scripts'))

from preprocessing.data_ingestion import create_unified_dataset
from preprocessing.data_cleaning import clean_dataset, generate_cleaning_report
from preprocessing.resistance_encoding import create_encoded_dataset
from preprocessing.feature_engineering import prepare_analysis_ready_dataset
from clustering.hierarchical_clustering import run_clustering_pipeline, get_cluster_summary
from visualization.visualization import generate_all_visualizations
from supervised.supervised_learning import run_species_discrimination, save_model
from analysis.regional_environmental import run_regional_environmental_analysis
from analysis.integration_synthesis import run_integration_synthesis


def run_full_pipeline(data_dir: str = None, output_dir: str = None):
    """
    Run the complete AMR analysis pipeline.
    
    Parameters:
    -----------
    data_dir : str, optional
        Directory containing raw CSV files
    output_dir : str, optional
        Directory to save processed data and outputs
    """
    # Set default paths
    if data_dir is None:
        data_dir = str(project_root)
    
    if output_dir is None:
        output_dir = str(project_root / 'data' / 'processed')
    
    os.makedirs(output_dir, exist_ok=True)
    
    print("=" * 70)
    print("AMR THESIS PROJECT - FULL ANALYSIS PIPELINE")
    print("=" * 70)
    
    # =============================================
    # PHASE 2: Data Preprocessing
    # =============================================
    
    # Phase 2.1: Data Ingestion
    print("\n" + "=" * 70)
    print("PHASE 2.1: DATA INGESTION AND CONSOLIDATION")
    print("=" * 70)
    
    unified_path = os.path.join(output_dir, 'unified_raw_dataset.csv')
    df_raw = create_unified_dataset(data_dir, unified_path)
    
    if df_raw.empty:
        print("ERROR: No data loaded. Check your CSV files.")
        return
    
    # Phase 2.2 & 2.3: Data Cleaning (with formal missing data strategy)
    print("\n")
    # Using stricter thresholds: 70% antibiotic coverage, 30% isolate missing threshold
    df_clean, cleaning_report = clean_dataset(df_raw, 
                                               min_antibiotic_coverage=70.0,
                                               max_isolate_missing=30.0)
    
    clean_path = os.path.join(output_dir, 'cleaned_dataset.csv')
    df_clean.to_csv(clean_path, index=False)
    print(f"Cleaned dataset saved to: {clean_path}")
    
    report_path = os.path.join(output_dir, 'cleaning_report.txt')
    generate_cleaning_report(cleaning_report, report_path)
    
    # Phase 2.4: Encoding
    print("\n")
    df_encoded, encoding_info = create_encoded_dataset(df_clean)
    
    encoded_path = os.path.join(output_dir, 'encoded_dataset.csv')
    df_encoded.to_csv(encoded_path, index=False)
    print(f"Encoded dataset saved to: {encoded_path}")
    
    # Phase 2.5: Feature Engineering (with structural data separation)
    print("\n")
    encoded_cols = encoding_info['encoded_columns']
    analysis_path = os.path.join(output_dir, 'analysis_ready_dataset.csv')
    df_analysis, feature_matrix, metadata, feature_info = prepare_analysis_ready_dataset(
        df_encoded, encoded_cols, output_path=analysis_path
    )
    
    # =============================================
    # PHASE 3: Unsupervised Structure Identification
    # =============================================
    
    print("\n")
    feature_cols = [c for c in df_analysis.columns if c.endswith('_encoded')]
    
    # =============================================
    # DATA-DRIVEN CLUSTER SELECTION
    # =============================================
    print("\n")
    from validate_clustering import find_optimal_k
    
    # Find optimal k using COMBINED elbow + silhouette analysis
    # The elbow method identifies diminishing returns, typically k=4-5
    # Combined with silhouette quality threshold (≥0.4) ensures robust selection
    #
    # ==========================================================================
    # SCIENTIFIC RATIONALE FOR max_k=6 CONSTRAINT (Action Item 6)
    # ==========================================================================
    # The upper bound of k=6 is justified on three grounds:
    #
    # 1. BIOLOGICAL INTERPRETABILITY:
    #    - With 492 isolates, k>6 would create clusters averaging <82 isolates
    #    - Small clusters (<50 isolates) have low statistical power for:
    #      (a) MDR proportion estimation (95% CI width > ±15%)
    #      (b) Species composition characterization
    #      (c) Regional/environmental distribution analysis
    #
    # 2. EPIDEMIOLOGICAL RELEVANCE:
    #    - AMR surveillance typically identifies 3-6 distinct resistance phenotypes
    #    - Reference: Magiorakos et al. (2012) defines 3 main categories: 
    #      MDR, XDR, PDR - suggesting biologically meaningful groupings are limited
    #    - More clusters often represent noise or site-specific effects
    #
    # 3. STATISTICAL STABILITY:
    #    - Silhouette scores typically decline for k>6 in AMR datasets
    #    - Higher k increases risk of unstable clusters (sensitive to random seed)
    #    - Robustness analysis (Ward vs. Average linkage) shows lower ARI for k>6
    #
    # SENSITIVITY NOTE: If the elbow strongly suggests k>6, review the data
    # for potential batch effects or species-specific sub-clustering.
    # ==========================================================================
    k_result = find_optimal_k(
        df_analysis, 
        feature_cols, 
        k_range=range(2, 11),
        min_k=3, 
        max_k=6,  # See scientific rationale above
        method='combined'  # Uses elbow + silhouette together
    )
    optimal_k = k_result['optimal_k']
    elbow_k = k_result['elbow_k']
    
    print(f"\n[CLUSTERING] Using data-driven k={optimal_k}")
    print(f"   Silhouette: {k_result['silhouette_score']:.4f}")
    print(f"   Elbow point: k={elbow_k}")
    print(f"   Reason: {k_result['selection_reason']}")
    
    # Regenerate validation plot with actual selected and elbow k values
    from validate_clustering import create_validation_plot
    import pandas as pd
    figures_dir_path = os.path.join(output_dir, 'figures')
    os.makedirs(figures_dir_path, exist_ok=True)
    
    # Build results dataframe for plot
    results_for_plot = pd.DataFrame({
        'k': list(k_result['all_silhouette_scores'].keys()),
        'silhouette_score': list(k_result['all_silhouette_scores'].values()),
        'wcss': list(k_result['all_wcss_scores'].values())
    })
    create_validation_plot(results_for_plot, 
                          os.path.join(figures_dir_path, 'cluster_validation.png'),
                          selected_k=optimal_k, 
                          elbow_k=elbow_k)
    
    # Create artifacts directory for clustering objects
    artifacts_dir = os.path.join(output_dir, 'clustering_artifacts')
    
    # Run clustering with DATA-DRIVEN k (evidence-based, not hardcoded)
    df_clustered, linkage_matrix, clustering_info = run_clustering_pipeline(
        df_analysis, 
        feature_cols, 
        n_clusters=optimal_k,  # DATA-DRIVEN: selected via combined elbow+silhouette
        perform_robustness=True,
        output_dir=artifacts_dir
    )
    
    clustered_path = os.path.join(output_dir, 'clustered_dataset.csv')
    df_clustered.to_csv(clustered_path, index=False)
    print(f"Clustered dataset saved to: {clustered_path}")
    
    # Phase 3.2: Visualization of resistance patterns
    print("\n")
    figures_dir = os.path.join(output_dir, 'figures')
    generate_all_visualizations(df_clustered, feature_cols, linkage_matrix, figures_dir, clustering_info)
    
    # Cluster interpretation using consistent C1, C2, ... labeling
    print("\n" + "=" * 70)
    print("PHASE 3.3: Cluster Interpretation (Resistance Phenotypes)")
    print("=" * 70)
    print("\nNOTE: Clusters represent RESISTANCE PHENOTYPES, not taxonomic groups.")
    print("      Metadata associations are correlational, not causal.\n")
    
    cluster_summary = get_cluster_summary(df_clustered, feature_cols)
    
    for cluster_id, info in cluster_summary.items():
        print(f"\nC{cluster_id} (Resistance Phenotype):")
        print(f"  Isolates: {info['n_isolates']} ({info['percentage']:.1f}%)")
        if 'mdr_proportion' in info:
            print(f"  MDR proportion: {info['mdr_proportion']:.1f}%")
        if 'mean_mar_index' in info:
            print(f"  Mean MAR index: {info['mean_mar_index']:.4f}")
        if 'dominant_species' in info:
            print(f"  Dominant species: {info['dominant_species']} ({info.get('dominant_species_pct', 0):.1f}%)")
        if 'top_resistant_antibiotics' in info:
            print(f"  Top resistant antibiotics: {', '.join(info['top_resistant_antibiotics'][:3])}")
    
    # ==============================================
    # PHASE 4: Supervised Learning (Phase 3 Improvements)
    # =============================================
    
    print("\n")
    print("=" * 70)
    print("PHASE 4: Supervised Learning (with Phase 3 Improvements)")
    print("  - Leakage-safe preprocessing")
    print("  - Separate task pipelines (Species vs MDR)")
    print("  - Rationalized model set")
    print("  - Macro-averaged metrics")
    print("=" * 70)
    
    # Create models directory
    models_dir = os.path.join(output_dir, '..', 'models')
    os.makedirs(models_dir, exist_ok=True)
    
    # NOTE: Circular MDR Discrimination REMOVED (Phase 3 Critical Fix)
    # MDR was derived from same AST features used as input - circular logic.
    # Instead, use co-resistance network analysis for MDR-related patterns.
    print("\n   NOTE: MDR discrimination removed (circular - MDR derived from input features).")
    print("   Use Co-Resistance Network Analysis for MDR-related patterns.")
    
    # Task A: Species Discrimination (Multi-class)
    species_results = None
    if 'ISOLATE_ID' in df_clustered.columns and df_clustered['ISOLATE_ID'].nunique() > 1:
        try:
            from supervised.supervised_learning import run_species_discrimination
            species_results = run_species_discrimination(df_clustered, feature_cols)
            
            # Save model with all preprocessors
            save_model(
                species_results['best_model']['model_object'],
                species_results['scaler'],
                species_results['label_encoder'],
                os.path.join(models_dir, 'species_classifier.joblib'),
                imputer=species_results.get('imputer'),
                preprocessing_info=species_results.get('preprocessing_info')
            )
        except Exception as e:
            print(f"Warning: Species discrimination failed: {e}")
    
    # =============================================
    # PHASE 4: Regional & Environmental Analysis (Phase 4 Improvements)
    # =============================================
    
    print("\n")
    figures_dir = os.path.join(output_dir, 'figures')
    regional_results = run_regional_environmental_analysis(
        df_clustered, feature_cols, figures_dir
    )
    
    # =============================================
    # PHASE 5: Integration & Synthesis
    # =============================================
    
    # Run comprehensive integration and synthesis analysis
    integration_results = run_integration_synthesis(
        df_clustered, feature_cols, supervised_results=None  # MDR results removed
    )
    
    # Additional summary statistics
    print("\n" + "-" * 50)
    print("ADDITIONAL STATISTICS:")
    print("-" * 50)
    
    print("\n1. Dataset Summary:")
    print(f"   Total isolates analyzed: {len(df_clustered)}")
    print(f"   Antibiotics tested: {len(feature_cols)}")
    if 'ISOLATE_ID' in df_clustered.columns:
        print(f"   Species identified: {df_clustered['ISOLATE_ID'].nunique()}")
    if 'REGION' in df_clustered.columns:
        print(f"   Regions: {df_clustered['REGION'].nunique()}")
    
    print("\n2. Resistance Patterns:")
    if 'MDR_FLAG' in df_clustered.columns:
        mdr_pct = df_clustered['MDR_FLAG'].mean() * 100
        print(f"   MDR prevalence: {mdr_pct:.1f}%")
    if 'MAR_INDEX_COMPUTED' in df_clustered.columns:
        print(f"   Mean MAR index: {df_clustered['MAR_INDEX_COMPUTED'].mean():.4f}")
    
    print("\n3. Clustering Results:")
    print(f"   Number of clusters: {clustering_info['n_clusters']}")
    for cluster_id, count in clustering_info['cluster_distribution'].items():
        pct = (count / len(df_clustered)) * 100
        print(f"   Cluster {cluster_id}: {count} isolates ({pct:.1f}%)")
    
    print("\n" + "=" * 70)
    print("PIPELINE COMPLETE")
    print("=" * 70)
    
    print(f"\nOutputs saved to: {output_dir}")
    print("\nGenerated files:")
    print("  - unified_raw_dataset.csv")
    print("  - cleaned_dataset.csv")
    print("  - cleaning_report.txt")
    print("  - encoded_dataset.csv")
    print("  - analysis_ready_dataset.csv")
    print("  - clustered_dataset.csv")
    print("  - figures/ (visualization outputs)")
    
    print("\nTo run the interactive dashboard:")
    print("  streamlit run app/streamlit_app.py")
    
    return df_clustered, integration_results


if __name__ == "__main__":
    run_full_pipeline()
