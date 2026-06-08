import pandas as pd

# Dataset Load
df = pd.read_csv("netflix_titles.csv")

# Basic Info
print("Shape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nMovies vs TV Shows:")
print(df['type'].value_counts())

print("\nTop 10 Countries:")
print(df['country'].value_counts().head(10))
