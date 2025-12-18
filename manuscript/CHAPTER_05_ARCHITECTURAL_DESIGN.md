# CHAPTER 5: ARCHITECTURAL DESIGN

## Pattern Recognition of Antibiotic Resistance in *Escherichia coli*, *Salmonella* spp., *Shigella* spp., and *Vibrio cholerae* from the Water–Fish–Human Nexus

---

## 5.1 System Overview

### 5.1.1 Purpose

The AMR Pattern Recognition Pipeline implements a comprehensive analytical system for antimicrobial resistance surveillance and pattern recognition. The system processes antimicrobial susceptibility testing (AST) data from bacterial isolates collected across multiple Philippine regions, enabling researchers to:

- Identify natural groupings (clusters) in resistance profiles
- Evaluate pattern discrimination capabilities using supervised learning
- Analyze regional and environmental factors associated with resistance patterns
- Visualize and interact with analysis results through an interactive dashboard

### 5.1.2 Architectural Goals

| Goal | Description |
|------|-------------|
| **Modularity** | Independent, loosely-coupled components that can be developed and tested separately |
| **Extensibility** | Easy addition of new analysis methods, visualizations, and data sources |
| **Reproducibility** | Deterministic results with configurable random states and versioned outputs |
| **Usability** | Clear APIs and interactive interfaces for researchers |
| **Maintainability** | Clean code structure with comprehensive documentation |

---

## 5.2 High-Level Architecture

### 5.2.1 Architectural Style

The system follows a **Layered Architecture** combined with a **Pipeline Pattern**:

- **Layered Architecture:** Separates concerns into distinct layers (data, processing, presentation)
- **Pipeline Pattern:** Sequential processing phases with well-defined inputs and outputs

### 5.2.2 System Layers Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         PRESENTATION LAYER                                   │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  Streamlit Dashboard (app/streamlit_app.py)                         │    │
│  │  • Interactive data exploration                                      │    │
│  │  • Visualization rendering                                           │    │
│  │  • Analysis result display                                           │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
├─────────────────────────────────────────────────────────────────────────────┤
│                          ANALYSIS LAYER                                      │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────────────────┐    │
│  │  Clustering    │  │  Supervised    │  │  Integration & Synthesis   │    │
│  │  (Phase 3)     │  │  Learning      │  │  (Phase 6)                 │    │
│  │                │  │  (Phase 4)     │  │                            │    │
│  └────────────────┘  └────────────────┘  └────────────────────────────┘    │
│  ┌────────────────┐  ┌────────────────┐                                    │
│  │  Regional      │  │  Visualization │                                    │
│  │  Analysis      │  │  (Phase 3.2)   │                                    │
│  │  (Phase 5)     │  │                │                                    │
│  └────────────────┘  └────────────────┘                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                        PREPROCESSING LAYER                                   │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐  ┌──────────┐  │
│  │  Data          │  │  Data          │  │  Resistance    │  │  Feature │  │
│  │  Ingestion     │  │  Cleaning      │  │  Encoding      │  │  Eng.    │  │
│  │  (Phase 2.1)   │  │  (Phase 2.2-3) │  │  (Phase 2.4)   │  │  (2.5)   │  │
│  └────────────────┘  └────────────────┘  └────────────────┘  └──────────┘  │
├─────────────────────────────────────────────────────────────────────────────┤
│                           DATA LAYER                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  Raw CSV Files → Processed Datasets → Analysis Results → Models     │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 5.3 Data Flow Architecture

### 5.3.1 End-to-End Data Flow

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                              DATA FLOW DIAGRAM                                   │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│   Raw CSV Files (*.csv)                                                         │
│       │                                                                         │
│       ▼                                                                         │
│   ┌────────────────────────────────────────────────────────────────────┐       │
│   │                    DATA INGESTION (Phase 2.1)                       │       │
│   │  • Load multiple CSV files from directory                           │       │
│   │  • Parse isolate codes for metadata extraction                      │       │
│   │  • Extract region/site from filenames                               │       │
│   │  • Standardize antibiotic abbreviations                             │       │
│   └────────────────────────────────────────────────────────────────────┘       │
│       │                                                                         │
│       ▼                                                                         │
│   unified_raw_dataset.csv                                                       │
│       │                                                                         │
│       ▼                                                                         │
│   ┌────────────────────────────────────────────────────────────────────┐       │
│   │                    DATA CLEANING (Phase 2.2-2.3)                    │       │
│   │  • Standardize species names                                        │       │
│   │  • Standardize resistance values (S, I, R)                          │       │
│   │  • Remove duplicate isolates                                        │       │
│   │  • Filter antibiotics by coverage threshold (≥70%)                  │       │
│   │  • Remove isolates with excessive missing data (>30%)               │       │
│   └────────────────────────────────────────────────────────────────────┘       │
│       │                                                                         │
│       ▼                                                                         │
│   cleaned_dataset.csv + cleaning_report.txt                                     │
│       │                                                                         │
│       ▼                                                                         │
│   ┌────────────────────────────────────────────────────────────────────┐       │
│   │                  RESISTANCE ENCODING (Phase 2.4)                    │       │
│   │  • Encode resistance values: S=0, I=1, R=2                          │       │
│   │  • Generate resistance fingerprints                                 │       │
│   │  • Create encoded columns (*_encoded)                               │       │
│   └────────────────────────────────────────────────────────────────────┘       │
│       │                                                                         │
│       ▼                                                                         │
│   encoded_dataset.csv                                                           │
│       │                                                                         │
│       ▼                                                                         │
│   ┌────────────────────────────────────────────────────────────────────┐       │
│   │                  FEATURE ENGINEERING (Phase 2.5)                    │       │
│   │  • Compute MAR Index (resistant/tested)                             │       │
│   │  • Compute resistance count                                         │       │
│   │  • Count resistant antibiotic classes                               │       │
│   │  • Determine MDR status (≥3 classes)                                │       │
│   │  • Create binary resistance indicators                              │       │
│   └────────────────────────────────────────────────────────────────────┘       │
│       │                                                                         │
│       ▼                                                                         │
│   analysis_ready_dataset.csv ───────────────────────────────────────────────   │
│       │                                                                    │    │
│       ├──────────────────────┬──────────────────────┬───────────────────┐ │    │
│       ▼                      ▼                      ▼                   ▼ │    │
│   ┌──────────┐          ┌──────────┐          ┌──────────┐       ┌──────┴───┐ │
│   │ Phase 3  │          │ Phase 4  │          │ Phase 5  │       │ Phase 7  │ │
│   │Clustering│          │Supervised│          │Regional  │       │Dashboard │ │
│   └────┬─────┘          └────┬─────┘          └────┬─────┘       └──────────┘ │
│        │                     │                     │                          │
│        ▼                     ▼                     ▼                          │
│   clustered_      *.joblib models    figures/*.png                           │
│   dataset.csv                                                                 │
│        │                                                                       │
│        └────────────────────────┬────────────────────────────┘                │
│                                 ▼                                              │
│                    ┌────────────────────────┐                                  │
│                    │  INTEGRATION (Phase 6) │                                  │
│                    │  • Cluster-supervised  │                                  │
│                    │    comparison          │                                  │
│                    │  • Resistance archetypes│                                 │
│                    │  • Species-environment │                                  │
│                    │  • MDR-enriched patterns│                                 │
│                    └────────────────────────┘                                  │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### 5.3.2 Data Transformation Summary

| Phase | Input | Transformation | Output |
|-------|-------|----------------|--------|
| **2.1** | Raw CSV files | Parse, extract metadata, consolidate | `unified_raw_dataset.csv` |
| **2.2-2.3** | Unified raw dataset | Clean, standardize, filter | `cleaned_dataset.csv` |
| **2.4** | Cleaned dataset | Encode resistance values | `encoded_dataset.csv` |
| **2.5** | Encoded dataset | Compute derived features | `analysis_ready_dataset.csv` |
| **3.1** | Analysis-ready dataset | Hierarchical clustering | `clustered_dataset.csv` |
| **3.2** | Clustered dataset | Generate plots | PNG visualizations |
| **4** | Analysis-ready dataset | Train classifiers | `*.joblib` model files |
| **5** | Clustered dataset | PCA, cross-tabulation | Statistical results |
| **6** | All results | Synthesize findings | Summary reports |

---

## 5.4 Component Architecture

### 5.4.1 Source Code Organization

```
src/
├── __init__.py
├── config.py                           # Centralized configuration
├── preprocessing/
│   ├── __init__.py
│   ├── data_ingestion.py              # Phase 2.1: CSV loading, metadata extraction
│   ├── data_cleaning.py               # Phase 2.2-2.3: Standardization, filtering
│   ├── resistance_encoding.py         # Phase 2.4: S/I/R encoding
│   └── feature_engineering.py         # Phase 2.5: MAR, MDR computation
├── clustering/
│   ├── __init__.py
│   └── hierarchical_clustering.py     # Phase 3.1: Ward's method clustering
├── visualization/
│   ├── __init__.py
│   └── visualization.py               # Phase 3.2: Heatmaps, dendrograms
├── supervised/
│   ├── __init__.py
│   └── supervised_learning.py         # Phase 4: Classification, evaluation
└── analysis/
    ├── __init__.py
    ├── regional_environmental.py      # Phase 5: PCA, distributions
    └── integration_synthesis.py       # Phase 6: Result integration
```

### 5.4.2 Component Specifications

#### Preprocessing Components

| Module | Purpose | Key Functions |
|--------|---------|---------------|
| `data_ingestion.py` | CSV loading, metadata extraction | `create_unified_dataset()`, `parse_isolate_code()` |
| `data_cleaning.py` | Data standardization, filtering | `clean_dataset()`, `filter_antibiotics_by_coverage()` |
| `resistance_encoding.py` | Resistance value encoding | `create_encoded_dataset()`, `encode_resistance_profile()` |
| `feature_engineering.py` | Derived feature computation | `prepare_analysis_ready_dataset()`, `compute_mar_index()` |

#### Analysis Components

| Module | Purpose | Key Functions |
|--------|---------|---------------|
| `hierarchical_clustering.py` | Unsupervised clustering | `run_clustering_pipeline()`, `perform_hierarchical_clustering()` |
| `visualization.py` | Plot generation | `create_resistance_heatmap()`, `create_dendrogram()` |
| `supervised_learning.py` | Pattern discrimination | `run_mdr_discrimination()`, `get_feature_importance()` |
| `regional_environmental.py` | Regional analysis | `run_regional_environmental_analysis()`, `perform_pca()` |
| `integration_synthesis.py` | Result synthesis | `run_integration_synthesis()`, `identify_resistance_archetypes()` |

---

## 5.5 Data Model and Schemas

### 5.5.1 Input Data Schema

Raw CSV files contain structured antimicrobial susceptibility testing data:

```
Row 3: CODE | ISOLATE ID | [metadata] | ... | SCORED RESISTANCE | NO. ANTIBIOTIC TESTED | MAR INDEX
Row 4: ESBL | AM | AMC | CPT | CN | ... (antibiotic names)
Row 5: MIC  | INT| INT | INT | INT| ... (value type indicators)
Row 6+: Data rows with isolate-level AST results
```

### 5.5.2 Processed Data Schema: analysis_ready_dataset.csv

| Column Type | Examples | Description |
|-------------|----------|-------------|
| **Identification** | CODE, ISOLATE_ID | Unique isolate identifiers |
| **Metadata** | REGION, SITE, ENVIRONMENT | Geographic and environmental context |
| **Raw AST** | AM, AMC, TE, ... | Original S/I/R values |
| **Encoded AST** | AM_encoded, AMC_encoded, ... | Numerical encoding (0/1/2) |
| **Derived Features** | MAR_INDEX_COMPUTED, MDR_FLAG, ... | Computed resistance metrics |
| **Binary Indicators** | AM_RESISTANT, TE_RESISTANT, ... | Binary resistance flags |

### 5.5.3 Key Schema Elements

| Column | Type | Description |
|--------|------|-------------|
| `CODE` | string | Unique isolate identifier |
| `ISOLATE_ID` | string | Species name |
| `REGION` | string | Geographic region (BARMM, Region III, Region VIII) |
| `ENVIRONMENT` | string | Sample category (Water, Fish, Hospital) |
| `{AB}_encoded` | integer | Encoded resistance (0=S, 1=I, 2=R) |
| `MAR_INDEX_COMPUTED` | float | Multiple Antibiotic Resistance index (0–1) |
| `MDR_FLAG` | boolean | Multi-drug resistant indicator |
| `MDR_CATEGORY` | string | "MDR" or "Non-MDR" |
| `CLUSTER` | integer | Cluster assignment (1–5) |

---

## 5.6 Technology Stack

### 5.6.1 Technology Stack Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           TECHNOLOGY STACK                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                      PRESENTATION LAYER                              │   │
│  │  Streamlit >= 1.24.0                                                │   │
│  │  • Web framework for interactive dashboards                         │   │
│  │  • Reactive UI components                                           │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                      VISUALIZATION LAYER                             │   │
│  │  Matplotlib >= 3.6.0  |  Seaborn >= 0.12.0                          │   │
│  │  • Heatmaps, dendrograms, scatter plots                             │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                     MACHINE LEARNING LAYER                           │   │
│  │  scikit-learn >= 1.1.0                                              │   │
│  │  • Classification (RF, LR, KNN) | PCA | Preprocessing               │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    SCIENTIFIC COMPUTING LAYER                        │   │
│  │  SciPy >= 1.9.0                                                     │   │
│  │  • Hierarchical clustering | Chi-square tests | Distance metrics    │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                        DATA LAYER                                    │   │
│  │  Pandas >= 1.5.0  |  NumPy >= 1.23.0                                │   │
│  │  • DataFrame operations | CSV I/O | Numerical computing             │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                       RUNTIME ENVIRONMENT                            │   │
│  │  Python >= 3.8  |  joblib (model persistence)                       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 5.6.2 Dependency Matrix

| Dependency | Version | Purpose | Components |
|------------|---------|---------|------------|
| pandas | >=1.5.0 | Data manipulation | All modules |
| numpy | >=1.23.0 | Numerical operations | All modules |
| scipy | >=1.9.0 | Clustering, statistics | clustering, analysis |
| scikit-learn | >=1.1.0 | ML algorithms | supervised, preprocessing |
| matplotlib | >=3.6.0 | Visualization | visualization, analysis |
| seaborn | >=0.12.0 | Statistical plots | visualization |
| streamlit | >=1.24.0 | Dashboard | app |
| joblib | >=1.2.0 | Model persistence | supervised |

---

## 5.7 Pipeline Execution

### 5.7.1 Execution Modes

| Mode | Command | Purpose |
|------|---------|---------|
| **Full Pipeline** | `python main.py` | Execute complete analysis |
| **Dashboard** | `streamlit run app/streamlit_app.py` | Interactive exploration |
| **Module Test** | `python -m src.preprocessing.data_ingestion` | Test individual module |

### 5.7.2 Pipeline Orchestration

The `main.py` script orchestrates the complete pipeline:

```python
def run_full_pipeline():
    # Phase 2: Data Preprocessing
    df_unified = create_unified_dataset(data_dir)
    df_cleaned, report = clean_dataset(df_unified)
    df_encoded, info = create_encoded_dataset(df_cleaned)
    df_ready, X, metadata, features = prepare_analysis_ready_dataset(df_encoded)
    
    # Phase 3: Clustering
    df_clustered, linkage, cluster_info = run_clustering_pipeline(df_ready, feature_cols)
    
    # Phase 4: Supervised Learning
    supervised_results = run_mdr_discrimination(df_clustered, feature_cols)
    
    # Phase 5: Regional Analysis
    regional_results = run_regional_environmental_analysis(df_clustered, feature_cols)
    
    # Phase 6: Integration
    integration_results = run_integration_synthesis(df_clustered, feature_cols, supervised_results)
    
    return df_clustered, integration_results
```

---

## 5.8 Output File Structure

### 5.8.1 Directory Structure at Runtime

```
amr-thesis-project/
├── data/
│   ├── processed/
│   │   ├── unified_raw_dataset.csv
│   │   ├── cleaned_dataset.csv
│   │   ├── cleaning_report.txt
│   │   ├── encoded_dataset.csv
│   │   ├── analysis_ready_dataset.csv
│   │   ├── clustered_dataset.csv
│   │   ├── feature_matrix_X.csv
│   │   ├── metadata.csv
│   │   └── figures/
│   │       ├── resistance_heatmap.png
│   │       ├── dendrogram.png
│   │       ├── clustered_heatmap.png
│   │       ├── cluster_profiles.png
│   │       ├── mdr_distribution.png
│   │       ├── mar_distribution.png
│   │       ├── pca_by_cluster.png
│   │       ├── pca_by_region.png
│   │       └── pca_biplot.png
│   └── models/
│       └── *.joblib (trained models)
├── src/ (source code)
├── app/ (dashboard application)
├── docs/ (documentation)
└── manuscript/ (thesis manuscript)
```

---

## 5.9 Quality Attributes

### 5.9.1 Reliability

| Attribute | Implementation |
|-----------|----------------|
| Error Handling | Try-catch blocks with informative error messages |
| Missing Data | Graceful handling via median imputation |
| Edge Cases | Filters for insufficient samples |

### 5.9.2 Maintainability

| Attribute | Implementation |
|-----------|----------------|
| Modularity | Separate modules for each processing phase |
| Documentation | Comprehensive docstrings and markdown documentation |
| Configuration | Centralized configuration in `config.py` |

### 5.9.3 Reproducibility

| Attribute | Implementation |
|-----------|----------------|
| Random State | Fixed seed (RANDOM_STATE=42) for all random operations |
| Parameter Documentation | All thresholds and parameters documented |
| Version Control | Git-based version control for code and documentation |

---

## 5.10 Security Considerations

### 5.10.1 Data Privacy

| Concern | Mitigation |
|---------|------------|
| Patient Identifiers | System processes environmental samples only |
| Data Anonymization | Isolate codes contain no personally identifiable information |
| Data Transmission | Local processing only; no external transmission |

### 5.10.2 Usage Restrictions

> ⚠️ **CRITICAL DISCLAIMER**: This tool is intended for **exploratory pattern recognition and surveillance analysis only**. It should **NOT** be used for clinical decision support, treatment recommendations, or patient-level predictions.

---

*This chapter is part of the Manuscript for Basic Research: Pattern Recognition of Antibiotic Resistance in Escherichia coli, Salmonella spp., Shigella spp., and Vibrio cholerae from the Water–Fish–Human Nexus.*
