arr = input()
if arr[0] == '0':
    print(0)
else:
    eight_dict = {
        "0":"000",
        "1":"001",
        "2":"010",
        "3":"011",
        "4":"100",
        "5":"101",
        "6":"110",
        "7":"111"
    }
    result = []
    for a in arr:
        result.append(eight_dict[a])

    x = ''.join(result)
    print(x.lstrip("0"))
