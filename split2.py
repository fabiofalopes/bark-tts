import nltk
from typing import List, Union

def split_text_to_chunks2(text_or_file: Union[str, object], max_chars: int = 200, overlap: int = 50) -> List[str]:
    """
    Split text into chunks of approximately max_chars length, respecting sentence boundaries where possible.
    
    Args:
    text_or_file (str or file-like object): The input text or a file object to read from.
    max_chars (int): Maximum number of characters per chunk.
    overlap (int): Number of characters to overlap between chunks.
    
    Returns:
    List[str]: A list of text chunks.
    """
    if hasattr(text_or_file, 'read'):
        text = text_or_file.read()
    else:
        text = text_or_file

    sentences = nltk.sent_tokenize(text)
    chunks = []
    current_chunk = ""
    
    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= max_chars:
            current_chunk += " " + sentence
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            
            # If the sentence is longer than max_chars, split it
            if len(sentence) > max_chars:
                words = sentence.split()
                temp_chunk = ""
                for word in words:
                    if len(temp_chunk) + len(word) <= max_chars:
                        temp_chunk += " " + word
                    else:
                        chunks.append(temp_chunk.strip())
                        temp_chunk = word
                if temp_chunk:
                    current_chunk = temp_chunk
            else:
                current_chunk = sentence

    if current_chunk:
        chunks.append(current_chunk.strip())

    # Add overlap
    if overlap > 0:
        overlapped_chunks = []
        for i, chunk in enumerate(chunks):
            if i > 0:
                start = max(0, len(chunk) - overlap)
                chunk = chunks[i-1][-overlap:] + " " + chunk
            if i < len(chunks) - 1:
                end = min(len(chunk), len(chunk) - overlap)
                chunk = chunk[:end]
            overlapped_chunks.append(chunk.strip())
        chunks = overlapped_chunks

    return chunks

