import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
from pyodbc import connect

# Load datasets
movies_df = pd.read_csv('tmdb_5000_movies.csv')
credits_df = pd.read_csv('tmdb_5000_credits.csv')

# Inspect the first few rows of the datasets
print(movies_df.head())
print(credits_df.head())

# Check for missing values
print("Missing values in movies_df:\n", movies_df.isnull().sum())
print("Missing values in credits_df:\n", credits_df.isnull().sum())

# Check for duplicates
print("Duplicate rows in movies_df:", movies_df.duplicated().sum())
print("Duplicate rows in credits_df:", credits_df.duplicated().sum())

# Data type validation
print("Data types in movies_df:\n", movies_df.dtypes)
print("Data types in credits_df:\n", credits_df.dtypes)

# Range checks (example: checking budget and revenue)
print("Budget range in movies_df:\n", movies_df['budget'].describe())
print("Revenue range in movies_df:\n", movies_df['revenue'].describe())

# Consistency checks (example: checking if movie_id in credits_df matches id in movies_df)
credits_df['movie_id'] = credits_df['movie_id'].astype(int)
missing_ids = credits_df[~credits_df['movie_id'].isin(movies_df['id'])]
print("Missing movie_ids in movies_df:\n", missing_ids)

def check_missing_values(df):
    return df.isnull().sum()

def check_duplicates(df):
    return df.duplicated().sum()

def check_data_types(df):
    return df.dtypes

def check_range(df, column):
    return df[column].describe()

def check_consistency(df1, df2, column1, column2):
    return df1[~df1[column1].isin(df2[column2])]

# Example usage
print("Missing values in movies_df:\n", check_missing_values(movies_df))
print("Duplicate rows in credits_df:", check_duplicates(credits_df))
print("Data types in movies_df:\n", check_data_types(movies_df))
print("Budget range in movies_df:\n", check_range(movies_df, 'budget'))
print("Inconsistent movie_ids:\n", check_consistency(credits_df, movies_df, 'movie_id', 'id'))

# Plot missing values
def plot_missing_values(df):
    missing = df.isnull().sum()
    missing = missing[missing > 0]
    plt.figure(figsize=(10, 6))
    sns.barplot(x=missing.index, y=missing.values)
    plt.xticks(rotation=90)
    plt.title('Missing Values in Dataset')
    plt.show()

plot_missing_values(movies_df)

# Save missing values report
missing_report = check_missing_values(movies_df)
missing_report.to_csv('missing_values_report.csv')

# Save duplicates report
duplicates_report = check_duplicates(credits_df)
with open('duplicates_report.txt', 'w') as file:
    file.write(f"Number of duplicate rows: {duplicates_report}\n")

# Example using SQLAlchemy to connect to a SQLite database
engine = create_engine('sqlite:///data_quality.db')
movies_df.to_sql('movies', con=engine, if_exists='replace', index=False)
credits_df.to_sql('credits', con=engine, if_exists='replace', index=False)

# Fill missing values in 'release_date' with 'Unknown'
movies_df['release_date'] = movies_df['release_date'].fillna('Unknown')

# Fill missing values in 'runtime' with the median value
movies_df['runtime'] = movies_df['runtime'].fillna(movies_df['runtime'].median())

# Fill missing values in 'tagline' with 'No tagline'
movies_df['tagline'] = movies_df['tagline'].fillna('No tagline')

movies_df['release_date'] = pd.to_datetime(movies_df['release_date'], errors='coerce')

# Example: Checking the format of 'cast' and 'crew' columns
print(credits_df['cast'].head())
print(credits_df['crew'].head())

def plot_missing_values(df):
    missing = df.isnull().sum()
    missing = missing[missing > 0]
    plt.figure(figsize=(10, 6))
    sns.barplot(x=missing.index, y=missing.values)
    plt.xticks(rotation=90)
    plt.title('Missing Values in Dataset')
    plt.show()

def plot_value_ranges(df, column):
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column].dropna(), bins=50, kde=True)
    plt.title(f'{column} Distribution')
    plt.show()

plot_missing_values(movies_df)
plot_value_ranges(movies_df, 'budget')

# Example: Save report to a file
missing_report = check_missing_values(movies_df)
missing_report.to_csv('missing_values_report.csv')

import pandas as pd
import schedule
import time


def check_missing_values(df):
    missing_values = df.isnull().sum()
    print("Missing values in dataset:")
    print(missing_values)


def check_duplicates(df):
    duplicate_rows = df.duplicated().sum()
    print(f"Duplicate rows in dataset: {duplicate_rows}")


def main():
    # Load datasets
    movies_df = pd.read_csv(
        'C:/Users/shree/OneDrive/Documents/GitHub/Automated-Data-Quality-Monitoring-System/tmdb_5000_movies.csv')
    credits_df = pd.read_csv(
        'C:/Users/shree/OneDrive/Documents/GitHub/Automated-Data-Quality-Monitoring-System/tmdb_5000_credits.csv')

    # Perform checks
    check_missing_values(movies_df)
    check_duplicates(movies_df)
    # Add other checks as needed


if __name__ == "__main__":
    main()

def job():
    main()  # Call the main function from the perform_data_quality_checks module


import pandas as pd
import schedule
import time


def check_missing_values(df):
    missing_values = df.isnull().sum()
    print("Missing values in dataset:")
    print(missing_values)


def check_duplicates(df):
    duplicate_rows = df.duplicated().sum()
    print(f"Duplicate rows in dataset: {duplicate_rows}")


def job():
    print("Running scheduled data quality checks...")
    # Load datasets
    try:
        movies_df = pd.read_csv(
            'C:/Users/shree/OneDrive/Documents/GitHub/Automated-Data-Quality-Monitoring-System/tmdb_5000_movies.csv')
        credits_df = pd.read_csv(
            'C:/Users/shree/OneDrive/Documents/GitHub/Automated-Data-Quality-Monitoring-System/tmdb_5000_credits.csv')

        # Perform checks
        check_missing_values(movies_df)
        check_duplicates(movies_df)
        # Add other checks as needed

    except Exception as e:
        print(f"An error occurred: {e}")









