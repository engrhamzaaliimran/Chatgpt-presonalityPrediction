import pickle

# Specify the path to your transcription_training.pkl file
file_path = 'annotation_training.pkl'

# Open the file in binary mode and read the content
with open(file_path, 'rb') as file:
    # Load the content of the file using pickle
    data = pickle.load(file,encoding='latin1')

# Now, 'data' contains the deserialized content of the file
# You can work with the data as needed
print(data)
