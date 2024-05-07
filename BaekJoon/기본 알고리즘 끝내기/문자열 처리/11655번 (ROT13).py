text = input()

for t in text:
    if t.islower():
        print(chr((ord(t)-97+13)%26+97), end="")
    elif t.isupper():
        print(chr((ord(t)-65+13)%26+65), end="")
    else:
        print(t, end="")