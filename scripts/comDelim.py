import pandas as pd

# Load the CSV file
input_file = 'your_input_file.csv'  # Replace with your actual file path
output_file = 'your_output_file.csv'  # Replace with your desired output file path

# Read the CSV file with commas as the delimiter
df = pd.read_csv(input_file)

# Save the file with semicolons as the delimiter
df.to_csv(output_file, index=False, sep=';')

print(f"File saved with semicolons as delimiter: {output_file}")