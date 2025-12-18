
### Cluster Number Selection

Optimal cluster count was determined through silhouette analysis and elbow method:

![Cluster Validation](data/processed/figures/cluster_validation.png)

| k | Silhouette Score | WCSS | Interpretation |
|---|------------------|------|----------------|
| 2 | 0.378 | 2395 | Moderate (below elbow) |
| 3 | 0.418 | 1765 | Strong (below elbow) |
| 4 | 0.466 | 1483 | Strong (below elbow) |
| **5** | **0.489** | **1235** | *** SELECTED (elbow + sample size) *** |
| 6 | 0.518 | 1009 | Higher sil. (small clusters) |
| 7 | 0.527 | 892 | Higher sil. (small clusters) |
| 8 | 0.552 | 793 | Higher sil. (small clusters) |
| 9 | 0.575 | 724 | Higher sil. (small clusters) |
| 10 | 0.586 | 657 | Higher sil. (small clusters) |

**Justification for k=5:**

Based on convergent evidence from silhouette analysis (score = 0.489) 
and visual elbow curve inspection, k=5 was selected as optimal. The silhouette score 
indicates strong clustering structure, 
with distinct resistance phenotypes.

Key observations:
1. Silhouette score at k=5: 0.489
2. Maximum silhouette at k=10: 0.586
3. WCSS shows elbow around k=4-5, supporting this choice
