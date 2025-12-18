# MANUSCRIPT: Pattern Recognition of Antibiotic Resistance in *Escherichia coli*, *Salmonella* spp., *Shigella* spp., and *Vibrio cholerae* from the Water–Fish–Human Nexus

## Manuscript for Basic Research

---

## Table of Contents

| Chapter | Title | File |
|---------|-------|------|
| **1** | [Introduction](CHAPTER_01_INTRODUCTION.md) | Background, Problem Statement, Objectives, Significance, Scope |
| **2** | [Review of Related Literature](CHAPTER_02_LITERATURE_REVIEW.md) | Related Concepts, Related Studies |
| **3** | [Theoretical Framework](CHAPTER_03_THEORETICAL_FRAMEWORK.md) | One Health, Ecological Theory, Pattern Recognition Theory |
| **4** | [Methodology](CHAPTER_04_METHODOLOGY.md) | Research Design, Data Collection, Analytical Methods |
| **5** | [Architectural Design](CHAPTER_05_ARCHITECTURAL_DESIGN.md) | System Architecture, Data Flow, Technology Stack |
| **6** | [Results and Discussion](CHAPTER_06_RESULTS_AND_DISCUSSION.md) | Findings, Statistical Analysis, Interpretation |
| **7** | [Conclusion](CHAPTER_07_CONCLUSION.md) | Summary, Key Findings, Implications |
| **8** | [Recommendations](CHAPTER_08_RECOMMENDATIONS.md) | Future Research, Surveillance, Policy |

---

## Abstract

**Background:** Antimicrobial resistance (AMR) represents a critical global health challenge, with the Water–Fish–Human nexus serving as a significant transmission pathway. Limited surveillance data exists for environmental AMR patterns in the Philippines.

**Objective:** To develop and apply a comprehensive pattern recognition pipeline for characterizing AMR patterns in bacterial isolates from water, fish, and hospital-associated samples across three Philippine regions.

**Methods:** A cross-sectional analytical study was conducted on 491 bacterial isolates (6 species) from BARMM, Central Luzon, and Eastern Visayas. Hierarchical agglomerative clustering (Ward's method), supervised classification, chi-square tests, and principal component analysis were applied to antimicrobial susceptibility testing data across 21 antibiotics.

**Results:** Five distinct resistance archetypes were identified with silhouette score 0.488. *Escherichia coli* exhibited striking phenotypic heterogeneity, with two clusters showing 54.5% vs. 0.0% MDR prevalence despite similar geographic and environmental distributions. Species identity (Cramér's V = 0.765) was the dominant factor driving cluster membership, exceeding geographic (V = 0.321) and environmental (V = 0.204) factors. The tetracycline-dominated MDR signature (TE, DO, SXT, AM) suggests aquaculture-associated selection pressures.

**Conclusion:** Environmental AMR in the Philippines is structured, species-driven, and amenable to systematic pattern recognition. The identified archetypes provide baseline references for One Health surveillance, and the dichotomous *E. coli* phenotypes reveal intraspecific heterogeneity that aggregate reporting would obscure.

**Keywords:** Antimicrobial resistance, pattern recognition, machine learning, One Health, *Escherichia coli*, Philippines, aquaculture, environmental surveillance

---

## Key Findings Summary

| Finding | Evidence | Significance |
|---------|----------|--------------|
| *E. coli* phenotypic heterogeneity | Cluster 3 (54.5% MDR) vs. Cluster 4 (0.0% MDR) | Intraspecific diversity exceeds interspecific differences |
| Species-driven clustering | Cramér's V = 0.765 | Species identity dominates over environment |
| Geographic structuring | χ² = 101.18, p < 10⁻¹⁸ | Regional resistance specificity exists |
| Tetracycline-MDR signature | TE-DO-SXT-AM co-resistance | Mobile element-mediated resistance |
| Five resistance archetypes | Silhouette = 0.488 | Biologically interpretable pattern structure |

---

## Authors and Affiliations

*(To be completed)*

---

## Acknowledgments

*(To be completed)*

---

## Data Availability

The processed datasets and analytical code are available in this repository:
- **Processed Data:** `data/processed/`
- **Source Code:** `src/`
- **Documentation:** `docs/`

---

## Citation

*(To be completed upon publication)*

---

## Document Information

| Attribute | Value |
|-----------|-------|
| **Document Type** | Manuscript for Basic Research |
| **Status** | Draft |
| **Generated** | December 2025 |
| **Word Count** | ~25,000 words (estimated) |

---

## Related Documentation

| Document | Description | Location |
|----------|-------------|----------|
| Methodology | Comprehensive analytical methodology | `docs/methodology.md` |
| Architecture | System design documentation | `docs/architecture.md` |
| Results Templates | Detailed results with actual values | `docs/results/` |
| Limitations | Explicit scope boundaries | `docs/limitations.md` |
| Discussion | Extended discussion content | `docs/discussion.md` |
| Conclusion | Extended conclusion content | `docs/conclusion.md` |

---

*This manuscript is part of the AMR Thesis Project: Antimicrobial Resistance Pattern Recognition and Surveillance Pipeline.*
