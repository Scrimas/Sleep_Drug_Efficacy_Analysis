import pandas as pd
from scipy import stats
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, '..', 'data', 'dataset_somniferes.csv')

df = pd.read_csv(file_path)

print("--- DATA PREVIEW ---")
print(df)
print("-" * 30)

df['difference'] = df['hyoscine'] - df['hyosciamine']

print("\n--- SHAPIRO-WILK TEST (NORMALITY) ---")
shapiro_stat, shapiro_p = stats.shapiro(df['difference'])

print(f"Statistic: {shapiro_stat:.5f}")
print(f"P-value:   {shapiro_p:.5f}")

if shapiro_p < 0.05:
    print("Result: Distribution is NOT normal (p < 0.05).")
else:
    print("Result: Distribution is normal.")

print("\n--- WILCOXON SIGNED-RANK TEST ---")
wilcox_stat, wilcox_p = stats.wilcoxon(df['hyosciamine'], df['hyoscine'])

print(f"Statistic: {wilcox_stat}")
print(f"P-value:   {wilcox_p:.5f}")

if wilcox_p < 0.05:
    print("CONCLUSION: Significant difference detected between the two drugs.")
else:
    print("CONCLUSION: No significant difference detected.")
