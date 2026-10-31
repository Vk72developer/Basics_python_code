# Check string Rotation
# ex-: "cdeab" is rotation of "abcde"

s1 = "abcde"
s2 = "cdeab"

if len(s1) == len(s2) and s2 in s1 + s1:
    print(s2, "is a rotation of", s1)
else:
    print(s2, "is not a rotation of", s1)