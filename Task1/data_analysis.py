import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 1. Load Dataset
# -----------------------------
df = pd.read_csv("All_Diets.csv")

# Standardize column names (safe practice)
df.columns = df.columns.str.strip()

# -----------------------------
# 2. Data Cleaning
# -----------------------------
# Convert macronutrient columns to numeric (handles bad strings)
macros = ['Protein(g)', 'Carbs(g)', 'Fat(g)']
for col in macros:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Fill missing values with column mean
df[macros] = df[macros].fillna(df[macros].mean())

# Normalize Diet_type text (case consistency)
df['Diet_type'] = df['Diet_type'].str.title()

# -----------------------------
# 3. Average Macronutrients by Diet Type
# -----------------------------
avg_macros = df.groupby('Diet_type')[macros].mean()
print("\nAverage Macronutrients by Diet Type:\n")
print(avg_macros)

# -----------------------------
# 4. Top 5 Protein-Rich Recipes per Diet
# -----------------------------
top_protein = (
    df.sort_values('Protein(g)', ascending=False)
      .groupby('Diet_type')
      .head(5)
)

pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)
pd.set_option('display.max_columns', None)
print("\nTop 5 Protein-Rich Recipes per Diet Type:\n")
print(top_protein[['Diet_type', 'Recipe_name', 'Protein(g)']])

# -----------------------------
# 5. Diet Type with Highest Protein Content
# -----------------------------
highest_protein_diet = avg_macros['Protein(g)'].idxmax()
print(f"\nDiet type with highest average protein: {highest_protein_diet}")

# -----------------------------
# 6. Most Common Cuisine per Diet Type
# -----------------------------
common_cuisines = (
    df.groupby('Diet_type')['Cuisine_type']
      .agg(lambda x: x.value_counts().idxmax())
)

print("\nMost Common Cuisine for Each Diet Type:\n")
for diet, cuisine in common_cuisines.items():
    print(f"{diet:<15} : {cuisine}")

# -----------------------------
# 7. New Metrics
# -----------------------------
df['Protein_to_Carbs_ratio'] = df['Protein(g)'] / df['Carbs(g)']
df['Carbs_to_Fat_ratio'] = df['Carbs(g)'] / df['Fat(g)']

# -----------------------------
# 8. Visualizations
# -----------------------------
sns.set(style="whitegrid")

# --- Bar Chart: Average Macronutrients ---
avg_macros.plot(kind='bar', figsize=(12, 6))
plt.title("Average Macronutrient Content by Diet Type")
plt.ylabel("Grams")
plt.xlabel("Diet Type")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("bar_chart.png")

# --- Heatmap: Macronutrients vs Diet Types ---
plt.figure(figsize=(10, 6))
sns.heatmap(avg_macros, annot=True, cmap="YlGnBu", fmt=".1f")
plt.title("Heatmap of Macronutrients by Diet Type")
plt.tight_layout()
plt.savefig("heatmap.png")

# --- Scatter Plot: Top Protein Recipes ---
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=top_protein,
    x='Protein(g)',
    y='Carbs(g)',
    hue='Cuisine_type',
    size='Fat(g)',
    sizes=(40, 300),
    alpha=0.7
)
plt.title("Top 5 Protein-Rich Recipes Across Diet Types")
plt.xlabel("Protein (g)")
plt.ylabel("Carbs (g)")
plt.tight_layout()
plt.savefig("scatter_plot.png")