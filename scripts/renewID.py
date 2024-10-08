import pandas as pd
import numpy as np

# Load the spreadsheet (change the filename as needed)
get_file_path = '/Users/milanichikeka/Documents/Tech Giants anaylytics/updated_location_without_commas(1) 2.csv'  # Replace with your actual file path
dest_file_path = '/Users/milanichikeka/Documents/GitHub/rProgrammingCaptsone/spreadsheets/updated_location_without_commas(1) 2.csv'  # Replace with your actual file path



# Read the data into a DataFrame
df = pd.read_csv(get_file_path, sep=',')  # Removed the sheet_name argument

# Check the existing IDs and the number of rows
num_rows = len(df)

# Generate unique IDs starting from 1
# If you want to start from a different number, change the range accordingly
new_ids = np.arange(1, num_rows + 1)

# Assign new unique IDs to the 'id' column (assuming it's the first column)
df['id'] = new_ids

# Save the updated DataFrame back to the spreadsheet
df.to_csv(dest_file_path, index=False)

print("Unique IDs regenerated successfully.")
