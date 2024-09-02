import nltk
from typing import List, Union

def split_text_to_chunks(text_or_file: Union[str, object], min_chars: int = 100, max_chars: int = 200) -> List[str]:
    """
    Split text into chunks respecting sentence boundaries, with size constraints.
    
    Args:
    text_or_file (str or file-like object): The input text or a file object to read from.
    min_chars (int): Minimum number of characters per chunk.
    max_chars (int): Maximum number of characters per chunk.
    
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
            current_chunk = sentence

        # If the current chunk is longer than max_chars, we need to split it
        while len(current_chunk) > max_chars:
            split_point = current_chunk.rfind(' ', min_chars, max_chars)
            if split_point == -1:  # If we can't find a space, we'll have to split mid-word
                split_point = max_chars
            chunks.append(current_chunk[:split_point].strip())
            current_chunk = current_chunk[split_point:].strip()

    # Add any remaining text as the last chunk
    if current_chunk:
        chunks.append(current_chunk.strip())

    # Merge short chunks with neighbors
    i = 0
    while i < len(chunks) - 1:
        if len(chunks[i]) < min_chars:
            if len(chunks[i] + " " + chunks[i+1]) <= max_chars:
                chunks[i] += " " + chunks[i+1]
                chunks.pop(i+1)
            else:
                i += 1
        else:
            i += 1

    return chunks

'''
# Example usage
text = "Your long text here. It can contain multiple sentences. Some sentences might be very long, while others could be quite short. We want to make sure that we respect sentence boundaries as much as possible, while also ensuring that our chunks are neither too short nor too long."
chunks = split_text_to_chunks(text, min_chars=100, max_chars=200)
for i, chunk in enumerate(chunks):
    print(f"Chunk {i + 1} ({len(chunk)} chars): {chunk}\n")

'''