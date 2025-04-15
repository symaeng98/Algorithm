def solution(s):
    answer = []

    for x in s:
        stack = []
        cnt = 0
        now = []
        for c in x:
            if len(stack) >= 2 and c == "0" and stack[-2] == "1" and stack[-1] == "1":
                for _ in range(2):
                    stack.pop()
                cnt += 1
                continue
            stack.append(c)

        flag = True
        while stack:
            st = stack.pop()
            if st == "0" and flag:
                for _ in range(cnt):
                    now.append("110")
                flag = False
            now.append(st)

        if flag:
            for _ in range(cnt):
                now.append("110")

        now.reverse()
        answer.append(''.join(now))


    return answer