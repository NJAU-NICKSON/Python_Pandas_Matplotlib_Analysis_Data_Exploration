# Task 2: Basic Data Analysis

import pandas as pd
from sklearn.datasets import load_iris

def analyze_data():
    iris = load_iris(as_frame=True)
    df = iris.frame
    df["species"] = df["target"].map({0: "setosa", 1: "versicolor", 2: "virginica"})

    # Descriptive stats
    print("\nDescriptive statistics:")
    print(df.describe(), "\n")

    # Grouping
    print("Average Petal Length by Species:")
    print(df.groupby("species")["petal length (cm)"].mean(), "\n")

    print("Average Petal Width by Species:")
    print(df.groupby("species")["petal width (cm)"].mean(), "\n")

if __name__ == "__main__":
    analyze_data()
