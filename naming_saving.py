import os
from scipy.io.wavfile import write as write_wav

def __get_unique_filename(base_name, directory):
    """Generate a unique filename by appending an incrementing number."""
    # Check if the directory exists
    if not os.path.isdir(directory):
        raise ValueError(f"The directory {directory} does not exist.")

    # Get a list of existing filenames in the directory
    existing_files = os.listdir(directory)

    # Extract existing numbers from filenames
    existing_numbers = []
    for filename in existing_files:
        if filename.startswith(base_name) and filename[len(base_name)].isdigit():
            try:
                number = int(filename[len(base_name):].split('.')[0])
                existing_numbers.append(number)
            except ValueError:
                continue

    # Find the highest number and increment
    highest_number = max(existing_numbers, default=0)
    next_number = highest_number + 1

    unique_filename = f"{base_name}{next_number}"
    
    return unique_filename

def save_text_file_with_unique_name(content, base_name, directory, extension='txt'):
    """Save a text file with a unique name in the specified directory."""
    # Generate a unique filename
    filename = __get_unique_filename(base_name, directory) + f".{extension}"
    
    # Full path to save the file
    filepath = os.path.join(directory, filename)
    
    # Save the file
    with open(filepath, 'w') as file:
        file.write(content)
    
    return filepath

def save_wav_file_with_unique_name(audio_array, base_name, directory, sample_rate):
    """Save a wav file with a unique name in the specified directory."""
    
    # Generate a unique filename
    filename = __get_unique_filename(base_name, directory) + ".wav"
    
    # Full path to save the file
    filepath = os.path.join(directory, filename)

    write_wav(filepath, sample_rate, audio_array)

    return filepath

'''
# Example usage
content = "This is a test file."
base_name = "test_file_"
directory = "outputs"  # Ensure this directory exists

# Save the file with a unique name
file_path = save_file_with_unique_name(content, base_name, directory)
print(f"File saved as: {file_path}")
'''