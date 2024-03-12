def check(current, rectangle):
    result = []
    x, y = current
    for x1, y1, x2, y2 in rectangle:
        if y1 == y and x1<=x<x2:
            result.append(0)
        if x2 == x and y1<=y<y2:
            result.append(1)
        if y2 == y and x1<x<=x2:
            result.append(2)
        if x1 == x and y1<y<=y2:
            result.append(3)

    if set(result) == {0, 3}:
        return max(result)
    else:
        return min(result)


def move(point, l_index):
    direct = [[1,0], [0,1], [-1,0], [0,-1]]
    dx, dy = direct[l_index]
    x, y = point
    return (x+dx, y+dy)


def solution(rectangle, characterX, characterY, itemX, itemY):
    start = (characterX, characterY)
    item = (itemX, itemY)
    current = (characterX, characterY)
    start_d, item_d = 0, 0
    while True:
        l_index = check(current, rectangle)
        current = move(current, l_index)
        start_d += 1
        if current == item:
            item_d = start_d
        if current == start:
            break

    return min(start_d-item_d, item_d)

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))
print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1))
print(solution([[1,1,5,7]], 1, 1, 4, 7))
print(solution([[2,1,7,5],[6,4,10,10]], 3, 1, 7, 10))
print(solution([[2,2,5,5],[1,3,6,4],[3,1,4,6]], 1, 4, 6, 3))