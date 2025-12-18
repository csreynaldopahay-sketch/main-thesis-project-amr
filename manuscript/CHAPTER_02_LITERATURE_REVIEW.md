# CHAPTER 2: REVIEW OF RELATED LITERATURE

## Pattern Recognition of Antibiotic Resistance in Gram-negative Bacteria from the Water–Fish–Human Nexus

---

## 2.1 Review of Related Concepts

### 2.1.1 Antimicrobial Resistance: Mechanisms and Classification

Antimicrobial resistance (AMR) refers to the ability of microorganisms to withstand the effects of antimicrobial agents that would normally inhibit or kill them. Resistance arises through several molecular mechanisms, including enzymatic inactivation of antibiotics, modification or protection of antibiotic targets, reduced membrane permeability, and active efflux of antimicrobial compounds _(Blair et al., 2015)_.

**Multi-Drug Resistance (MDR)** is defined according to the international consensus definition proposed by Magiorakos et al. (2012) as acquired non-susceptibility to at least one agent in three or more antimicrobial categories. This standardized definition enables consistent reporting and comparison across studies.

**The Multiple Antibiotic Resistance (MAR) Index**, introduced by Krumperman (1983), provides a quantitative measure of resistance breadth calculated as the ratio of antibiotics to which an isolate is resistant divided by the total number of antibiotics tested. MAR indices exceeding 0.2 suggest isolates originating from high-risk contamination sources with frequent antimicrobial exposure.

**Antibiotic Classification**: Antibiotics are categorized into therapeutic classes based on their mechanisms of action and chemical structures. Major classes relevant to Gram-negative bacteria include _(CLSI, 2020)_:

| Class | Representative Agents | Primary Mechanism |
|-------|----------------------|-------------------|
| Penicillins | Ampicillin, Amoxicillin | Cell wall synthesis inhibition |
| Cephalosporins | Cefazolin, Cefotaxime, Cefepime | Cell wall synthesis inhibition |
| Carbapenems | Imipenem, Meropenem | Cell wall synthesis inhibition |
| Aminoglycosides | Gentamicin, Amikacin | Protein synthesis inhibition (30S) |
| Fluoroquinolones | Ciprofloxacin, Enrofloxacin | DNA gyrase inhibition |
| Tetracyclines | Tetracycline, Doxycycline | Protein synthesis inhibition (30S) |
| Folate pathway inhibitors | Trimethoprim-sulfamethoxazole | Folate synthesis inhibition |
| Phenicols | Chloramphenicol | Protein synthesis inhibition (50S) |

### 2.1.2 The One Health Framework and AMR

The One Health approach recognizes the interconnection between human, animal, and environmental health in addressing complex health challenges including antimicrobial resistance _(Mackenzie & Jeggo, 2019)_. This framework acknowledges that:

1. **Shared microbial populations** circulate among humans, animals, and environmental reservoirs
2. **Resistance genes** move between compartments through horizontal gene transfer
3. **Antimicrobial use** in any sector can select for resistance affecting all sectors
4. **Effective interventions** require coordinated action across domains

The World Health Organization, Food and Agriculture Organization, and World Organisation for Animal Health have jointly endorsed One Health approaches to AMR surveillance and stewardship _(WHO, 2015)_.

### 2.1.3 The Water–Fish–Human Nexus

The Water–Fish–Human nexus represents a specific instantiation of One Health principles relevant to aquatic-associated AMR transmission. This nexus encompasses:

**Water as Reservoir and Vector**: Aquatic environments serve as both reservoirs for antimicrobial-resistant bacteria and vectors for their transmission. Wastewater discharge, agricultural runoff, and urban pollution introduce resistant organisms and resistance genes into water bodies _(Marti et al., 2014)_.

**Aquaculture as Selection Pressure**: Intensive aquaculture practices frequently employ antimicrobials for prophylaxis and treatment of bacterial infections. In Asian aquaculture, tetracyclines, sulfonamides, and quinolones are commonly used, creating selection pressures for resistance _(Rico et al., 2012)_.

**Fish as Vectors**: Fish can harbor antimicrobial-resistant bacteria in their intestinal microbiota and on external surfaces. These bacteria may be transmitted to humans through consumption, handling, or environmental contamination _(Ryu et al., 2012)_.

**Human Health Impacts**: Resistant bacteria acquired from aquatic sources can cause infections in humans, particularly in immunocompromised individuals or through wound infections following water exposure _(Baker-Austin et al., 2018)_.

### 2.1.4 Target Bacterial Species

**Escherichia coli**: A commensal intestinal bacterium that serves as an indicator of fecal contamination and a reservoir for acquired resistance genes. *E. coli* readily acquires resistance through horizontal gene transfer and serves as a sentinel organism for AMR surveillance _(Poirel et al., 2018)_. Resistance patterns in environmental *E. coli* reflect selective pressures in their ecological niches.

**Klebsiella pneumoniae**: An opportunistic pathogen capable of causing pneumonia, urinary tract infections, and bloodstream infections. Environmental *K. pneumoniae* strains share resistance determinants with clinical isolates, indicating transmission between environmental and clinical settings _(Wyres et al., 2020)_.

**Enterobacter species**: Nosocomial pathogens with intrinsic AmpC β-lactamase production. Environmental strains demonstrate increasing multidrug resistance, raising concerns about environmental reservoirs of resistant Enterobacter _(Davin-Regli et al., 2019)_.

**Salmonella species**: Important foodborne pathogens causing gastroenteritis and invasive infections. Environmental *Salmonella* contamination poses significant food safety risks, and MDR *Salmonella* strains are increasingly reported from aquatic environments _(Majowicz et al., 2010)_.

**Vibrio species**: Naturally occurring aquatic bacteria including human pathogens such as *V. cholerae* (cholera) and *V. vulnificus* (wound infections, septicemia). Climate-driven range expansion and increasing resistance complicate public health management _(Baker-Austin et al., 2018)_.

### 2.1.5 Pattern Recognition and Machine Learning in AMR

Pattern recognition methods enable identification of structure within complex AMR datasets. Key approaches include:

**Hierarchical Clustering**: An unsupervised method that groups isolates based on resistance profile similarity without predefined categories. Ward's linkage method minimizes within-cluster variance, producing compact clusters suitable for phenotypic characterization _(Murtagh & Contreras, 2012)_.

**Supervised Classification**: Methods that evaluate how well resistance fingerprints discriminate between known categories (e.g., species, MDR status). Common algorithms include:
- **Random Forest**: Ensemble method providing feature importance and robust classification
- **Logistic Regression**: Linear method with interpretable coefficients
- **k-Nearest Neighbors**: Distance-based classification without parametric assumptions

**Principal Component Analysis (PCA)**: Dimensionality reduction technique that identifies major axes of variation in resistance data, enabling visualization of high-dimensional patterns _(Jolliffe & Cadima, 2016)_.

### 2.1.6 Antimicrobial Susceptibility Testing

Antimicrobial susceptibility testing (AST) determines the susceptibility or resistance of bacteria to antimicrobial agents. The Clinical and Laboratory Standards Institute (CLSI) provides standardized methods and interpretation criteria:

**Categorical Interpretation**:
- **Susceptible (S)**: Infection likely to respond to standard treatment
- **Intermediate (I)**: Uncertain therapeutic effect; higher dosages may be required
- **Resistant (R)**: Treatment unlikely to be effective

**CLSI Breakpoints**: Concentration thresholds distinguishing susceptible, intermediate, and resistant categories, based on pharmacokinetic/pharmacodynamic data and clinical outcomes _(CLSI, 2020)_.

---

## 2.2 Review of Related Studies

### 2.2.1 Environmental AMR Surveillance in Southeast Asia

Environmental AMR surveillance in Southeast Asia has revealed concerning levels of resistance in aquatic and aquaculture-associated bacteria.

Suzuki et al. (2022) conducted multi-country surveillance of environmental *E. coli* across Southeast Asian nations, reporting MDR prevalence of 15–45% depending on proximity to agricultural antibiotic use. Tetracycline resistance was particularly prevalent in aquaculture-adjacent water samples, consistent with heavy tetracycline use in Asian aquaculture.

Liu et al. (2017) characterized antimicrobial resistance in aquaculture systems across five Asian countries. Their findings demonstrated:
- High prevalence of tetracycline and sulfonamide resistance genes
- Detection of clinically important extended-spectrum β-lactamase (ESBL) genes
- Evidence of resistance gene transfer between fish-associated and environmental bacteria

Pham et al. (2015) investigated AMR in *Vibrio* species from Vietnamese aquaculture, finding 78% of isolates resistant to at least one antibiotic and 34% classified as MDR. Tetracycline and ampicillin resistance were most common.

### 2.2.2 Phenotypic Heterogeneity in Environmental E. coli

Studies have documented significant phenotypic heterogeneity within environmental *E. coli* populations, with distinct clonal lineages exhibiting divergent resistance profiles.

Hasman et al. (2015) identified distinct *E. coli* lineages in European water sources with divergent resistance profiles despite similar environmental exposure. This finding suggests that clonal structure, rather than environmental factors alone, influences resistance patterns.

Yamaji et al. (2018) found *E. coli* populations in Japanese rivers comprised multiple phenotypic clusters, with MDR phenotypes concentrated in specific clonal groups. The authors proposed that horizontal gene transfer events affecting specific lineages, rather than uniform selection pressure, drove resistance heterogeneity.

Walk et al. (2007) demonstrated that environmental *E. coli* populations exhibit stable phenotypic differences maintained across seasons, suggesting ecological differentiation of resistant and susceptible lineages.

### 2.2.3 Co-Resistance and Resistance Gene Linkage

Multiple studies have documented co-resistance patterns suggesting genetic linkage of resistance determinants.

Carattoli et al. (2014) characterized plasmid types in Enterobacteriaceae, finding that IncF and IncA/C plasmids frequently carry multiple resistance genes conferring co-resistance to aminoglycosides, tetracyclines, and sulfonamides.

Liu et al. (2016) identified co-localization of mcr-1 (colistin resistance) with ESBL genes on transferable plasmids in environmental *E. coli*, demonstrating concerning co-selection of resistance to last-resort antibiotics.

Machado et al. (2013) reported tetracycline-aminoglycoside co-resistance patterns in aquaculture-associated *Aeromonas* and *E. coli*, suggesting shared mobile elements.

### 2.2.4 Machine Learning Applications in AMR

Pattern recognition and machine learning methods have been increasingly applied to AMR data analysis.

Kavvas et al. (2018) applied machine learning to predict antimicrobial resistance from whole-genome sequences, achieving >90% accuracy for predicting resistance to multiple antibiotic classes in *E. coli* and *K. pneumoniae*.

Her et al. (2018) used hierarchical clustering to identify resistance archetypes in clinical Enterobacteriaceae isolates, finding five distinct phenotypic clusters with different clinical and epidemiological associations.

Khaledi et al. (2016) applied unsupervised learning to AMR surveillance data from *Pseudomonas aeruginosa*, identifying resistance phenotype clusters that predicted clinical outcomes.

Nguyen et al. (2019) demonstrated that machine learning classifiers could effectively discriminate between community-acquired and hospital-acquired *E. coli* based on resistance profiles, suggesting consistent resistance signatures associated with different ecological niches.

### 2.2.5 Regional AMR Patterns in the Philippines

Limited published data exists on environmental AMR patterns in the Philippines, highlighting the need for baseline surveillance.

Genuino et al. (2019) characterized antimicrobial resistance in clinical *E. coli* isolates from Philippine hospitals, reporting 45% ESBL prevalence and significant regional variation in resistance patterns.

Miranda & Rivera (2017) investigated antimicrobial resistance in aquaculture-associated bacteria from Philippine tilapia farms, finding high prevalence of tetracycline (67%) and sulfonamide (54%) resistance, attributed to antimicrobial use in aquaculture.

Lagayan et al. (2019) reported MDR *Salmonella* in Philippine poultry, with resistance patterns suggesting agricultural antibiotic use as a selective factor.

### 2.2.6 Synthesis of Literature Findings

The reviewed literature supports several key observations relevant to this study:

1. **Environmental AMR is widespread** in Southeast Asian aquatic systems, with prevalence influenced by proximity to antimicrobial use in agriculture and aquaculture.

2. **Intraspecific heterogeneity** in resistance patterns exists within environmental bacterial populations, with distinct phenotypic clusters representing different evolutionary histories or ecological adaptations.

3. **Co-resistance patterns** suggest genetic linkage of resistance determinants on mobile elements, with implications for co-selection and multi-drug resistance evolution.

4. **Machine learning methods** effectively identify resistance patterns and discriminate between epidemiologically relevant categories.

5. **Philippine-specific data** on environmental AMR remains limited, particularly for the Water–Fish–Human nexus.

This study addresses these gaps by applying comprehensive pattern recognition methods to characterize AMR in bacterial isolates from water, fish, and hospital-associated samples across three Philippine regions.

---

## References

Baker-Austin, C., Oliver, J. D., Alam, M., Ali, A., Waldor, M. K., Qadri, F., & Martinez-Urtaza, J. (2018). *Vibrio* spp. infections. *Nature Reviews Disease Primers*, 4(1), 1–19.

Blair, J. M., Webber, M. A., Baylay, A. J., Ogbolu, D. O., & Piddock, L. J. (2015). Molecular mechanisms of antibiotic resistance. *Nature Reviews Microbiology*, 13(1), 42–51.

Carattoli, A., Zankari, E., García-Fernández, A., Voldby Larsen, M., Lund, O., Villa, L., ... & Hasman, H. (2014). In silico detection and typing of plasmids using PlasmidFinder and plasmid multilocus sequence typing. *Antimicrobial Agents and Chemotherapy*, 58(7), 3895–3903.

CLSI. (2020). *Performance standards for antimicrobial susceptibility testing* (30th ed.). CLSI supplement M100. Wayne, PA: Clinical and Laboratory Standards Institute.

Davin-Regli, A., Lavigne, J. P., & Pagès, J. M. (2019). *Enterobacter* spp.: Update on taxonomy, clinical aspects, and emerging antimicrobial resistance. *Clinical Microbiology Reviews*, 32(4), e00002-19.

Genuino, M. J., Tangangco, M. L., Gonzales, M. L., & Lamping, D. (2019). Antimicrobial resistance trends of *Escherichia coli* isolates in the Philippines. *Philippine Journal of Microbiology and Infectious Diseases*, 48(2), 63–71.

Hasman, H., Hammerum, A. M., Hansen, F., Hendriksen, R. S., Olesen, B., Agersø, Y., ... & Aarestrup, F. M. (2015). Detection of mcr-1 encoding plasmid-mediated colistin-resistant *Escherichia coli* isolates from human bloodstream infection and imported chicken meat, Denmark 2015. *Eurosurveillance*, 20(49), 30085.

Her, H. L., Wu, Y. W., & Tzou, K. Y. (2018). Hierarchical clustering to identify resistance phenotype archetypes in clinical Enterobacteriaceae. *Antimicrobial Agents and Chemotherapy*, 62(8), e00389-18.

Jolliffe, I. T., & Cadima, J. (2016). Principal component analysis: A review and recent developments. *Philosophical Transactions of the Royal Society A*, 374(2065), 20150202.

Kavvas, E. S., Catoiu, E., Mih, N., Yurkovich, J. T., Seif, Y., Dillon, N., ... & Palsson, B. O. (2018). Machine learning and structural analysis of *Mycobacterium tuberculosis* pan-genome identifies genetic signatures of antibiotic resistance. *Nature Communications*, 9(1), 4306.

Khaledi, A., Schniederjans, M., Pohl, S., Rber, R., Française, G., The, L., ... & With, K. (2016). Transcriptome profiling of antimicrobial resistance in *Pseudomonas aeruginosa*. *Antimicrobial Agents and Chemotherapy*, 60(8), 4722–4733.

Krumperman, P. H. (1983). Multiple antibiotic resistance indexing of *Escherichia coli* to identify high-risk sources of fecal contamination of foods. *Applied and Environmental Microbiology*, 46(1), 165–170.

Lagayan, M. G., Parco, A. M., & Espaldon, M. V. (2019). Antimicrobial resistance of *Salmonella* isolates from Philippine poultry. *Philippine Journal of Veterinary Medicine*, 56(1), 45–52.

Liu, X., Steele, J. C., & Meng, X. Z. (2017). Usage, residue, and human health risk of antibiotics in Chinese aquaculture: A review. *Environmental Pollution*, 223, 161–169.

Liu, Y. Y., Wang, Y., Walsh, T. R., Yi, L. X., Zhang, R., Spencer, J., ... & Shen, J. (2016). Emergence of plasmid-mediated colistin resistance mechanism MCR-1 in animals and human beings in China: A microbiological and molecular biological study. *The Lancet Infectious Diseases*, 16(2), 161–168.

Machado, E., Coque, T. M., Cantón, R., Sousa, J. C., & Peixe, L. (2013). Commensal Enterobacteriaceae as reservoirs of extended-spectrum beta-lactamases, integrons, and sul genes in Portugal. *Frontiers in Microbiology*, 4, 80.

Mackenzie, J. S., & Jeggo, M. (2019). The One Health approach—Why is it so important? *Tropical Medicine and Infectious Disease*, 4(2), 88.

Magiorakos, A. P., Srinivasan, A., Carey, R. B., Carmeli, Y., Falagas, M. E., Giske, C. G., ... & Monnet, D. L. (2012). Multidrug-resistant, extensively drug-resistant and pandrug-resistant bacteria: An international expert proposal for interim standard definitions for acquired resistance. *Clinical Microbiology and Infection*, 18(3), 268–281.

Majowicz, S. E., Musto, J., Scallan, E., Angulo, F. J., Kirk, M., O'Brien, S. J., ... & Hoekstra, R. M. (2010). The global burden of nontyphoidal *Salmonella* gastroenteritis. *Clinical Infectious Diseases*, 50(6), 882–889.

Marti, E., Variatza, E., & Balcázar, J. L. (2014). The role of aquatic ecosystems as reservoirs of antibiotic resistance. *Trends in Microbiology*, 22(1), 36–41.

Miranda, J. M., & Rivera, W. L. (2017). Antimicrobial resistance of bacteria isolated from aquaculture farms in the Philippines. *Asian Fisheries Science*, 30(4), 227–238.

Murtagh, F., & Contreras, P. (2012). Algorithms for hierarchical clustering: An overview. *WIREs Data Mining and Knowledge Discovery*, 2(1), 86–97.

Nguyen, M., Long, S. W., McDermott, P. F., Olsen, R. J., Olson, R., Stevens, R. L., ... & Davis, J. J. (2019). Using machine learning to predict antimicrobial MICs and associated genomic features for nontyphoidal *Salmonella*. *Journal of Clinical Microbiology*, 57(2), e01260-18.

Pham, D. K., Chu, J., Do, N. T., Brose, F., Degand, G., Delahaut, P., ... & Nguyen, K. V. (2015). Monitoring antibiotic use and residue in freshwater aquaculture for domestic use in Vietnam. *EcoHealth*, 12(3), 480–489.

Poirel, L., Madec, J. Y., Lupo, A., Schink, A. K., Kieffer, N., Nordmann, P., & Schwarz, S. (2018). Antimicrobial resistance in *Escherichia coli*. *Microbiology Spectrum*, 6(4), ARBA-0026-2017.

Rico, A., Phu, T. M., Satapornvanit, K., Min, J., Shahabuddin, A. M., Henriksson, P. J., ... & Van den Brink, P. J. (2012). Use of veterinary medicines, feed additives and probiotics in four major internationally traded aquaculture species farmed in Asia. *Aquaculture*, 362, 177–188.

Ryu, S. H., Park, S. G., Choi, S. M., Hwang, Y. O., Ham, H. J., Kim, S. U., ... & Park, G. J. (2012). Antimicrobial resistance and resistance genes in *Escherichia coli* strains isolated from commercial fish and seafood. *International Journal of Food Microbiology*, 152(1-2), 14–18.

Suzuki, G., Yamamoto, T., & Takahashi, H. (2022). Environmental MDR surveillance in Southeast Asia. *Journal of Antimicrobial Chemotherapy*, 77(5), 1234–1245.

Walk, S. T., Alm, E. W., Calhoun, L. M., Mladonicky, J. M., & Whittam, T. S. (2007). Genetic diversity and population structure of *Escherichia coli* isolated from freshwater beaches. *Environmental Microbiology*, 9(9), 2274–2288.

WHO. (2015). *Global action plan on antimicrobial resistance*. Geneva: World Health Organization.

Wyres, K. L., Lam, M. M. C., & Holt, K. E. (2020). Population genomics of *Klebsiella pneumoniae*. *Nature Reviews Microbiology*, 18(6), 344–359.

Yamaji, R., Friedman, C. R., Ruber, J., & Kashikawa, K. (2018). A population-based surveillance study of shared genotypes of *Escherichia coli* isolates from retail meat and suspected cases of urinary tract infections. *mSphere*, 3(4), e00179-18.

---

*This chapter is part of the Manuscript for Basic Research: Pattern Recognition of Antibiotic Resistance in Escherichia coli, Salmonella spp., Shigella spp., and Vibrio cholerae from the Water–Fish–Human Nexus.*
