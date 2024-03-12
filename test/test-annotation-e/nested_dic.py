import pickle
import pandas as pd

# Replace 'annotation_training.pkl' with your actual file path
file_path = 'annotation_test.pkl'

# Read the pickle file using pickle module with 'latin1' encoding
with open(file_path, 'rb') as file:
    data_dict = pickle.load(file, encoding='latin1')

# Flatten the nested dictionary
flat_data = []

for trait, videos in data_dict.items():
    for video, value in videos.items():
        flat_data.append({
            'Trait': trait,
            'Video': video,
            'Value': value
        })

# Create a DataFrame from the flattened data
df = pd.DataFrame(flat_data)

# Print the head of the DataFrame
print(df.head())

# Specify the desired CSV file path
csv_file_path = 'output_data.csv'

# Dump the DataFrame into a CSV file
df.to_csv(csv_file_path, index=False)

print(f'Data has been successfully dumped to {csv_file_path}.')

