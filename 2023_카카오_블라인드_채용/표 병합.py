un_gn = -1
def update_value(table, r, c, value):
    v, gn = table[r][c]
    if gn == -1:
        table[r][c][0] = value
        return
    for i in range(1, 51):
        for j in range(1, 51):
            if table[i][j][1] == gn:
                table[i][j][0] = value

def update_all_value(table, value1, value2):
    for i in range(1, 51):
        for j in range(1, 51):
            if table[i][j][0] == value1:
                table[i][j][0] = value2

def merge(table, r1, c1, r2, c2):
    if r1 == r2 and c1 == c2:
        return

    v, gn = table[r1][c1]
    v2, gn2 = table[r2][c2]

    if v == "EMPTY" and v2 == "EMPTY":
        for i in range(1, 51):
            for j in range(1, 51):
                if table[i][j][1] == gn or table[i][j][1] == gn2:
                    table[i][j] = [v, gn]

    elif v == "EMPTY" and v2 != "EMPTY":
        for i in range(1, 51):
            for j in range(1, 51):
                if table[i][j][1] == gn:
                    table[i][j] = [v2, gn2]
    else:
        for i in range(1, 51):
            for j in range(1, 51):
                if table[i][j][1] == gn2:
                    table[i][j] = [v, gn]


def unmerge(table, r, c):
    global un_gn
    v, gn = table[r][c]
    for i in range(1, 51):
        for j in range(1, 51):
            if table[i][j][1] == gn:
                table[i][j] = ["EMPTY", un_gn]
                un_gn -= 1
    table[r][c][0] = v

def print_table(table, r, c):
    return table[r][c][0]

def solution(commands):
    result = []
    table = [[] for _ in range(51)]
    gn = 1
    for i in range(1, 51):
        for j in range(51):
            table[i].append(["EMPTY", gn])
            gn += 1

    for command in commands:
        arr = list(command.split(" "))
        if arr[0] == "UPDATE":
            if len(arr) == 4:
                r, c, v = int(arr[1]), int(arr[2]), arr[3]
                update_value(table, r, c, v)
            else:
                v1, v2 = arr[1], arr[2]
                update_all_value(table, v1, v2)
        elif arr[0] == "MERGE":
            r1, c1, r2, c2 = int(arr[1]), int(arr[2]), int(arr[3]), int(arr[4])
            merge(table, r1, c1, r2, c2)
        elif arr[0] == "UNMERGE":
            r, c = int(arr[1]), int(arr[2])
            unmerge(table, r, c)
        elif arr[0] == "PRINT":
            r, c = int(arr[1]), int(arr[2])
            result.append(print_table(table, r, c))

    return result

print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))
print(solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))