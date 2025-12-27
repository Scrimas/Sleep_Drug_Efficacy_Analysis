"""
Sleep Study Analysis Pipeline
Automates the statistical comparison of soporific drugs using paired samples.
Handles normality assumptions dynamically to select between T-test and Wilcoxon.
"""

from pathlib import Path
import pandas as pd
from scipy import stats
from typing import Tuple, Dict

# Constants
ALPHA = 0.05

def load_data(relative_path: str) -> pd.DataFrame:
    """Loads data relative to the current script location using pathlib."""
    base_path = Path(__file__).resolve().parent
    data_path = base_path / relative_path
    
    if not data_path.exists():
        raise FileNotFoundError(f"Dataset not found at: {data_path}")
        
    return pd.read_csv(data_path)

def perform_paired_analysis(df: pd.DataFrame, col1: str, col2: str) -> Dict:
    """
    Evaluates assumptions and runs the appropriate statistical test.
    Returns a dictionary with test metadata and results.
    """
    # 1. Compute differences for paired normality check
    differences = df[col1] - df[col2]
    
    # 2. Shapiro-Wilk Test
    stat_shapiro, p_shapiro = stats.shapiro(differences)
    is_normal = p_shapiro > ALPHA
    
    # 3. Dynamic Test Selection
    if is_normal:
        test_name = "Paired Student's t-test"
        stat, p_val = stats.ttest_rel(df[col1], df[col2])
        assumption_note = f"Normality accepted (Shapiro p={p_shapiro:.4f})"
    else:
        test_name = "Wilcoxon Signed-Rank Test"
        stat, p_val = stats.wilcoxon(df[col1], df[col2])
        assumption_note = f"Normality rejected (Shapiro p={p_shapiro:.4f})"
        
    return {
        "test_used": test_name,
        "statistic": stat,
        "p_value": p_val,
        "assumption_note": assumption_note,
        "significant": p_val < ALPHA
    }

def print_report(results: Dict):
    """Formats the analysis results for the console."""
    print("-" * 40)
    print(f"ANALYSIS REPORT: {results['test_used']}")
    print("-" * 40)
    print(f"Assumption Check: {results['assumption_note']}")
    print(f"Test Statistic:   {results['statistic']:.4f}")
    print(f"P-value:          {results['p_value']:.4f}")
    print("-" * 40)
    
    if results['significant']:
        print(f"CONCLUSION: Significant difference found (p < {ALPHA}).")
        print(">> The drugs have different effects on sleep duration.")
    else:
        print(f"CONCLUSION: No significant difference found (p >= {ALPHA}).")

# --- Main Execution Entry Point ---
if __name__ == "__main__":
    try:
        # Load
        df_sleep = load_data('../data/dataset_somniferes.csv')
        
        # Analyze
        results = perform_paired_analysis(df_sleep, 'hyosciamine', 'hyoscine')
        
        # Report
        print_report(results)
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
