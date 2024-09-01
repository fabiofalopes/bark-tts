import re
import nltk
import os

# run 'python download_nltk.py' first

def split_text_to_sentence_chunks(text_or_file, min_words=10, max_words=15):
    if hasattr(text_or_file, 'read'):
        # If it's a file object, read the text
        text = text_or_file.read()
    else:
        # If it's not a file object, assume it's a string
        text = text_or_file

    # Tokenize text into sentences
    sentences = nltk.sent_tokenize(text)
    chunks = []
    current_chunk = ""
    current_word_count = 0

    for sentence in sentences:
        sentence_words = nltk.word_tokenize(sentence)
        sentence_word_count = len(sentence_words)

        if current_word_count + sentence_word_count > max_words:
            if current_word_count >= min_words:
                chunks.append(current_chunk.strip())
                current_chunk = sentence
                current_word_count = sentence_word_count
            else:
                current_chunk += " " + sentence
                current_word_count += sentence_word_count
        else:
            current_chunk += " " + sentence
            current_word_count += sentence_word_count

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

'''
# Example usage
with open("inputs/sd.md", 'r') as file:
    chunks = split_text_to_sentence_chunks(file)
    for idx, chunk in enumerate(chunks):
        print(f"Chunk {idx+1}: {chunk}")
'''