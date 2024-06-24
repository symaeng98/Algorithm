def solution(triangle):
    for i in range(len(triangle)-1):
        triangle[i+1][0] += triangle[i][0]
        for j in range(1, len(triangle[i+1])-1):
            triangle[i+1][j] += max(triangle[i][j-1], triangle[i][j])
        triangle[i+1][len(triangle[i+1])-1] += triangle[i][len(triangle[i+1])-2]

    return max(triangle[-1])