import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats

# Optional: show active Python executable (handy for debugging envs)
import sys
print("Python:", sys.executable)
print("Environment ready")

pd.set_option("display.max_columns", 100)
pd.set_option("display.width", 200)

sns.set_theme(style="whitegrid")

# Load dataset
df = pd.read_csv("../data/irrigation_prediction.csv")

# Basic inspection
print("Shape:", df.shape)
df.info()

# Checking for duplicate rows
duplicate_rows = df.duplicated().sum()
print("Number of duplicate rows:", duplicate_rows)

# Checking for missing values
missing = df.isna().sum().sort_values(ascending=False)
missing = missing[missing > 0]
missing

# Separate Numeric vs Categorical Columns
target_col = "Irrigation_Need"

numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
categorical_cols = df.select_dtypes(include=["string"]).columns.tolist()

if target_col in categorical_cols:
    categorical_cols.remove(target_col)

print("Target:", target_col)
print("Numeric cols:", numeric_cols)
print("Categorical cols:", categorical_cols)
