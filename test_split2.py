
# Use split_text_to_chunks to divide any text into chunk

# Example usage

file_path="inputs/sd.md"

with open(file_path, 'r') as text_file:
    chunks = split_text_to_chunks2(text_file, max_chars=150, overlap=0)
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i + 1}: {chunk}\n")