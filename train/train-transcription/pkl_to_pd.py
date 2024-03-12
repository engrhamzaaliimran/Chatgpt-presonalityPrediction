import pandas as pd
import pickle

# Load data from pickle file
with open('transcription_training.pkl', 'rb') as file:
    data = pickle.load(file)

# Create DataFrame
df = pd.DataFrame(list(data.items()), columns=['Video Name', 'Transcription'])

# Print the head of the DataFrame
print(df.head())

# Save DataFrame to CSV
df.to_csv('transcription_training.csv', index=False)

print("Data has been successfully saved to transcription_training.csv.")

