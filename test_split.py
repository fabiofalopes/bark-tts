import split

with open("inputs/sd.md", 'r') as file:
    chunks = split.split_text_to_sentence_chunks(file)
    for idx, chunk in enumerate(chunks):
        print(f"Chunk {idx+1}: {chunk}")