import pandas as pd

# Creating DataFrames
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salary': [50000, 60000, 70000]}
df = pd.DataFrame(data)

# Basic operations
print(df.head())       # First few rows
print(df.describe())   # Summary statistics
print(df['Age'].mean())# Mean of Age column

# Indexing and selection
print(df.loc[0])               # First row
print(df.iloc[0:2])            # First two rows
print(df[df['Age'] > 25])      # Filtering

# Grouping and aggregation
grouped = df.groupby('Age').mean()

# Handling missing data
df['Bonus'] = [1000, None, 1500]  # Add column with missing value
df_filled = df.fillna(0)           # Fill missing values with 0