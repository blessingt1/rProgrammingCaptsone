import pandas as pd

# Load both spreadsheets
df1 = pd.read_csv('cleaned_listings_updated(1) copy.csv', sep=';')
df2 = pd.read_csv('/Users/blessingt03/Documents/GitHub/rProgrammingCaptsone/spreadsheets/cleaned_listings_updated.csv', sep=';')  # Replace with the path to your second file

# Swap the first column ('id' or column index 0) of both DataFrames
df1_first_col = df1.iloc[:, 0].copy()  # First column from df1
df2_first_col = df2.iloc[:, 0].copy()  # First column from df2

df1.iloc[:, 0] = df2_first_col  # Replace df1's first column with df2's first column
df2.iloc[:, 0] = df1_first_col  # Replace df2's first column with df1's first column

# Save the updated data back to CSV
df1.to_csv('cleaned_listings_updated(1) copy.csv', index=False)  # Save the updated df1
df2.to_csv('cleaned_listings_updated.csv', index=False)  # Save the updated df2

print("Columns swapped and files updated successfully!")