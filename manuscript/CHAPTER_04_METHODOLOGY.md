# CHAPTER 4: METHODOLOGY

## Pattern Recognition of Antibiotic Resistance in *Escherichia coli*, *Salmonella* spp., *Shigella* spp., and *Vibrio cholerae* from the Water–Fish–Human Nexus

---

## 4.1 Research Design

This study employs a **cross-sectional observational design** with quantitative analysis of antimicrobial susceptibility testing (AST) data from bacterial isolates collected across three Philippine regions. The analytical framework integrates unsupervised structure identification, supervised pattern discrimination, and multivariate statistical analysis.

### 4.1.1 Study Objectives Alignment

| Objective | Analytical Approach |
|-----------|-------------------|
| Consolidated dataset establishment | Data preprocessing pipeline (Phase 2) |
| Natural resistance pattern identification | Hierarchical clustering (Phase 3) |
| Pattern discrimination evaluation | Supervised classification (Phase 4) |
| Regional/environmental association analysis | Cross-tabulation, chi-square, PCA (Phase 5) |
| MDR enrichment identification | Integration and synthesis (Phase 6) |

---

## 4.2 Data Collection and Sources

### 4.2.1 Study Sites and Regions

Data were collected from three geographic regions in the Philippines representing diverse agricultural, environmental, and healthcare contexts:

| Region | Code | Sites | Sample Count |
|--------|------|-------|--------------|
| **BARMM** (Bangsamoro Autonomous Region in Muslim Mindanao) | M | APMC, Dayawan, Gadongan, Tuca Kialdan | 250 (50.8%) |
| **Region III - Central Luzon** | P | San Gabriel, San Roque | 140 (30.5%) |
| **Region VIII - Eastern Visayas** | O | Alegria, Larrazabal, OD Hospital | 102 (18.7%) |

### 4.2.2 Sample Sources

Bacterial isolates were obtained from three environmental categories spanning the Water–Fish–Human nexus:

| Category | Sources | Description |
|----------|---------|-------------|
| **Water** | Drinking Water (DW), Lake Water (LW), River Water (RW) | Surface and potable water samples |
| **Fish** | Tilapia (FT), Banak (FB), Gusaw (FG), Kaolang (FK) | Aquaculture and freshwater fish samples |
| **Hospital** | Effluent Water Untreated (EWU), Effluent Water Treated (EWT) | Healthcare facility wastewater |

### 4.2.3 Bacterial Species Identification

Bacterial isolates were identified using standard biochemical methods and recorded with species-level identification. The following species were included in analysis:

- *Escherichia coli*
- *Klebsiella pneumoniae*
- *Enterobacter cloacae*
- *Enterobacter aerogenes*
- *Salmonella* species
- *Vibrio* species

### 4.2.4 Isolate Identification Convention

Each bacterial isolate follows a standardized naming convention encoding metadata:

```
[Species Prefix]_[National Site][Local Site][Sample Source][Replicate][Colony]

Example: EC_OADWR1C3
├── EC    = Escherichia coli
├── O     = Ormoc (National Site)
├── A     = Alegria (Local Site)
├── DW    = Drinking Water (Sample Source)
├── R1    = Replicate 1
└── C3    = Colony 3
```

---

## 4.3 Antimicrobial Susceptibility Testing

### 4.3.1 Antibiotic Panel

A panel of 21 antibiotics across 12 therapeutic classes was tested following Clinical and Laboratory Standards Institute (CLSI) guidelines:

| Antibiotic Class | Antibiotics (Abbreviation) |
|------------------|---------------------------|
| Penicillins | Ampicillin (AM) |
| β-lactam/β-lactamase inhibitor combinations | Amoxicillin-Clavulanate (AMC), Piperacillin-Tazobactam (PRA) |
| Cephalosporins (1st generation) | Cephalothin (CN), Cefazolin (CF) |
| Cephalosporins (3rd/4th generation) | Cefpodoxime (CPD), Cefotaxime (CTX), Ceftriaxone (CFT) |
| Cephamycins | Cefoxitin (CFO) |
| Cephalosporin/BLI combinations | Ceftazidime-Avibactam (CZA) |
| Carbapenems | Imipenem (IPM), Meropenem (MRB) |
| Aminoglycosides | Amikacin (AN), Gentamicin (GM), Neomycin (N) |
| Quinolones/Fluoroquinolones | Nalidixic Acid (NAL), Enrofloxacin (ENR) |
| Tetracyclines | Doxycycline (DO), Tetracycline (TE) |
| Nitrofurans | Nitrofurantoin (FT) |
| Phenicols | Chloramphenicol (C) |
| Folate pathway inhibitors | Trimethoprim-Sulfamethoxazole (SXT) |

### 4.3.2 Interpretation Categories

Antimicrobial susceptibility results were interpreted following CLSI breakpoints:

| Category | Code | Interpretation |
|----------|------|----------------|
| **Susceptible** | S | Infection likely to respond to standard treatment |
| **Intermediate** | I | Uncertain therapeutic effect; higher dosages may be required |
| **Resistant** | R | Treatment unlikely to be effective |

---

## 4.4 Data Preprocessing Pipeline (Phase 2)

The data preprocessing pipeline implements a formal missing data strategy with transparent, defensible methodology.

### 4.4.1 Data Ingestion and Consolidation (Phase 2.1)

**Objectives:**
- Load and merge AST data from multiple CSV files
- Extract metadata from filenames and isolate codes
- Standardize antibiotic abbreviations across sources
- Create unified raw dataset with validated metadata

**Procedures:**
1. Parse CSV files containing structured AST data
2. Extract region and site from filenames
3. Parse isolate codes for metadata (species, source, replicate)
4. Map sample sources to environmental categories
5. Validate metadata coverage statistics

**Output:** `unified_raw_dataset.csv`

### 4.4.2 Data Cleaning (Phase 2.2–2.3)

**Validation Rules:**

| Rule | Description | Action |
|------|-------------|--------|
| Valid Values | Only {S, I, R} allowed | Invalid values set to NULL |
| Species Standardization | Apply controlled vocabulary | Map variants to standard names |
| Antibiotic Standardization | Apply controlled vocabulary | Map abbreviation variants |
| Duplicate Detection | Identify by CODE column | Remove duplicates, keep first |

**Formal Missing Data Strategy:**

| Parameter | Threshold | Rationale |
|-----------|-----------|-----------|
| **Minimum antibiotic coverage** | ≥70% | Antibiotics tested in fewer than 70% of isolates excluded to ensure robust pattern discrimination |
| **Maximum missing data per isolate** | ≤30% | Isolates with >30% missing AST values excluded to maintain data quality |

**Output:**
- `cleaned_dataset.csv`
- `cleaning_report.txt` documenting all decisions

### 4.4.3 Resistance Encoding (Phase 2.4)

Categorical resistance values were converted to ordinal numerical encoding:

| Original Value | Encoded Value | Biological Interpretation |
|----------------|---------------|---------------------------|
| S (Susceptible) | 0 | No resistance detected |
| I (Intermediate) | 1 | Intermediate resistance |
| R (Resistant) | 2 | Full resistance |

**Rationale:** Ordinal encoding preserves biological meaning of resistance levels and enables meaningful distance calculations for clustering.

**Output:** `encoded_dataset.csv`

### 4.4.4 Feature Engineering (Phase 2.5)

**MAR Index (Multiple Antibiotic Resistance Index):**

$$MAR = \frac{a}{b}$$

Where:
- *a* = Number of antibiotics to which the isolate is resistant (R)
- *b* = Total number of antibiotics tested on the isolate

*Reference:* Krumperman PH. (1983). *Applied and Environmental Microbiology*, 46(1), 165–170.

**MDR Classification:**

An isolate is classified as Multi-Drug Resistant (MDR) if it exhibits resistance to at least one agent in **≥3 antimicrobial categories**.

*Reference:* Magiorakos AP, et al. (2012). *Clinical Microbiology and Infection*, 18(3), 268–281.

**Derived Features:**

| Feature | Formula | Description |
|---------|---------|-------------|
| MAR_INDEX_COMPUTED | a / b | Multiple Antibiotic Resistance index (0–1) |
| RESISTANCE_COUNT | Count where encoded = 2 | Total number of resistant antibiotics |
| RESISTANT_CLASSES_COUNT | Count of unique resistant classes | Number of antimicrobial categories with resistance |
| MDR_FLAG | Boolean: Classes ≥ 3 | Multi-Drug Resistant indicator |
| MDR_CATEGORY | "MDR" or "Non-MDR" | Categorical MDR status |

**Output:**
- `analysis_ready_dataset.csv`
- `feature_matrix_X.csv` (encoded resistance features only)
- `metadata.csv` (sample identification and derived features)

---

## 4.5 Unsupervised Structure Identification (Phase 3)

### 4.5.1 Hierarchical Agglomerative Clustering

**Objective:** Discover natural groupings in resistance patterns through unsupervised learning without pre-defined categories.

**Clustering Parameters:**

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Linkage Method** | Ward | Minimizes within-cluster variance, produces compact clusters |
| **Distance Metric** | Euclidean | Captures ordinal resistance differences |
| **Number of Clusters** | 5 | Selected via combined elbow + silhouette analysis |
| **Imputation Strategy** | Median | Robust to outliers in resistance data |

**Cluster Number Selection:**

The number of clusters (k=5) was determined using multiple criteria:

1. **Elbow Method:** Identifying where within-cluster sum of squares (WCSS) reduction diminishes
2. **Silhouette Analysis:** Maximizing average silhouette score while maintaining adequate cluster sizes
3. **Biological Interpretability:** Ensuring clusters represent meaningful phenotypic groupings
4. **Statistical Reliability:** Maintaining minimum cluster sizes for chi-square validity

**Quality Assessment:**

| Metric | Threshold | Interpretation |
|--------|-----------|----------------|
| Silhouette Score | >0.4 | Strong clustering structure |
| Minimum Cluster Size | >20 | Adequate for statistical testing |
| Robustness (ARI) | >0.8 | Stable across methods |

**Output:** `clustered_dataset.csv` with CLUSTER assignments

### 4.5.2 Visualization of Resistance Patterns

| Visualization | Purpose |
|---------------|---------|
| **Dendrogram** | Visualize hierarchical clustering structure |
| **Resistance Heatmap** | Display resistance patterns across isolates |
| **Cluster Profiles** | Characterize mean resistance per cluster |
| **Cluster Distribution** | Assess cluster balance |

---

## 4.6 Supervised Learning for Pattern Discrimination (Phase 4)

### 4.6.1 Objective and Scope

**Objective:** Evaluate how well resistance fingerprints discriminate known categories through two independent tasks:

| Task | Input | Target | Type |
|------|-------|--------|------|
| **Task A: Species discrimination** | Resistance fingerprints | Species | Multi-class |
| **Task B: MDR discrimination** | Resistance fingerprints | MDR flag | Binary |

> **Important:** This is **pattern discrimination**, NOT forecasting or prediction. Results quantify how consistently resistance patterns align with known categories within the analyzed dataset.

### 4.6.2 Data Splitting (Leakage-Safe Protocol)

**Critical:** Train-test split performed **BEFORE** any preprocessing to prevent data leakage.

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Training Set | 80% | Sufficient data for model learning |
| Test Set | 20% | Independent evaluation |
| Stratification | By target variable | Preserves class distribution |
| Random State | 42 (fixed) | Reproducibility |

**Preprocessing Order:**
1. Split FIRST: 80/20 train-test split (stratified)
2. Imputation: Median strategy fit on TRAIN only, applied to both
3. Scaling: StandardScaler fit on TRAIN only, applied to both

### 4.6.3 Model Selection

| Model | Category | Rationale |
|-------|----------|-----------|
| **Logistic Regression** | Linear | Linear baseline with coefficient interpretation |
| **Random Forest** | Tree-based | Nonlinear model with Gini feature importance |
| **k-Nearest Neighbors** | Distance-based | Distance-based consistency check |

### 4.6.4 Evaluation Metrics

| Metric | Formula | Interpretation |
|--------|---------|----------------|
| **Accuracy** | (TP + TN) / Total | Overall correct classifications |
| **Precision (Macro)** | Mean of per-class precision | Treats all classes equally |
| **Recall (Macro)** | Mean of per-class recall | Treats all classes equally |
| **F1-Score (Macro)** | Harmonic mean of macro P and R | Primary comparison metric |

**Macro Averaging:** All classes treated equally regardless of sample size to prevent class imbalance bias.

### 4.6.5 Feature Importance Analysis

| Model | Importance Method |
|-------|-------------------|
| **Random Forest** | Gini importance (mean decrease in impurity) |
| **Logistic Regression** | Absolute coefficient magnitude |

> **Interpretation Discipline:** Importance scores indicate associative contribution to group separation, NOT causal relationships.

---

## 4.7 Regional and Environmental Analysis (Phase 5)

### 4.7.1 Cluster Distribution Analysis

**Cross-tabulation analysis** examines how clusters distribute across:
- Geographic regions (BARMM, Central Luzon, Eastern Visayas)
- Environmental sources (Water, Fish, Hospital)
- Bacterial species

**Chi-square test of independence** assesses statistical significance of cluster-category associations:

| Test | Null Hypothesis | Alternative Hypothesis |
|------|-----------------|----------------------|
| Cluster × Region | Clusters and regions are independent | Clusters differ by region |
| Cluster × Environment | Clusters and sources are independent | Clusters differ by environment |
| Cluster × Species | Clusters and species are independent | Clusters differ by species |

**Effect Size (Cramér's V):**

| Value Range | Interpretation |
|-------------|----------------|
| <0.1 | Negligible |
| 0.1–0.3 | Small |
| 0.3–0.5 | Medium |
| >0.5 | Large |

### 4.7.2 Principal Component Analysis

**Objective:** Reduce dimensionality of resistance profiles and visualize patterns in lower-dimensional space.

**Procedures:**
1. Extract encoded resistance columns
2. Impute missing values (median strategy)
3. Standardize features (StandardScaler)
4. Extract principal components (2 components for visualization)
5. Compute explained variance ratios
6. Calculate and interpret component loadings

---

## 4.8 Integration and Synthesis (Phase 6)

### 4.8.1 Cluster-Supervised Comparison

Compare how unsupervised clusters align with supervised classification targets:

**Cluster Purity:**
$$Purity(cluster) = \frac{max(category\_count)}{cluster\_size}$$

### 4.8.2 Resistance Archetype Identification

For each cluster, compute:
- Mean resistance profile per antibiotic
- High resistance antibiotics (mean > 1.5)
- Low resistance antibiotics (mean < 0.5)
- Overall resistance level classification

| Mean Resistance Score | Level |
|-----------------------|-------|
| > 1.5 | High resistance |
| > 1.0 | Moderate-high resistance |
| > 0.5 | Moderate resistance |
| ≤ 0.5 | Low resistance |

### 4.8.3 MDR Enrichment Analysis

For each grouping variable (cluster, region, environment, species):

**Fold Enrichment:**
$$Fold\_Enrichment = \frac{Group\_MDR\_Rate}{Overall\_MDR\_Rate}$$

---

## 4.9 Software and Tools

### 4.9.1 Programming Environment

| Component | Specification |
|-----------|---------------|
| **Language** | Python 3.8+ |
| **Random State** | 42 (fixed for reproducibility) |

### 4.9.2 Core Libraries

| Library | Purpose |
|---------|---------|
| **pandas** | Data manipulation, CSV I/O |
| **numpy** | Numerical computing |
| **scipy** | Hierarchical clustering, statistical tests |
| **scikit-learn** | Classification, PCA, preprocessing |
| **matplotlib** | Static visualization |
| **seaborn** | Statistical visualization |
| **streamlit** | Interactive dashboard |
| **joblib** | Model persistence |

---

## 4.10 Quality Control and Validation

### 4.10.1 Data Quality Checks

| Check | Criteria | Action |
|-------|----------|--------|
| Missing values | >30% per isolate | Exclude isolate |
| Missing values | <70% coverage per antibiotic | Exclude antibiotic |
| Duplicates | By CODE column | Remove duplicates |
| Invalid values | Not S, I, R, or null | Set to null |

### 4.10.2 Model Validation

| Method | Purpose |
|--------|---------|
| Train-test split | Assess generalization within dataset |
| Stratified sampling | Maintain class balance |
| Multiple model comparison | Identify robust patterns |
| Effect size reporting | Quantify association strength |

---

## 4.11 Ethical Considerations

### 4.11.1 Data Handling

- **Anonymization:** No patient-level identifiers collected or processed
- **Environmental Focus:** Primary focus on environmental and water samples
- **Data Security:** Processed data stored locally; no external transmission

### 4.11.2 Research Purpose

This methodology was developed for **academic research purposes** as part of a thesis project on antimicrobial resistance surveillance. Results should not be used for clinical decision support.

---

## 4.12 Limitations of the Methodology

### 4.12.1 Study Design Limitations

| Limitation | Impact | Mitigation |
|------------|--------|------------|
| Cross-sectional design | Cannot infer temporal trends | Focus on pattern identification |
| No longitudinal data | Cannot assess resistance evolution | Acknowledge in limitations |
| Observational design | Cannot establish causation | Use associative language |

### 4.12.2 Analytical Limitations

| Limitation | Impact | Mitigation |
|------------|--------|------------|
| Clustering subjectivity | Parameter choices affect results | Document all parameters, test alternatives |
| No cross-validation | Single train-test split | Stratified sampling, multiple models |
| Phenotypic data only | Cannot confirm mechanisms | Acknowledge need for genomic validation |

---

*This chapter is part of the Manuscript for Basic Research: Pattern Recognition of Antibiotic Resistance in Escherichia coli, Salmonella spp., Shigella spp., and Vibrio cholerae from the Water–Fish–Human Nexus.*
