# Task 1: Load and Explore the Dataset

import pandas as pd
from sklearn.datasets import load_iris

def load_and_explore():
    # Load the Iris dataset
    iris = load_iris(as_frame=True)
    df = iris.frame

    # Display first few rows
    print("First 5 rows of the dataset:")
    print(df.head(), "\n")

    # Dataset info
    print("Dataset info:")
    print(df.info(), "\n")

    # Missing values
    print("Missing values in dataset:")
    print(df.isnull().sum(), "\n")

    # Clean dataset (drop missing if any)
    df = df.dropna()
    print("Dataset cleaned. Shape:", df.shape)

    return df

if __name__ == "__main__":
    df = load_and_explore()
