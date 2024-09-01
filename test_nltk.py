import nltk

# Print all paths where NLTK is searching for data
print("NLTK data paths:", nltk.data.path)

# Attempt to load punkt again
try:
    nltk.data.find('tokenizers/punkt')
    print("Punkt tokenizer found!")
except LookupError:
    print("Punkt tokenizer not found in the specified paths.")
