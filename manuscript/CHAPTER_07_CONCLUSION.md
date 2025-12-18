# CHAPTER 7: CONCLUSION

## Pattern Recognition of Antibiotic Resistance in *Escherichia coli*, *Salmonella* spp., *Shigella* spp., and *Vibrio cholerae* from the Water–Fish–Human Nexus

---

## 7.1 Summary of Contributions

This thesis presents the development and application of a comprehensive antimicrobial resistance (AMR) pattern recognition pipeline, demonstrating the utility of unsupervised machine learning for epidemiological surveillance in environmental bacteria. The work makes three primary contributions:

### 7.1.1 Methodological Contribution

A rigorous, reproducible AMR analysis framework was implemented with the following characteristics:

- **Leakage-safe preprocessing:** Train-test splits performed before all transformations (scaling, imputation), preventing data leakage that could inflate model performance estimates
- **Documented parameter choices:** All clustering parameters, distance metrics, and thresholds explicitly justified
- **Multi-method validation:** Ward's linkage validated through robustness checks with alternative distance metrics (Adjusted Rand Index > 0.8)
- **Statistical rigor:** Effect sizes (Cramér's V) reported alongside p-values; Bonferroni correction applied to co-resistance analysis

This pipeline serves as a template for standardized AMR surveillance analysis that can be applied to other regional datasets, enhancing reproducibility and comparability across studies.

### 7.1.2 Biological Findings

Analysis of 491 environmental bacterial isolates (6 species) from three Philippine regions revealed:

**1. Five Distinct Resistance Archetypes**

Hierarchical clustering identified species-specific, geographically structured, and environmentally associated resistance patterns:

| Archetype | Dominant Species | MDR Rate | Characterization |
|-----------|------------------|----------|-----------------|
| C1 | *Salmonella* | 26.1% | Aminoglycoside-resistant, water-associated |
| C2 | *E. cloacae* | 20.4% | Beta-lactam-resistant |
| C3 | *E. coli* | **54.5%** | **Tetracycline-MDR hotspot** |
| C4 | *E. coli* | **0.0%** | Pan-susceptible |
| C5 | *K. pneumoniae* | 1.4% | Low-level resistance |

**2. Intraspecific *E. coli* Heterogeneity**

Two opposing *E. coli* phenotypes (Clusters 3 and 4) demonstrate that intraspecific diversity can exceed interspecific differences in resistance profiles. Despite sharing similar geographic and environmental distributions, these clusters exhibit fundamentally different resistance patterns (54.5% vs. 0.0% MDR).

**3. Species-Driven Clustering**

Species identity (Cramér's V = 0.765) is the dominant factor driving cluster membership, exceeding geographic (V = 0.321) and environmental (V = 0.204) factors. This finding supports species-stratified surveillance approaches.

**4. Tetracycline-MDR Signature**

MDR status is strongly associated with tetracycline resistance (TE, DO), suggesting tetracycline use in aquaculture as a potential selective factor. The co-resistance pattern (TE-DO-SXT-AM) is consistent with mobile genetic element-mediated co-carriage.

### 7.1.3 Public Health Insights

The findings inform AMR surveillance priorities:

- **Regional baseline establishment:** Five resistance archetypes provide reference profiles for future monitoring in the Philippines
- **MDR hotspot identification:** Cluster 3 (*E. coli*-Tetracycline-MDR) at 54.5% MDR warrants targeted surveillance attention
- **Aquaculture-associated resistance:** Tetracycline resistance dominance in fish-associated isolates suggests antibiotic stewardship opportunities in aquaculture

---

## 7.2 Key Findings Summary

The following represent the most significant findings from this study:

| Finding | Evidence | Significance |
|---------|----------|--------------|
| *E. coli* phenotypic split | C3 (54.5% MDR) vs. C4 (0% MDR) | Intraspecific diversity exceeds interspecific differences |
| Species drives clustering | Cramér's V = 0.765 | Species identity is the dominant factor, not environment |
| Geographic structuring | χ² = 101.18, p < 10⁻¹⁸ | Resistance patterns show regional specificity |
| Cluster-MDR alignment | Cramér's V = 0.559 | Unsupervised clusters capture clinically relevant patterns |
| Tetracycline-MDR signature | TE mean difference = +1.51 | Coordinated resistance consistent with mobile elements |

---

## 7.3 Addressing Research Objectives

### Objective 1: Consolidated Dataset Establishment ✓

A quality-controlled dataset of 491 bacterial isolates was established, consolidating AST data from nine source files across three Philippine regions. Formal missing data strategy achieved 84.2% retention rate with transparent documentation.

### Objective 2: Natural Resistance Pattern Identification ✓

Hierarchical clustering (Ward's linkage, Euclidean distance, k=5) identified five distinct resistance archetypes with silhouette score 0.488 indicating strong clustering structure. Clusters demonstrate biological interpretability with species-specific and resistance-level characterization.

### Objective 3: Pattern Discrimination Evaluation ✓

Supervised learning demonstrated moderate-to-strong discriminative capacity:
- Species discrimination: F1 = 0.724 (Random Forest)
- Cluster discrimination: F1 = 0.912 (Random Forest)
- Results confirm resistance fingerprints contain species-distinguishing information.

### Objective 4: Regional/Environmental Association Characterization ✓

Statistical analysis revealed hierarchical factor importance:
- Species: Cramér's V = 0.765 (dominant)
- Region: Cramér's V = 0.321 (moderate)
- Environment: Cramér's V = 0.204 (weak)

Principal component analysis visualized resistance pattern structure (39.9% variance in PC1-PC2).

### Objective 5: MDR Enrichment Pattern Identification ✓

MDR enrichment analysis identified:
- **Cluster hotspot:** Cluster 3 at 2.86× enrichment
- **MDR signature:** Tetracycline-based (TE, DO, SXT, AM)
- Cluster-MDR association: Cramér's V = 0.559 (large effect)

### Objective 6: Actionable Surveillance Insights ✓

Integration and synthesis generated:
- Five characterized resistance archetypes as baseline reference profiles
- Identification of MDR hotspot cluster for targeted surveillance
- Species-stratified surveillance recommendations
- Aquaculture-associated resistance patterns for stewardship consideration

---

## 7.4 Hypothesis Testing Summary

| Hypothesis | Result | Evidence |
|------------|--------|----------|
| **H₁:** AMR is structured | **SUPPORTED** | 5 clusters, silhouette = 0.488 |
| **H₂:** Species-driven patterns | **SUPPORTED** | Species V = 0.765 > Region V = 0.321 |
| **H₃:** Intraspecific heterogeneity | **SUPPORTED** | *E. coli* C3 (54.5% MDR) vs. C4 (0.0% MDR) |
| **H₄:** Environmental association | **PARTIALLY SUPPORTED** | Significant but weak (V = 0.204) |
| **H₅:** Co-resistance patterns | **SUPPORTED** | TE-DO-SXT-AM signature consistent with mobile elements |

---

## 7.5 Limitations

The principal limitations of this work include:

1. **Cross-sectional design:** Cannot assess temporal trends, resistance evolution, or seasonal variation
2. **Phenotypic data only:** Without genomic validation, resistance mechanisms remain unconfirmed
3. **Sampling imbalance:** BARMM contributes 50.8% of isolates, potentially biasing regional comparisons
4. **PCA variance capture:** First two components explain only 39.9% of variance; 2D visualizations are simplified representations
5. **Environmental categorization:** Broad categories (Water, Fish, Hospital) may mask finer-grained associations
6. **Clinical applicability:** Results are for exploratory surveillance analysis only; not validated for clinical decision support

---

## 7.6 Implications

### 7.6.1 For AMR Surveillance

The identification of species-stratified resistance archetypes suggests that:

- **Surveillance should be species-specific:** Aggregate statistics mask intraspecific heterogeneity evident in *E. coli* Clusters 3 and 4
- **Regional baselines established:** The five archetypes provide reference profiles against which future surveillance data can be compared
- **Pattern recognition integration:** Clustering approaches should complement traditional susceptibility reporting

### 7.6.2 For One Health

While environmental associations were weaker than expected (Cramér's V = 0.204), the detection of similar resistance patterns across water, fish, and hospital-associated samples supports:

- Integration of environmental surveillance into clinical AMR monitoring
- Recognition that resistance traverses environmental boundaries
- Need for higher-resolution environmental sampling to detect finer associations

### 7.6.3 For Policy Consideration

> **Note:** The following considerations are based on observational findings from a single cross-sectional dataset and require further validation before implementation.

- **Aquaculture antibiotic practices:** Tetracycline-dominated resistance in fish-associated isolates suggests that veterinary antibiotic use practices may merit review
- **Regional surveillance priorities:** Findings suggest BARMM region may warrant consideration for enhanced AMR surveillance efforts
- **Antibiogram development:** Observed co-resistance patterns may provide useful context for regional antibiogram development

---

## 7.7 Closing Statement

This thesis demonstrates that structured resistance patterns exist in environmental bacteria from the Philippines, identifiable through systematic application of machine learning methods. The five resistance archetypes—particularly the dichotomous *E. coli* phenotypes—reveal biological complexity that traditional aggregate reporting obscures.

The methodological rigor of the pipeline, with its emphasis on reproducibility and transparent parameter justification, provides a framework that extends beyond this specific dataset. As environmental AMR surveillance becomes increasingly important under One Health frameworks, such standardized analytical approaches will be essential for generating actionable public health insights.

While limitations exist, particularly regarding the single-timepoint design and absence of genomic validation, this work establishes foundational baseline patterns and demonstrates proof-of-concept for machine learning-enhanced AMR surveillance in resource-limited settings.

**The evidence presented here supports the thesis that environmental AMR in the Philippines is structured, species-driven, and amenable to systematic pattern recognition—knowledge that can directly inform regional surveillance priorities and antibiotic stewardship discussions.**

---

*This chapter is part of the Manuscript for Basic Research: Pattern Recognition of Antibiotic Resistance in Escherichia coli, Salmonella spp., Shigella spp., and Vibrio cholerae from the Water–Fish–Human Nexus.*
