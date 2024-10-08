import pandas as pd

# Load the CSV file
input_file = '/Users/blessingt03/Documents/GitHub/rProgrammingCaptsone/spreadsheets/cleaned_listings_updated.csv'  # Replace with your actual file path
output_file = '/Users/blessingt03/Documents/GitHub/rProgrammingCaptsone/spreadsheets/cleaned_listings_wSemiCol.csv'  # Replace with your desired output file path

# Read the CSV file with commas as the delimiter
df = pd.read_csv(input_file)

# Save the file with semicolons as the delimiter
df.to_csv(output_file, index=False, sep=';')

print(f"File saved with semicolons as delimiter: {output_file}")