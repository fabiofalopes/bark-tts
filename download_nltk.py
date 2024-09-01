import nltk
import os

# Set NLTK data path to the directory within the virtual environment
nltk_data_dir = os.path.join(os.getcwd(), '.venv', 'nltk_data')
nltk.data.path.append(nltk_data_dir)

# Download the 'punkt' tokenizer to this directory
nltk.download('punkt', download_dir=nltk_data_dir)
nltk.download('punkt_tab', download_dir=nltk_data_dir)
