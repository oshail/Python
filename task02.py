import pandas as pd

# Path to the Excel file
file_path = '/Users/oshailmadaan/Desktop/csvtask2.xlsx'

# Read the Excel file
df = pd.read_excel(file_path)

# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# Filter data based on a condition

filtered_df = df[df['feb'] > 4,215,309]
print("\nFiltered DataFrame:")
print(filtered_df)

# Handle missing values
# Example: Drop rows with any missing values
df_dropped = df.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(df_dropped)

# Example: Fill missing values with a specified value
# Change 'column_name' and 'value_to_fill' as needed
df_filled = df.fillna(value={'column_name': 'value_to_fill'})
print("\nDataFrame after filling missing values:")
print(df_filled)

# Calculate summary statistics
summary = df.describe()
print("\nSummary statistics of the DataFrame:")
print(summary)
