# Longest Common Prefix 

words = ["flower", "flow", "flight"]
prefix = words[0]

for word in words[1:]:
    while not word.startswith(prefix):
        prefix = prefix[:-1]
        if prefix == "":
            break 

if prefix:
    print("Longest common prefix:", prefix)
else:
    print("No common prefix")
