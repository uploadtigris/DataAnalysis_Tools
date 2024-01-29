import pandas as pd

# Load your CSV file into a Pandas DataFrame
csv_file_path = r'E:\UI Lab\Electricity and EV Adoption\Code\iou_zipcodes_2021.csv'
df = pd.read_csv(csv_file_path)

# Print the original data type of the 'zip' column
print("Original 'zip' column data type:", df.dtypes['zip'])

# Convert the "zip" column to Text datatype with a length of 10 characters
df['zip'] = df['zip'].astype(str).str.zfill(5)

# Print the modified data type of the 'zip' column
print("Modified 'zip' column data type:", df.dtypes['zip'])

# Save the modified DataFrame back to a CSV file
modified_csv_file_path = r'E:\UI Lab\Electricity and EV Adoption\Code\modified_iou_zipcodes_2021.csv'
df.to_csv(modified_csv_file_path, index=False)
print(f"Modified CSV file saved at: {modified_csv_file_path}")
