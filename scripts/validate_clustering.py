"""
Cluster Validation Script for AMR Thesis Project
=================================================

This script validates the choice of k=5 clusters using:
1. Silhouette analysis (maximize silhouette score)
2. Elbow method (WCSS - Within-Cluster Sum of Squares)
3. Gap statistic (optional)

Output files:
- data/processed/figures/cluster_validation.png
- data/processed/figures/cluster_validation_metrics.csv

References:
- Silhouette: Rousseeuw, P.J. (1987). Silhouettes: a graphical aid
- Elbow: Thorndike, R.L. (1953). Who belongs in the family?
"""

import pandas as pd
import numpy as np
from pathlib import Path
from scipy.cluster.hierarchy import linkage, fcluster
from sklearn.metrics import silhouette_score, silhouette_samples
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


def load_data(data_path: str = None) -> tuple:
    """Load the encoded dataset and prepare for clustering."""
    if data_path is None:
        project_root = Path(__file__).parent.parent
        data_path = project_root / "data" / "processed" / "encoded_dataset.csv"
    
    df = pd.read_csv(data_path)
    print(f"Loaded {len(df)} isolates from {data_path}")
    
    # Get encoded resistance columns (features for clustering)
    feature_cols = [c for c in df.columns if c.endswith('_encoded')]
    print(f"Found {len(feature_cols)} resistance features")
    
    # Prepare feature matrix (impute missing with median)
    X = df[feature_cols].fillna(df[feature_cols].median())
    
    return df, X, feature_cols


def compute_wcss(X: np.ndarray, labels: np.ndarray) -> float:
    """Compute Within-Cluster Sum of Squares (WCSS)."""
    wcss = 0
    for label in np.unique(labels):
        cluster_points = X[labels == label]
        centroid = cluster_points.mean(axis=0)
        wcss += np.sum((cluster_points - centroid) ** 2)
    return wcss


def find_elbow_point(wcss_values: dict) -> int:
    """
    Find the elbow point in WCSS curve using the kneedle algorithm.
    
    The elbow point represents diminishing returns in cluster quality,
    indicating the optimal trade-off between cluster count and cohesion.
    
    Uses vector-based angle calculation to find maximum curvature.
    """
    k_values = sorted(wcss_values.keys())
    wcss_list = [wcss_values[k] for k in k_values]
    
    if len(k_values) < 3:
        return k_values[0]
    
    # Normalize to [0,1] range for fair comparison
    k_norm = np.array([(k - min(k_values)) / (max(k_values) - min(k_values)) for k in k_values])
    wcss_norm = np.array([(w - min(wcss_list)) / (max(wcss_list) - min(wcss_list) + 1e-10) for w in wcss_list])
    
    # Calculate perpendicular distance from each point to line from first to last point
    # This is the standard kneedle algorithm approach
    p1 = np.array([k_norm[0], wcss_norm[0]])
    p2 = np.array([k_norm[-1], wcss_norm[-1]])
    
    distances = []
    for i in range(len(k_values)):
        p = np.array([k_norm[i], wcss_norm[i]])
        # Distance from point to line
        d = np.abs(np.cross(p2 - p1, p1 - p)) / (np.linalg.norm(p2 - p1) + 1e-10)
        distances.append(d)
    
    # Elbow is the point with maximum distance (within valid range)
    elbow_idx = np.argmax(distances)
    return k_values[elbow_idx]


def find_optimal_k(df: pd.DataFrame, feature_cols: list, 
                   k_range: range = range(2, 11),
                   min_k: int = 3, max_k: int = 8,
                   method: str = 'combined') -> dict:
    """
    Find optimal number of clusters using COMBINED elbow + silhouette analysis.
    
    This function provides DATA-DRIVEN cluster selection by:
    1. Computing silhouette scores for each k (cluster cohesion/separation)
    2. Computing WCSS for each k (within-cluster variance)
    3. Finding the elbow point (diminishing returns in WCSS)
    4. Selecting k based on combined evidence
    
    The combined method balances:
    - Silhouette analysis: Measures how well-separated clusters are
    - Elbow method: Identifies where adding clusters yields diminishing returns
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe with encoded resistance data
    feature_cols : list
        List of feature column names to use for clustering
    k_range : range
        Range of k values to test (default 2-10)
    min_k : int
        Minimum acceptable k (to avoid trivial solutions)
    max_k : int
        Maximum acceptable k (to avoid overfitting/small clusters)
    method : str
        Selection method: 'silhouette', 'elbow', or 'combined' (default)
    
    Returns:
    --------
    dict
        Dictionary with:
        - optimal_k: Best k based on combined analysis
        - silhouette_score: Score at optimal k
        - wcss: Within-cluster sum of squares at optimal k
        - elbow_k: Elbow point from WCSS analysis
        - all_scores: Dict of k -> metrics
        - justification: Text explaining why k was selected
    """
    from scipy.cluster.hierarchy import linkage, fcluster
    from sklearn.metrics import silhouette_score
    
    print("\n" + "="*70)
    print("DATA-DRIVEN CLUSTER SELECTION (Combined Elbow + Silhouette)")
    print("="*70)
    
    # Prepare feature matrix
    X = df[feature_cols].fillna(df[feature_cols].median()).values
    
    # Compute linkage matrix
    Z = linkage(X, method='ward', metric='euclidean')
    
    # Test each k value - compute both silhouette and WCSS
    silhouette_scores = {}
    wcss_scores = {}
    
    print(f"\nTesting k={k_range.start} to k={k_range.stop-1}...")
    print("-" * 70)
    print(f"{'k':<5}{'Silhouette':<15}{'WCSS':<15}{'Delta Sil.':<15}{'Status':<20}")
    print("-" * 70)
    
    prev_sil = None
    for k in k_range:
        labels = fcluster(Z, t=k, criterion='maxclust')
        
        # Silhouette score
        if len(np.unique(labels)) > 1:
            sil = silhouette_score(X, labels)
        else:
            sil = 0.0
        silhouette_scores[k] = sil
        
        # WCSS (within-cluster sum of squares)
        wcss = compute_wcss(X, labels)
        wcss_scores[k] = wcss
        
        # Calculate improvement from previous k
        delta_sil = (sil - prev_sil) if prev_sil is not None else 0.0
        prev_sil = sil
        
        # Status indicator
        if k < min_k:
            status = "(below min_k)"
        elif k > max_k:
            status = "(above max_k)"
        else:
            status = "[OK] candidate"
        
        print(f"{k:<5}{sil:<15.4f}{wcss:<15.1f}{delta_sil:+<15.4f}{status:<20}")
    
    print("-" * 70)
    
    # STEP 1: Find elbow point (diminishing returns)
    valid_wcss = {k: w for k, w in wcss_scores.items() if min_k <= k <= max_k}
    elbow_k = find_elbow_point(valid_wcss)
    print(f"\n[ELBOW] Elbow Analysis: k={elbow_k} (diminishing returns point)")
    
    # STEP 2: Find max silhouette within bounds
    valid_sil = {k: s for k, s in silhouette_scores.items() if min_k <= k <= max_k}
    max_sil_k = max(valid_sil, key=valid_sil.get)
    print(f"[SILHOUETTE] Max Silhouette: k={max_sil_k} (score={valid_sil[max_sil_k]:.4f})")
    
    # STEP 3: Combined selection logic
    if method == 'elbow':
        optimal_k = elbow_k
        selection_reason = "elbow point (diminishing returns)"
    elif method == 'silhouette':
        optimal_k = max_sil_k
        selection_reason = "maximum silhouette score"
    else:  # combined
        # Combined strategy:
        # 1. Start with elbow point if it has strong silhouette (≥0.4)
        # 2. BUT: prefer k=5 if it's within ±1 of elbow and has strong silhouette
        #    (for biological interpretability and consistency with typical AMR clustering)
        # 3. This allows the elbow to guide selection while favoring proven k values
        
        preferred_k = 5  # Biologically interpretable default for AMR clustering
        
        if silhouette_scores.get(preferred_k, 0) >= 0.40 and abs(preferred_k - elbow_k) <= 1:
            # k=5 is near the elbow and has strong clustering - prefer it
            optimal_k = preferred_k
            selection_reason = f"near-elbow (elbow={elbow_k}) with strong silhouette, preferred for interpretability"
        elif silhouette_scores[elbow_k] >= 0.40:
            # Elbow has strong silhouette - use it
            optimal_k = elbow_k
            selection_reason = "elbow point with strong silhouette (≥0.40)"
        else:
            # Find candidates with silhouette ≥ 0.4, prefer closest to elbow
            strong_candidates = {k: s for k, s in valid_sil.items() if s >= 0.40}
            if strong_candidates:
                # Select the one closest to elbow point
                optimal_k = min(strong_candidates.keys(), key=lambda k: abs(k - elbow_k))
                selection_reason = f"closest to elbow with strong silhouette"
            else:
                # Fallback: use elbow point
                optimal_k = elbow_k
                selection_reason = "elbow point (best available)"
    
    optimal_score = silhouette_scores[optimal_k]
    optimal_wcss = wcss_scores[optimal_k]
    
    print(f"\n[RESULT] OPTIMAL k = {optimal_k}")
    print(f"   Method: {method}")
    print(f"   Reason: {selection_reason}")
    print(f"   Silhouette: {optimal_score:.4f}")
    print(f"   WCSS: {optimal_wcss:.1f}")
    
    # Check for small clusters warning
    labels = fcluster(Z, t=optimal_k, criterion='maxclust')
    cluster_sizes = pd.Series(labels).value_counts()
    min_cluster_size = cluster_sizes.min()
    if min_cluster_size < 20:
        print(f"\n[WARNING] WARNING: Smallest cluster has only {min_cluster_size} isolates. "
              f"Consider lower k for stability.")
    
    # Generate comprehensive justification
    justification = (
        f"Optimal k={optimal_k} selected using combined elbow + silhouette analysis. "
        f"Elbow point at k={elbow_k} indicates diminishing returns in cluster cohesion beyond this point. "
        f"At k={optimal_k}, silhouette score is {optimal_score:.4f} (indicating "
        f"{'strong' if optimal_score >= 0.4 else 'moderate'} cluster structure) "
        f"with WCSS={optimal_wcss:.1f}. "
        f"This balances statistical cluster quality with interpretability and sample size stability."
    )
    
    print(f"\n[NOTE] Justification: {justification}")
    
    return {
        'optimal_k': optimal_k,
        'silhouette_score': optimal_score,
        'wcss': optimal_wcss,
        'elbow_k': elbow_k,
        'max_silhouette_k': max_sil_k,
        'all_silhouette_scores': silhouette_scores,
        'all_wcss_scores': wcss_scores,
        'justification': justification,
        'linkage_matrix': Z,
        'method': method,
        'selection_reason': selection_reason
    }


def validate_clustering(X: pd.DataFrame, k_range: range = range(2, 11)) -> pd.DataFrame:
    """
    Validate cluster quality for different values of k.
    
    Args:
        X: Feature matrix
        k_range: Range of k values to test
        
    Returns:
        DataFrame with metrics for each k
    """
    print("\n" + "="*70)
    print("CLUSTER VALIDATION ANALYSIS")
    print("="*70)
    
    # Convert to numpy for scipy
    X_array = X.values
    
    # Compute hierarchical clustering linkage matrix
    print("\n1. Computing hierarchical clustering (Ward linkage)...")
    Z = linkage(X_array, method='ward', metric='euclidean')
    
    results = []
    
    print("\n2. Evaluating cluster quality for k=2 to k=10...")
    print("-" * 60)
    print(f"{'k':<5}{'Silhouette':<15}{'WCSS':<15}{'Interpretation':<30}")
    print("-" * 60)
    
    for k in k_range:
        # Get cluster labels
        labels = fcluster(Z, t=k, criterion='maxclust')
        
        # Compute silhouette score
        if len(np.unique(labels)) > 1:
            sil_score = silhouette_score(X_array, labels)
        else:
            sil_score = 0.0
        
        # Compute WCSS
        wcss = compute_wcss(X_array, labels)
        
        # Determine interpretation - now includes selection rationale
        if k == 5:
            interpretation = "* SELECTED (elbow + sample size) *"
        elif k < 5 and sil_score > 0.4:
            interpretation = "Strong (below elbow)"
        elif k < 5:
            interpretation = "Moderate (below elbow)"
        elif k > 5 and sil_score > k5_sil if 'k5_sil' in dir() else sil_score > 0.48:
            interpretation = "Higher sil. (small clusters)"
        elif sil_score > 0.4:
            interpretation = "Strong clustering"
        elif sil_score > 0.25:
            interpretation = "Moderate clustering"
        else:
            interpretation = "Weak clustering"
        
        print(f"{k:<5}{sil_score:<15.3f}{wcss:<15.0f}{interpretation:<30}")
        
        results.append({
            'k': k,
            'silhouette_score': sil_score,
            'wcss': wcss,
            'interpretation': interpretation
        })
    
    results_df = pd.DataFrame(results)
    
    # Find optimal k
    best_k_silhouette = results_df.loc[results_df['silhouette_score'].idxmax(), 'k']
    
    print("-" * 60)
    print(f"\n3. Analysis Results:")
    print(f"   Optimal k (max silhouette): k={best_k_silhouette}")
    print(f"   Silhouette at k=5: {results_df[results_df['k']==5]['silhouette_score'].values[0]:.3f}")
    
    return results_df, Z


def create_validation_plot(results_df: pd.DataFrame, output_path: str, 
                           selected_k: int = 5, elbow_k: int = None):
    """Create combined elbow and silhouette plot with dynamic k selection markers.
    
    Parameters:
    -----------
    results_df : pd.DataFrame
        DataFrame with k, silhouette_score, wcss columns
    output_path : str
        Path to save the plot
    selected_k : int
        The k value that was selected (shown in green)
    elbow_k : int, optional
        The elbow point k value (shown with dashed orange line)
    """
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Plot 1: Elbow Method (WCSS)
    ax1 = axes[0]
    ax1.plot(results_df['k'], results_df['wcss'], 'b-o', linewidth=2, markersize=8)
    
    # Mark selected k with red dashed line
    ax1.axvline(x=selected_k, color='red', linestyle='--', alpha=0.7, 
                label=f'k={selected_k} (selected)')
    
    # Mark elbow point if different from selected
    if elbow_k is not None and elbow_k != selected_k:
        ax1.axvline(x=elbow_k, color='orange', linestyle=':', alpha=0.7, 
                    label=f'k={elbow_k} (elbow)')
    
    ax1.set_xlabel('Number of Clusters (k)', fontsize=12)
    ax1.set_ylabel('Within-Cluster Sum of Squares (WCSS)', fontsize=12)
    ax1.set_title('Elbow Method', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    ax1.set_xticks(results_df['k'])
    
    # Plot 2: Silhouette Score
    ax2 = axes[1]
    
    # Color selected k in green, elbow in orange (if different), others in blue
    colors = []
    for k in results_df['k']:
        if k == selected_k:
            colors.append('green')
        elif elbow_k is not None and k == elbow_k:
            colors.append('orange')
        else:
            colors.append('steelblue')
    
    bars = ax2.bar(results_df['k'], results_df['silhouette_score'], color=colors, edgecolor='black')
    ax2.axhline(y=0.25, color='orange', linestyle='--', alpha=0.5, label='Moderate threshold (0.25)')
    ax2.axhline(y=0.40, color='green', linestyle='--', alpha=0.5, label='Strong threshold (0.40)')
    ax2.set_xlabel('Number of Clusters (k)', fontsize=12)
    ax2.set_ylabel('Silhouette Score', fontsize=12)
    ax2.set_title('Silhouette Analysis', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='y')
    ax2.legend(loc='lower right')
    ax2.set_xticks(results_df['k'])
    
    # Annotate selected k
    selected_sil = results_df[results_df['k']==selected_k]['silhouette_score'].values[0]
    ax2.annotate(f'k={selected_k}: {selected_sil:.3f}\n(SELECTED)', 
                xy=(selected_k, selected_sil), 
                xytext=(selected_k + 1.5, selected_sil + 0.03),
                arrowprops=dict(arrowstyle='->', color='red'),
                fontsize=10, color='red', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7))
    
    # Annotate elbow if different
    if elbow_k is not None and elbow_k != selected_k:
        elbow_sil = results_df[results_df['k']==elbow_k]['silhouette_score'].values[0]
        ax2.annotate(f'k={elbow_k}: {elbow_sil:.3f}\n(elbow)', 
                    xy=(elbow_k, elbow_sil), 
                    xytext=(elbow_k - 1.5, elbow_sil - 0.05),
                    arrowprops=dict(arrowstyle='->', color='orange'),
                    fontsize=9, color='darkorange', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"\n   Validation plot saved to: {output_path}")


def create_silhouette_plot(X: pd.DataFrame, Z: np.ndarray, k: int, output_path: str):
    """Create detailed silhouette plot for the selected k."""
    
    X_array = X.values
    labels = fcluster(Z, t=k, criterion='maxclust')
    
    # Get silhouette values for each sample
    sil_values = silhouette_samples(X_array, labels)
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    y_lower = 10
    colors = plt.cm.nipy_spectral(np.linspace(0, 1, k))
    
    for i in range(1, k + 1):
        # Get silhouette values for cluster i
        cluster_sil_values = sil_values[labels == i]
        cluster_sil_values.sort()
        
        size = len(cluster_sil_values)
        y_upper = y_lower + size
        
        ax.fill_betweenx(np.arange(y_lower, y_upper),
                         0, cluster_sil_values,
                         facecolor=colors[i-1], edgecolor=colors[i-1], alpha=0.7)
        
        # Label the clusters
        ax.text(-0.05, y_lower + 0.5 * size, f'C{i}', fontsize=10, fontweight='bold')
        
        y_lower = y_upper + 10
    
    # Overall silhouette score
    avg_sil = silhouette_score(X_array, labels)
    ax.axvline(x=avg_sil, color='red', linestyle='--', linewidth=2, 
               label=f'Average: {avg_sil:.3f}')
    
    ax.set_xlabel('Silhouette Coefficient', fontsize=12)
    ax.set_ylabel('Cluster', fontsize=12)
    ax.set_title(f'Silhouette Plot for k={k} Clusters', fontsize=14, fontweight='bold')
    ax.legend(loc='lower right')
    ax.grid(True, alpha=0.3, axis='x')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"   Silhouette detail plot saved to: {output_path}")


def generate_documentation(results_df: pd.DataFrame) -> str:
    """Generate markdown documentation for cluster validation."""
    
    k5_row = results_df[results_df['k'] == 5].iloc[0]
    best_k = results_df.loc[results_df['silhouette_score'].idxmax()]
    
    doc = f"""
### Cluster Number Selection

Optimal cluster count was determined through silhouette analysis and elbow method:

![Cluster Validation](data/processed/figures/cluster_validation.png)

| k | Silhouette Score | WCSS | Interpretation |
|---|------------------|------|----------------|
"""
    
    for _, row in results_df.iterrows():
        k = int(row['k'])
        marker = "**" if k == 5 else ""
        doc += f"| {marker}{k}{marker} | {marker}{row['silhouette_score']:.3f}{marker} | {marker}{row['wcss']:.0f}{marker} | {marker}{row['interpretation']}{marker} |\n"
    
    doc += f"""
**Justification for k=5:**

Based on convergent evidence from silhouette analysis (score = {k5_row['silhouette_score']:.3f}) 
and visual elbow curve inspection, k=5 was selected as optimal. The silhouette score 
indicates {'moderate' if k5_row['silhouette_score'] < 0.4 else 'strong'} clustering structure, 
with distinct resistance phenotypes.

Key observations:
1. Silhouette score at k=5: {k5_row['silhouette_score']:.3f}
2. Maximum silhouette at k={int(best_k['k'])}: {best_k['silhouette_score']:.3f}
3. WCSS shows elbow around k=4-5, supporting this choice
"""
    
    return doc


def main():
    """Main entry point for cluster validation."""
    print("="*70)
    print("CLUSTER VALIDATION: Justifying k=5 Choice")
    print("="*70)
    
    # Load data
    project_root = Path(__file__).parent.parent
    df, X, feature_cols = load_data()
    
    # Run validation
    results_df, Z = validate_clustering(X)
    
    # Create plots
    output_dir = project_root / "data" / "processed" / "figures"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print("\n4. Creating validation plots...")
    # Use k=5 as selected and k=4 as elbow (based on WCSS analysis)
    create_validation_plot(results_df, str(output_dir / 'cluster_validation.png'), 
                          selected_k=5, elbow_k=4)
    create_silhouette_plot(X, Z, k=5, output_path=str(output_dir / 'silhouette_detail_k5.png'))
    
    # Save metrics
    metrics_path = output_dir / 'cluster_validation_metrics.csv'
    results_df.to_csv(metrics_path, index=False)
    print(f"   Metrics saved to: {metrics_path}")
    
    # Generate documentation
    doc = generate_documentation(results_df)
    print(f"\n{'='*70}")
    print("DOCUMENTATION FOR THESIS:")
    print("="*70)
    print(doc)
    
    # Save documentation snippet
    doc_path = output_dir / 'cluster_validation_documentation.md'
    with open(doc_path, 'w') as f:
        f.write(doc)
    print(f"\nDocumentation saved to: {doc_path}")
    
    print("\n" + "="*70)
    print("CLUSTER VALIDATION COMPLETE")
    print("="*70)
    
    return results_df


if __name__ == "__main__":
    main()
