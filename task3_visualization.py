import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import os

# Ensure images folder exists
os.makedirs("images", exist_ok=True)

# Load iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = pd.Categorical.from_codes(iris.target, iris.target_names)

# 1. Line Chart – Sepal Length Trend
df_sorted = df.sort_values("sepal length (cm)")
plt.figure(figsize=(8, 5))
plt.plot(df_sorted.index, df_sorted["sepal length (cm)"], label="Sepal Length Trend")
plt.title("Line Chart: Sepal Length Trend")
plt.xlabel("Index (sorted by sepal length)")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.savefig("images/line_chart.png")
plt.show()

# 2. Bar Chart – Average Petal Length by Species
avg_petal_length = df.groupby("species")["petal length (cm)"].mean()
plt.figure(figsize=(8, 5))
avg_petal_length.plot(kind="bar", color="skyblue")
plt.title("Bar Chart: Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.savefig("images/bar_chart.png")
plt.show()

# 3. Histogram – Sepal Width Distribution
plt.figure(figsize=(8, 5))
plt.hist(df["sepal width (cm)"], bins=15, color="green", edgecolor="black")
plt.title("Histogram: Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.savefig("images/histogram.png")
plt.show()

# 4. Scatter Plot – Sepal Length vs Petal Length by Species
colors = {"setosa": "red", "versicolor": "blue", "virginica": "purple"}
plt.figure(figsize=(8, 5))
for species, group in df.groupby("species"):
    plt.scatter(
        group["sepal length (cm)"],
        group["petal length (cm)"],
        label=species,
        color=colors[species]
    )
plt.title("Scatter Plot: Sepal Length vs. Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.savefig("images/scatter_plot.png")
plt.show()
