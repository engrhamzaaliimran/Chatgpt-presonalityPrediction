import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('output_data_pivot.csv')

# Sort the DataFrame based on the "Video" column
df_sorted = df.sort_values(by='Video')

# Write the sorted DataFrame to a new CSV file
df_sorted.to_csv('sorted_output_file_test.csv', index=False, sep='\t')

print("CSV file has been sorted and saved.")

