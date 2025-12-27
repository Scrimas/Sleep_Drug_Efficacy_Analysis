# Analysis of Soporific Drugs
# Context: Bio-statistics L3 - Paired data study (n=10)
# Goal: Compare sleep duration extension between Hyoscyamine and Hyoscine

# 1. Setup & Data Loading
data <- read.csv("../data/dataset_somniferes.csv")

# 2. Assumption Check (Normality)
# Since data is paired, we check normality on the differences
differences <- data$hyoscine - data$hyosciamine

shapiro_result <- shapiro.test(differences)
print(shapiro_result)

# DECISION STEP:
# Shapiro-Wilk p-value is ~0.033 (< Alpha = 0.05). 
# Normality assumption is rejected. We cannot use the paired Student's t-test.
# -> Proceeding with the Non-Parametric alternative (Wilcoxon).

# 3. Statistical Test (Wilcoxon Signed-Rank)
# Paired = TRUE is mandatory here (same patients tested both drugs)
test_result <- wilcox.test(data$hyosciamine, 
                           data$hyoscine, 
                           paired = TRUE)

print(test_result)

# 4. Final Conclusion (Alpha = 0.05)
# Result: p-value = 0.009091
# Decision: p-value < 0.05 -> We reject the Null Hypothesis (H0).
# Interpretation: There is a statistically significant difference between the two drugs.
# (Hyoscine appears more effective in extending sleep duration).
