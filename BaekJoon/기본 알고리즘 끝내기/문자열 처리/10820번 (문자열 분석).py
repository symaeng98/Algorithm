while True:
    try:
        text = input()
        lower, upper, num, blank = 0, 0, 0, 0
        for s in text:
            if s.islower():
                lower += 1
            elif s.isupper():
                upper += 1
            elif s.isdigit():
                num += 1
            elif s == " ":
                blank += 1
        print(lower, upper, num, blank)
    except EOFError:
        break