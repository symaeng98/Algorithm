#Input
st1 = input()
st2 = input()

#dp array
dp = [[0]*(len(st1)+1) for x in range(len(st2)+1)]

#problem solving
for i in range(1,len(st2)+1): #We have to compare the letters in st2 based on the letters in st1
    for j in range(1,len(st1)+1): #So, 'for loop based on st1' is in the 'for loop based on st2'
        if st2[i-1] == st1[j-1]: #If the letter is the same
            dp[i][j] = dp[i-1][j-1] + 1 #add one to the previous value
        else: #If the letter is different,
            dp[i][j] = max(dp[i][j-1], dp[i-1][j]) #put the larger one between dp[i][j-1] and dp[i-1][j]

print("Length of the LCS : ",end="")
print(dp[-1][-1])
print("")

#Structure of dp
print("<Structure of DP>")
for i in range(len(st2)+1):
    for j in range(len(st1)+1):
        print(dp[i][j],end=" ")
    print("")