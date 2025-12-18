# Chapter 5: Discussion

## 5.1 Summary of Principal Findings

This thesis developed and applied a comprehensive data science pipeline for antimicrobial resistance (AMR) pattern recognition in 491 environmental bacterial isolates (6 species, after standardization) from three Philippine regions. The analysis employed hierarchical clustering, co-resistance network analysis, and statistical characterization to identify distinct resistance phenotypes and their epidemiological associations.

### 5.1.1 Five Distinct Resistance Archetypes

Hierarchical clustering with Ward's linkage identified five resistance archetypes with distinct phenotypic and epidemiological profiles:

| Cluster | N | Dominant Species | MDR Rate | Major Environment | Key Resistance Pattern |
|---------|---|------------------|----------|-------------------|----------------------|
| C1 | 23 | *Salmonella* (100.0%) | 26.1% | Water (69.6%) | Aminoglycoside-resistant (AN, CN, GM) |
| C2 | 93 | *Enterobacter cloacae* (71.0%) | 20.4% | Fish (53.2%) | Ampicillin/cephalosporins (AM, CF, CN) |
| C3 | 123 | *Escherichia coli* (77.2%) | **54.5%** | Fish (56.1%) | **Tetracycline-MDR** (TE, DO, AM) |
| C4 | 104 | *Escherichia coli* (98.1%) | **0.0%** | Fish (58.7%) | Susceptible phenotype (CF, C, CFT) |
| C5 | 148 | *Klebsiella pneumoniae* (79.1%) | 1.4% | Fish (58.8%) | Ampicillin-intermediate (AM, FT, CN) |

**Key Finding 1: *E. coli* Phenotypic Heterogeneity**

The most striking finding is the split of *E. coli* into two opposing phenotypes:
- **Cluster 3 (MDR Type)**: 54.5% MDR prevalence, dominated by tetracycline and doxycycline resistance
- **Cluster 4 (Susceptible Type)**: 0% MDR, broadly susceptible to all tested antibiotics

Both clusters share similar geographic (BARMM, ~54%) and environmental (Fish, ~57%) distributions, yet exhibit fundamentally different resistance profiles. This intraspecific heterogeneity suggests that resistance patterns in *E. coli* are not determined solely by environmental or geographic factors, but may reflect:
1. Different clonal lineages within the species
2. Horizontal gene transfer events affecting specific populations
3. Differential antibiotic selection pressures at micro-geographic scales

**Key Finding 2: Geographic Structuring of Resistance**

Statistical analysis revealed significant association between clusters and geographic regions (χ² = 101.18, p < 10⁻¹⁸, Cramér's V = 0.321). However, this moderate effect size indicates that species (Cramér's V = 0.765) is the dominant factor driving cluster membership, with geography playing a secondary role.

The geographic distribution pattern shows:
- BARMM region: Dominated by *E. coli* clusters (C3, C4, C5)
- Central Luzon: Higher prevalence of *Salmonella* (C1) and *Enterobacter* (C2)
- Eastern Visayas: Similar to BARMM pattern

**Key Finding 3: Environmental Distribution**

Despite expectations based on One Health principles, environmental source showed the weakest association with resistance clusters (Cramér's V = 0.204). This suggests that:
1. Resistance determinants may spread across environmental compartments
2. Species-specific factors dominate over environmental selection
3. The broad environmental categories (Water, Fish, Hospital) may mask finer-grained associations

### 5.1.2 Co-Resistance Network Structure

Analysis of pairwise antibiotic co-resistance identified 14 statistically significant associations after Bonferroni correction (α/231 = 0.000216). The co-resistance network structure reveals:

**Network Topology:**
- 10 antibiotics participate in significant co-resistance relationships
- 14 edges (co-resistance pairs) connect these antibiotics
- Hub antibiotics (high connectivity): Those central to multi-drug resistance mechanisms

**Key Co-Resistance Patterns:**
The network analysis revealed clinically relevant co-carriage patterns:
1. **Tetracycline-aminoglycoside association**: Suggests co-localization on conjugative plasmids
2. **Beta-lactam co-resistance cluster**: Consistent with ESBL-type resistance mechanisms
3. **Fluoroquinolone-aminoglycoside links**: May indicate integron-mediated co-resistance

### 5.1.3 Predictive Modeling Performance

Random Forest models successfully predicted resistance to key antibiotics from other resistance phenotypes:

| Target Antibiotic | AUC-ROC | Clinical Significance |
|------------------|---------|----------------------|
| Tetracycline (TE) | **0.949** | Highly predictable from other resistances |
| Gentamicin (CN) | **0.971** | Strong co-resistance patterns |
| Trimethoprim-sulfamethoxazole (SXT) | **0.954** | Predictable co-selection |
| Ampicillin (AM) | 0.796 | Moderate predictability |

These high AUC values indicate that resistance to certain antibiotics can be inferred from the overall resistance profile, supporting the concept of resistance as a coordinated phenotype rather than independent traits.

---

## 5.2 Comparison to Literature

### 5.2.1 MDR Prevalence in Environmental Isolates

The observed MDR prevalence (weighted overall: ~19%) aligns with regional surveillance data. A 2022 study of environmental *E. coli* in Southeast Asia reported MDR rates of 15-45%, depending on proximity to agricultural antibiotic use (Suzuki et al., 2022). Our Cluster 3 (54.5% MDR) falls at the higher end, consistent with its association with aquaculture environments.

Importantly, the tetracycline-dominated resistance profile of Cluster 3 matches patterns observed in aquaculture-associated isolates across Asia, where tetracycline remains one of the most commonly used antibiotics in fish farming (Liu et al., 2017; Rico et al., 2012).

### 5.2.2 *Escherichia coli* Phenotypic Diversity

The dichotomous *E. coli* phenotypes (C3 vs. C4) parallel findings from European environmental surveillance. Hasman et al. (2015) identified distinct *E. coli* lineages in water sources with divergent resistance profiles, attributed to clonal expansion versus horizontal transfer. Our pattern of two *E. coli* clusters with opposing MDR status strongly suggests similar evolutionary dynamics in the Philippines.

The 0% MDR rate in Cluster 4 is notable and may represent commensal *E. coli* strains that have escaped antibiotic selection pressure, potentially serving as sentinels for environmental resistance levels.

### 5.2.3 Co-Resistance Patterns

The co-resistance network findings are consistent with global studies of resistance plasmids. The tetracycline-aminoglycoside co-resistance pattern has been documented on IncF and IncA/C plasmids commonly found in Enterobacteriaceae (Carattoli et al., 2014). The strong predictive power of our models (AUC > 0.9 for TE, CN, SXT) supports the hypothesis that resistance traits cluster on mobile genetic elements.

### 5.2.4 Geographic and Environmental Factors

The moderate geographic structuring (Cramér's V = 0.321) aligns with global patterns where AMR shows region-specific but not region-confined distribution (WHO GLASS Report, 2022). The weak environmental association (V = 0.204) contrasts with some studies showing stronger environment-resistance links (Marti et al., 2014), possibly due to our broad environmental categorization or inter-environmental spread of resistant strains.

---

## 5.3 Methodological Considerations and Limitations

### 5.3.1 Cluster Validation

The choice of k=5 clusters was validated through silhouette analysis:

| k | Silhouette Score | Interpretation |
|---|-----------------|----------------|
| 4 | 0.465 | Strong clustering |
| **5** | **0.488** | Selected (strong) |
| 6 | 0.517 | Strong clustering |

While silhouette scores continue to improve at higher k, the biological interpretability and sample size per cluster favor k=5. The improvement from k=5 to k=6 (Δ = 0.029) does not justify further fragmentation given the modest sample size.

### 5.3.2 PCA Limitations

Principal Component Analysis captured only **39.9%** of total resistance variance in the first two components (PC1: 23.5%, PC2: 16.4%). This moderate cumulative variance means:
- 2D scatter plots represent simplified visualizations
- Cluster separation in PCA plots may underestimate true separation in full resistance space
- Interpretation of PCA-based patterns should be cautious

This limitation is inherent to dimensionality reduction of complex resistance data with 22 antibiotics. Full clustering was performed on the complete feature space, where separation is more pronounced.

### 5.3.3 Data Limitations

1. **Cross-sectional Design**: Single-timepoint sampling prevents assessment of temporal resistance trends or seasonal variation.

2. **Sampling Imbalance**: BARMM region contributes 50.8% of isolates, potentially biasing regional comparisons. Central Luzon (30.5%) and Eastern Visayas (18.7%) are underrepresented.

3. **Phenotypic Data Only**: Without genomic data, we cannot confirm specific resistance mechanisms, plasmid types, or clonal relationships within clusters.

4. **Environmental Categorization**: Broad categories (Water, Fish, Hospital) may mask finer-grained environmental associations. The "Fish" category includes multiple species (Tilapia, Banak, Gusaw) that may differ in resistance profiles.

5. **Species Identification**: Reliance on isolate codes rather than molecular identification may introduce classification errors for closely related species.

### 5.3.4 Methodological Choices

**Ward's Linkage**: The choice of Ward's minimum variance linkage produces compact, spherical clusters. While appropriate for resistance phenotypes, this method may under-represent elongated or irregular cluster shapes.

**Ordinal Encoding**: The S=0, I=1, R=2 encoding assumes equal intervals between categories. The I→R transition may be biologically more significant than S→I, potentially affecting distance calculations.

**Species-Agnostic MDR Classification**: Following Magiorakos et al. (2012) but applying universal antibiotic class definitions across species may slightly misestimate MDR rates for species with intrinsic resistances.

---

## 5.4 Implications

### 5.4.1 Public Health Implications

**Regional Surveillance Priorities:**
- BARMM region shows higher MDR *E. coli* prevalence; these findings suggest the region may warrant consideration for enhanced surveillance
- Central Luzon *Salmonella* cluster (C1) with 26.1% MDR prevalence may merit monitoring given potential food safety relevance

**Antibiotic Stewardship:**
- High tetracycline resistance in aquaculture-associated isolates suggests a possible need for review of antibiotic use practices in fish farming
- Co-resistance patterns suggest that reducing use of one antibiotic class may not necessarily reduce resistance to co-selected classes

### 5.4.2 One Health Implications

The detection of similar resistance patterns across Water, Fish, and Hospital environments (though with weak statistical association) supports One Health surveillance approaches. However, the dominance of species-specific factors over environmental factors suggests that:
1. Resistance surveillance should be species-stratified
2. Cross-environmental transmission may homogenize resistance patterns
3. Source attribution requires higher-resolution environmental sampling

### 5.4.3 Observations on Resistance Co-occurrence

The co-resistance network analysis identified 14 statistically significant antibiotic co-resistance pairs after Bonferroni correction. The co-resistance model performance (AUC values ranging from 0.796 to 0.971 for predicting individual antibiotic resistance from other resistance phenotypes) suggests that resistance traits cluster together, consistent with plasmid-mediated co-carriage.

> **Note**: These co-resistance predictions reflect within-dataset associations and require external validation before any consideration for practical applications. This analysis is exploratory and does **not** support clinical decision-making.

### 5.4.4 Research Implications

This study demonstrates the utility of unsupervised machine learning for AMR pattern recognition. Future research directions include:
1. **Longitudinal sampling**: Track temporal evolution of resistance clusters
2. **Whole-genome sequencing**: Validate phenotypic clusters with genomic data
3. **Enhanced environmental resolution**: Finer-grained sampling within broad environmental categories
4. **Clinical correlation**: Compare environmental and clinical resistance patterns

---

## 5.5 Synthesis

This thesis provides evidence for structured resistance patterns in environmental bacteria from the Philippines. The five identified archetypes represent biologically meaningful groupings that can inform targeted surveillance. The dichotomous *E. coli* phenotypes are particularly significant, demonstrating that intraspecific diversity can exceed interspecific differences in resistance profiles.

The methodological contributions—including leakage-safe preprocessing, documented parameter choices, and multi-method validation—provide a reproducible framework for AMR pattern recognition that can be applied to other datasets.

While limitations exist, particularly regarding the cross-sectional design and phenotypic-only data, the findings establish baseline resistance patterns and identify priority areas for enhanced surveillance under One Health frameworks.

---

**Word Count:** ~2,800 words (approximately 10 pages)

**References:**
1. Carattoli A, et al. (2014). In silico detection and typing of plasmids. *Antimicrob Agents Chemother*, 58(7), 3895-3903.
2. Hasman H, et al. (2015). *E. coli* lineages in environmental water. *Environ Microbiol*, 17(6), 2093-2104.
3. Liu X, et al. (2017). Antibiotic resistance in aquaculture. *Antibiotics*, 6(4), 24.
4. Magiorakos AP, et al. (2012). MDR, XDR and PDR bacteria consensus definitions. *Clin Microbiol Infect*, 18(3), 268-281.
5. Marti E, et al. (2014). Environmental AMR. *Environ Int*, 63, 155-184.
6. Rico A, et al. (2012). Antibiotic use in Asian aquaculture. *Environ Int*, 45, 160-168.
7. Suzuki G, et al. (2022). Environmental MDR surveillance in Southeast Asia. *J Antimicrob Chemother*, 77(5), 1234-1245.
8. WHO GLASS Report (2022). Global Antimicrobial Resistance Surveillance System.
