# Analysis of Soporific Drugs
# Context: Bio-statistics L3 - Paired data study (n=10)
# Goal: Compare sleep duration extension between Hyoscyamine and Hyoscine

# 1. Setup
data <- read.csv("../data/dataset_somniferes.csv")

# 2. Assumption Check (Normality)
# Since data is paired, we check normality on the differences
differences <- data$hyoscine - data$hyosciamine

shapiro_result <- shapiro.test(differences)
print(shapiro_result)

# Shapiro p-value is ~0.033 (< 0.05). 
# Normality is rejected. We cannot use Student's t-test.
# -> Switching to Non-Parametric approach using Wilcoxon.

# 3. Statistical Test (Wilcoxon Signed-Rank)
# Paired = TRUE is mandatory here (same patients)
test_result <- wilcox.test(data$hyosciamine, 
                           data$hyoscine, 
                           paired = TRUE)

print(test_result)
