# string Compression

text = input("Enter a string: ")
result = ""
i = 0
while i < len(text):
    count = 1
    while i + count < len(text) and text[i + count] == text[i]:
        count += 1
    result += text[i] + str(count)
    i += count 
print("Compressed:", result)