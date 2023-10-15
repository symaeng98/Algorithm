a = input()
str_arr = []
int_arr = []
for i in range(len(a)):
    if "0" <= a[i] <="9":
        int_arr.append(int(a[i]))
    else:
        str_arr.append(a[i])

str_arr.sort()
sum_value = sum(int_arr)

for s in str_arr:
    print(s,end="")
print(sum_value)