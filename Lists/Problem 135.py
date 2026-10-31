# Chunk a List into Size-n-Pieces 

numbers = [1, 2, 3, 4, 5, 6, 7]

size = 3
chunks = []

for i in range(0, len(numbers), size):
    chunks.append(numbers[i:i + size])

print("Chunks:", chunks)