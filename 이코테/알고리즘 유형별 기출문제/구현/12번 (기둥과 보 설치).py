def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate == 0:
            answer.remove([x,y,stuff])
            if not possible(answer):
                answer.append([x,y,stuff])
        if operate == 1:
            answer.append([x,y,stuff])
            if not possible(answer):
                answer.remove([x,y,stuff])
    return sorted(answer)


def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 기둥인 경우
            # 바닥 위 or 보의 한쪽 끝 부분 위 or 다른 기둥 위
            if y == 0 or ([x-1, y, 1] in answer) or ([x, y, 1] in answer) or ([x, y-1, 0] in answer):
                continue
            return False
        elif stuff == 1:
            # 한쪽 끝부분이 기둥 위 or 양쪽 끝부분이 다른 보와 동시 연결
            if ([x, y-1, 0] in answer) or ([x+1, y-1, 0] in answer) or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True