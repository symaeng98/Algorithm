from itertools import permutations
import copy

def solution(expression):
    answer = 0

    cal = set()
    ex_list = []
    num = ""
    for ex in expression:
        if ex in ['+', '-', '*']:
            cal.add(ex)
            ex_list.append(num)
            ex_list.append(ex)
            num = ""
        else:
            num += ex
    ex_list.append(num)

    result = -1
    for per in permutations(cal):
        tmp = copy.deepcopy(ex_list)
        for p in per:
            stack = []
            index = 0
            while index < len(tmp):
                if tmp[index] == p:
                    l = int(stack.pop())
                    r = int(tmp[index+1])
                    if p == '+':
                        stack.append(str(l+r))
                    elif p == '-':
                        stack.append(str(l-r))
                    elif p == '*':
                        stack.append(str(l*r))
                    index += 1
                else:
                    stack.append(tmp[index])
                index += 1

            if len(stack) == 1:
                result = max(result, abs(int(stack[0])))
            tmp = stack



    return result