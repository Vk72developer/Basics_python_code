# First Non-Repeating Character 

text = input("Enter a string: ")
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
for ch in text:
    if freq[ch] == 1:
        answer = ch 
        break 

if answer is None:
    print("No non-repeating character")
else:
    print("First non-repeating character:", answer)