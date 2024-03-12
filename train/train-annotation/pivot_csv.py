import pandas as pd

# Read the input CSV file
df = pd.read_csv('output_data.csv', delimiter='\t')

# Print the columns to verify their names
print(df.columns)

# Pivot the dataframe to get the desired format
df_pivot = df.groupby(['Video', 'Trait'])['Value'].first().unstack().reset_index()

# Save the pivoted dataframe to a new CSV file
df_pivot.to_csv('output_data_pivot.csv', index=False)

