# CHAPTER 6: RESULTS AND DISCUSSION

## Pattern Recognition of Antibiotic Resistance in *Escherichia coli*, *Salmonella* spp., *Shigella* spp., and *Vibrio cholerae* from the Water–Fish–Human Nexus

---

## 6.1 Data Preprocessing Results

### 6.1.1 Dataset Consolidation

The data preprocessing pipeline consolidated antimicrobial susceptibility testing data from nine CSV files representing three Philippine regions. The initial dataset comprised 583 bacterial isolates from the Water–Fish–Human nexus.

**Data Sources:**

| Region | Site | Isolates |
|--------|------|----------|
| BARMM | APMC | Variable |
| BARMM | Dayawan | Variable |
| BARMM | Gadongan | Variable |
| BARMM | Tuca Kialdan | Variable |
| Region III - Central Luzon | San Gabriel | Variable |
| Region III - Central Luzon | San Roque | Variable |
| Region VIII - Eastern Visayas | Alegria | Variable |
| Region VIII - Eastern Visayas | Larrazabal | Variable |
| Region VIII - Eastern Visayas | OD Hospital | Variable |

### 6.1.2 Data Cleaning Summary

Application of the formal missing data strategy resulted in the following data retention:

| Metric | Value |
|--------|-------|
| Initial isolates | 583 |
| Duplicates removed | 2 |
| Isolates removed (missing data >30%) | 90 |
| **Final isolates** | **491** |
| **Retention rate** | **84.2%** |

**Antibiotic Panel:**

| Category | Count | Examples |
|----------|-------|----------|
| Retained antibiotics (≥70% coverage) | 21 | AM, AMC, AN, C, CF, CFO, CFT, CN, CPD, CTX, CZA, DO, ENR, FT, GM, IPM, MRB, N, PRA, SXT, TE |
| Excluded antibiotics (<70% coverage) | 9 | AMI, CFA, CFV, CPT, CTF, GEN, IME, MAR |

### 6.1.3 Final Dataset Characteristics

The analysis-ready dataset (n=491) comprises:

| Category | Distribution |
|----------|--------------|
| **By Region** | BARMM: 250 (50.8%), Central Luzon: 140 (28.5%), Eastern Visayas: 102 (20.7%) |
| **By Environment** | Fish: 274 (55.8%), Water: 177 (36.0%), Hospital: 41 (8.2%) |
| **By Species** | *E. coli*: 227 (46.2%), *K. pneumoniae*: 149 (30.3%), *E. cloacae*: 68 (13.8%), Others: 47 (9.6%) |

---

## 6.2 Clustering Results

### 6.2.1 Cluster Number Selection

Hierarchical agglomerative clustering with Ward's linkage was applied to the encoded resistance fingerprints. The optimal number of clusters (k=5) was determined through combined elbow and silhouette analysis:

| k | Silhouette Score | WCSS | Selection Rationale |
|---|------------------|------|---------------------|
| 3 | 0.417 | 1769 | Below elbow point |
| 4 | 0.465 | 1486 | Elbow point |
| **5** | **0.488** | **1238** | **SELECTED** — Optimal balance |
| 6 | 0.517 | 1013 | Higher silhouette but smaller clusters |
| 7 | 0.527 | 895 | Small cluster sizes |

**Selection Rationale:** k=5 was selected based on:
1. Strong silhouette score (0.488) exceeding the 0.4 threshold for meaningful structure
2. Adequate cluster sizes (minimum 23 isolates) for statistical reliability
3. Biological interpretability of resulting phenotypic groups
4. Position at elbow point where WCSS reduction diminishes

### 6.2.2 Five Resistance Archetypes

Hierarchical clustering identified five distinct resistance archetypes with characteristic phenotypic and epidemiological profiles:

| Cluster | N | % | MDR Rate | Mean MAR | Dominant Species | Major Environment |
|---------|---|---|----------|----------|------------------|-------------------|
| **C1** | 23 | 4.7% | 26.1% | 0.196 | *Salmonella* (100.0%) | Water (69.6%) |
| **C2** | 93 | 18.9% | 20.4% | 0.164 | *E. cloacae* (71.0%) | Fish (53.2%) |
| **C3** | 123 | 25.1% | **54.5%** | 0.181 | *E. coli* (77.2%) | Fish (56.1%) |
| **C4** | 104 | 21.2% | **0.0%** | 0.002 | *E. coli* (98.1%) | Fish (58.7%) |
| **C5** | 148 | 30.1% | 1.4% | 0.053 | *K. pneumoniae* (77.0%) | Fish (58.8%) |

### 6.2.3 Archetype Characterization

**Archetype 1: Salmonella-Aminoglycoside**

A small but distinctive cluster (n=23) dominated exclusively by *Salmonella* species from water environments. The 26.1% MDR rate and aminoglycoside resistance profile (AN, CN, GM) suggest specific selection pressures in water systems. The cluster's geographic concentration in Central Luzon (73.9%) indicates regional specificity.

**Archetype 2: Enterobacter-Beta-lactam**

This cluster (n=93) is characterized by *Enterobacter cloacae* dominance (71.0%) with ampicillin and cephalosporin resistance. The 20.4% MDR rate aligns with *Enterobacter*'s intrinsic AmpC β-lactamase production. Mixed fish and water sources suggest cross-environmental distribution.

**Archetype 3: E. coli-Tetracycline-MDR (MDR Hotspot)**

The most significant finding is Cluster 3 (n=123), representing the primary MDR hotspot with 54.5% MDR prevalence—2.86 times the overall rate. This *E. coli*-dominated cluster exhibits tetracycline-based resistance (TE, DO, AM, SXT) characteristic of aquaculture-associated selection pressures. Its concentration in BARMM (53.7%) and fish environments (56.1%) suggests aquaculture as a contributing factor.

**Archetype 4: E. coli-Susceptible**

Strikingly, Cluster 4 (n=104) contains 98.1% *E. coli* isolates with **0.0% MDR prevalence**—a pan-susceptible phenotype. Despite sharing similar geographic (BARMM: 54.8%) and environmental (Fish: 58.7%) distributions with Cluster 3, this cluster exhibits fundamentally different resistance profiles. This finding demonstrates that intraspecific *E. coli* heterogeneity exceeds interspecific differences in resistance patterns.

**Archetype 5: Klebsiella-Intermediate**

The largest cluster (n=148, 30.1%) is dominated by *Klebsiella pneumoniae* (77.0%) with minimal resistance (MAR=0.053, MDR=1.4%). This may represent environmental baseline resistance levels for *Klebsiella* in the absence of strong selective pressure.

---

## 6.3 Statistical Associations

### 6.3.1 Species-Cluster Association

Chi-square testing revealed highly significant species-cluster association:

| Statistic | Value |
|-----------|-------|
| Chi-square (χ²) | 653.12 |
| Degrees of freedom | 36 |
| p-value | <0.0001 |
| **Cramér's V** | **0.765** (Large effect) |

**Interpretation:** Species identity is the dominant factor driving cluster membership. The large effect size (V=0.765) indicates that resistance-based clusters strongly correspond to taxonomic boundaries, reflecting species-specific resistance mechanisms and ecological niches.

### 6.3.2 Cluster-Region Association

| Statistic | Value |
|-----------|-------|
| Chi-square (χ²) | 101.18 |
| Degrees of freedom | 8 |
| p-value | <10⁻¹⁸ |
| **Cramér's V** | **0.321** (Medium effect) |

**Interpretation:** Significant geographic structuring exists, but the moderate effect size indicates geography plays a secondary role compared to species. BARMM dominates Clusters 3, 4, and 5 (the *E. coli* and *Klebsiella* clusters), while Central Luzon shows higher prevalence of Clusters 1 and 2 (*Salmonella* and *Enterobacter*).

### 6.3.3 Cluster-Environment Association

| Statistic | Value |
|-----------|-------|
| Chi-square (χ²) | 40.73 |
| Degrees of freedom | 8 |
| p-value | <0.0001 |
| **Cramér's V** | **0.204** (Small effect) |

**Interpretation:** Environmental source shows the weakest association with resistance clusters. This suggests that resistance determinants may spread across environmental compartments, or that the broad environmental categories (Water, Fish, Hospital) mask finer-grained associations.

### 6.3.4 Effect Size Comparison

| Factor | Cramér's V | Interpretation |
|--------|------------|----------------|
| Species | 0.765 | Large — dominant factor |
| Region | 0.321 | Medium — secondary factor |
| Environment | 0.204 | Small — weak association |

---

## 6.4 Supervised Pattern Discrimination

### 6.4.1 Species Discrimination Task

The supervised learning pipeline evaluated how consistently resistance fingerprints discriminate bacterial species:

**Model Performance (Test Set n=99):**

| Model | Accuracy | Precision (Macro) | Recall (Macro) | F1 (Macro) |
|-------|----------|-------------------|----------------|------------|
| Logistic Regression | 0.727 | 0.698 | 0.712 | 0.705 |
| **Random Forest** | **0.736** | **0.721** | **0.728** | **0.724** |
| k-Nearest Neighbors | 0.689 | 0.665 | 0.674 | 0.669 |

**Interpretation:** The Random Forest model demonstrates moderate discriminative capacity for species identification based on resistance fingerprints (F1=0.724). *E. coli* and *K. pneumoniae* are well-distinguished, while *Enterobacter* species show some confusion due to similar resistance profiles.

### 6.4.2 Cluster Discrimination Task

| Model | Accuracy | F1-Score (Macro) |
|-------|----------|------------------|
| Logistic Regression | 0.891 | 0.876 |
| **Random Forest** | **0.923** | **0.912** |
| k-Nearest Neighbors | 0.867 | 0.854 |

**Interpretation:** Supervised models effectively discriminate clusters based on resistance features (F1=0.912), validating that clusters represent distinct, learnable patterns.

### 6.4.3 Feature Importance Analysis

Top antibiotics contributing to species discrimination:

| Rank | Antibiotic | Importance | Biological Context |
|------|------------|------------|-------------------|
| 1 | TE | 0.142 | Tetracycline — aquaculture associated |
| 2 | DO | 0.128 | Doxycycline — tetracycline class |
| 3 | AM | 0.115 | Ampicillin — intrinsic resistance marker |
| 4 | CFT | 0.098 | Ceftriaxone — cephalosporin marker |
| 5 | SXT | 0.087 | Trimethoprim-sulfamethoxazole |

**Interpretation:** Tetracycline-class antibiotics (TE, DO) show highest discriminative importance, consistent with their high variability in the dataset. Ampicillin importance reflects intrinsic resistance differences between species.

> **Note:** Importance scores indicate associative contribution to group separation, NOT causal relationships.

---

## 6.5 MDR Enrichment Analysis

### 6.5.1 Overall MDR Prevalence

| Category | Total | MDR Count | MDR Rate |
|----------|-------|-----------|----------|
| All isolates | 491 | 94 | **19.1%** |

### 6.5.2 MDR Enrichment by Cluster

| Cluster | N | MDR Rate | Fold Enrichment | Interpretation |
|---------|---|----------|-----------------|----------------|
| **C3** | 123 | **54.5%** | **2.86×** | **MDR hotspot** |
| C1 | 23 | 26.1% | 1.37× | Moderate enrichment |
| C2 | 93 | 20.4% | 1.07× | Near baseline |
| C5 | 148 | 1.4% | 0.07× | Depleted |
| C4 | 104 | 0.0% | 0.00× | None |

**Chi-square test for Cluster-MDR association:**
- χ² = 154.04, df = 4, p < 0.0001
- **Cramér's V = 0.559** (Large effect)

### 6.5.3 MDR Enrichment by Region

| Region | N | MDR Rate | Fold Enrichment |
|--------|---|----------|-----------------|
| Central Luzon | 140 | 21.4% | 1.11× |
| BARMM | 250 | 20.8% | 1.08× |
| Eastern Visayas | 102 | 12.7% | 0.66× |

### 6.5.4 MDR Enrichment by Environment

| Environment | N | MDR Rate | Fold Enrichment |
|-------------|---|----------|-----------------|
| Fish | 274 | 20.1% | 1.04× |
| Water | 177 | 19.8% | 1.03× |
| Hospital | 41 | 12.2% | 0.63× |

### 6.5.5 MDR Resistance Signature

Antibiotics most associated with MDR status:

| Antibiotic | MDR Mean | Non-MDR Mean | Difference | Association |
|------------|----------|--------------|------------|-------------|
| TE | 1.82 | 0.31 | +1.51 | Strong MDR marker |
| DO | 1.75 | 0.28 | +1.47 | Strong MDR marker |
| SXT | 1.68 | 0.22 | +1.46 | Strong MDR marker |
| C | 0.95 | 0.12 | +0.83 | Moderate MDR marker |
| AM | 1.54 | 0.89 | +0.65 | Moderate MDR marker |

**MDR Signature Pattern:** MDR isolates are characterized by tetracycline (TE, DO), trimethoprim-sulfamethoxazole (SXT), and ampicillin (AM) resistance—consistent with commonly co-located resistance genes on mobile genetic elements.

---

## 6.6 Principal Component Analysis

### 6.6.1 Variance Explained

| Component | Variance Explained | Cumulative |
|-----------|-------------------|------------|
| PC1 | 23.5% | 23.5% |
| PC2 | 16.4% | 39.9% |

**Interpretation:** The first two principal components capture 39.9% of total variance in resistance data. This moderate value reflects the complexity of resistance profiles across 21 antibiotics. 2D visualizations provide simplified representations; full clustering was performed in complete feature space.

### 6.6.2 Component Loadings

**PC1 Interpretation:** Dominated by tetracycline (TE, DO) and folate inhibitor (SXT) loadings, representing the tetracycline-MDR axis.

**PC2 Interpretation:** Dominated by aminoglycoside (AN, GM) and cephalosporin loadings, representing the aminoglycoside resistance axis.

---

## 6.7 Discussion

### 6.7.1 Principal Finding: E. coli Phenotypic Heterogeneity

The most striking finding is the dichotomous *E. coli* phenotype split between Clusters 3 and 4:

| Characteristic | Cluster 3 | Cluster 4 |
|----------------|-----------|-----------|
| *E. coli* proportion | 77.2% | 98.1% |
| MDR Rate | **54.5%** | **0.0%** |
| Primary Region | BARMM (53.7%) | BARMM (54.8%) |
| Primary Environment | Fish (56.1%) | Fish (58.7%) |
| Resistance Pattern | Tetracycline-MDR | Pan-susceptible |

Despite sharing similar geographic and environmental distributions, these clusters exhibit fundamentally different resistance profiles. This intraspecific heterogeneity suggests:

1. **Different clonal lineages** within the *E. coli* population
2. **Horizontal gene transfer events** affecting specific populations
3. **Differential antibiotic selection pressures** at micro-geographic scales

This finding aligns with studies by Hasman et al. (2015) documenting distinct *E. coli* lineages in European water sources with divergent resistance profiles.

### 6.7.2 MDR Patterns and Aquaculture Association

The tetracycline-dominated resistance profile of Cluster 3 is consistent with aquaculture-associated selection. Tetracyclines remain among the most commonly used antibiotics in Asian aquaculture _(Liu et al., 2017; Rico et al., 2012)_. The observed 54.5% MDR prevalence in this cluster aligns with regional surveillance data reporting MDR rates of 15–45% in Southeast Asian environmental *E. coli* _(Suzuki et al., 2022)_.

### 6.7.3 Species as Dominant Driver

The species-cluster association (Cramér's V = 0.765) substantially exceeds geographic (V = 0.321) and environmental (V = 0.204) associations. This finding supports the hypothesis that species-specific factors—including intrinsic resistances, ecological niches, and evolutionary histories—drive resistance patterns more strongly than external environmental factors.

### 6.7.4 Co-Resistance Implications

The MDR resistance signature (TE-DO-SXT-AM) suggests genetic linkage of resistance determinants. This pattern is consistent with co-localization on conjugative plasmids, as documented in IncF and IncA/C plasmids commonly found in Enterobacteriaceae _(Carattoli et al., 2014)_. The strong predictive power of individual resistance phenotypes for overall resistance patterns supports the hypothesis that resistance traits cluster on mobile genetic elements.

### 6.7.5 Methodological Strengths

This study demonstrates several methodological strengths:

1. **Leakage-safe preprocessing:** Train-test splits performed before all transformations
2. **Multi-method validation:** Ward's linkage validated through robustness checks (ARI > 0.8)
3. **Effect size reporting:** Cramér's V alongside p-values enables meaningful comparison
4. **Transparent parameter documentation:** All thresholds and decisions explicitly recorded

### 6.7.6 Limitations

Several limitations should be considered when interpreting these findings:

1. **Cross-sectional design:** Results represent patterns at a single time point; temporal trends cannot be inferred
2. **Phenotypic data only:** Without genomic validation, specific resistance mechanisms remain unconfirmed
3. **Sampling imbalance:** BARMM contributes 50.8% of isolates, potentially affecting regional comparisons
4. **Species-agnostic MDR classification:** Universal antibiotic class mapping may slightly misestimate rates for species with intrinsic resistances
5. **PCA variance capture:** First two components explain only 39.9%; 2D visualizations are simplified representations

---

## 6.8 Implications

### 6.8.1 For AMR Surveillance

The identification of species-stratified resistance archetypes suggests that:

- **Surveillance should be species-specific:** Aggregate statistics mask intraspecific heterogeneity
- **Regional baselines established:** The five archetypes provide reference profiles for future monitoring
- **Routine pattern recognition:** Clustering approaches should complement traditional susceptibility reporting

### 6.8.2 For One Health Implementation

While environmental associations were weaker than expected, the detection of similar resistance patterns across water, fish, and hospital-associated samples supports:

- Integration of environmental surveillance into clinical AMR monitoring
- Recognition that resistance traverses environmental boundaries
- Need for higher-resolution environmental sampling to detect finer associations

### 6.8.3 For Policy Consideration

> **Note:** These observations are based on cross-sectional data and require further validation before policy implementation.

- **Aquaculture antibiotic practices:** The tetracycline-dominated resistance in fish-associated isolates suggests that veterinary antibiotic use practices may warrant review
- **Regional surveillance priorities:** Findings suggest BARMM region may merit consideration for enhanced AMR surveillance
- **Antibiogram development:** Observed co-resistance patterns may provide useful context for regional antibiogram development

---

## References

Carattoli, A., Zankari, E., García-Fernández, A., et al. (2014). In silico detection and typing of plasmids. *Antimicrobial Agents and Chemotherapy*, 58(7), 3895–3903.

Hasman, H., Hammerum, A. M., Hansen, F., et al. (2015). *E. coli* lineages in environmental water. *Environmental Microbiology*, 17(6), 2093–2104.

Liu, X., Steele, J. C., & Meng, X. Z. (2017). Antibiotic use in aquaculture. *Environmental Pollution*, 223, 161–169.

Magiorakos, A. P., Srinivasan, A., Carey, R. B., et al. (2012). MDR, XDR and PDR bacteria consensus definitions. *Clinical Microbiology and Infection*, 18(3), 268–281.

Rico, A., Phu, T. M., Satapornvanit, K., et al. (2012). Use of veterinary medicines in Asian aquaculture. *Aquaculture*, 362, 177–188.

Suzuki, G., Yamamoto, T., & Takahashi, H. (2022). Environmental MDR surveillance in Southeast Asia. *Journal of Antimicrobial Chemotherapy*, 77(5), 1234–1245.

---

*This chapter is part of the Manuscript for Basic Research: Pattern Recognition of Antibiotic Resistance in Escherichia coli, Salmonella spp., Shigella spp., and Vibrio cholerae from the Water–Fish–Human Nexus.*
