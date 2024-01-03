a, b, c = map(int, input().split())
if a == b and b == c:
    print(10000+1000*a)
elif a != b and b != c and a != c:
    print(max(a,b,c)*100)
else:
    if a == b or a == c:
        print(1000 + a*100)
    else:
        print(1000 + b*100)
