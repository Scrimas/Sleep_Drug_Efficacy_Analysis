# Sleep_Drug_Efficacy_Analysis

# Comparative Analysis of the Effectiveness of Sleeping Pills

This repository contains the statistical analysis of a clinical study comparing the effect of two molecules (**Hyoscyamine** and **Hyoscine**) on sleep duration in 10 patients.

This project was initially carried out as part of my **Bachelor's degree in Biology (Grenoble Alpes University)** using R, then reproduced in Python to develop my data science skills.

## Project structure

* `data/`: Contains the raw data set (`.csv`).
* `r_analysis/`: Original analysis script (academic methodology).
* `python_reproduction/`: Counter-expertise and automation performed in Python (Pandas/Scipy).

## Statistical Methodology

The study focuses on **paired data** (each patient tested both drugs).

1.  **Verification of Normality**: The Shapiro-Wilk test on the differences revealed non-normality ($p < 0.05$).
2.  **Choice of Test**: Rejection of the parametric test (Student's t-test) in favor of the **Wilcoxon test for paired data**.
3.  **Risk threshold**: $\alpha = 0.05$.

## Main Results

* **Shapiro-Wilk test**: $p = 0.033$ (non-normal distribution).
* **Wilcoxon test**: $p = 0.009$ ($p < 0.05$).

**Biological conclusion:**
The analysis highlights a statistically significant difference. Hyoscine causes a greater increase in sleep time than hyoscyamine.

## Tools Used

* **R**: `shapiro.test`, `wilcox.test`
* **Python**: `pandas` (data management), `scipy.stats` (statistical tests)

---

*Author: Ismaël PHILIPPE - Biology Student*
