while True:
    x = input()
    if x == "end":
        break

    board = []
    for i in range(3):
        board.append(list(x[i*3:(i+1)*3]))

    x_pos = []
    o_pos = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "O":
                o_pos.append((i,j))
            elif board[i][j] == "X":
                x_pos.append((i,j))

    def check(b, o_x):
        if b[0][0]==b[0][1]==b[0][2]==o_x:
            return True
        if b[1][0]==b[1][1]==b[1][2]==o_x:
            return True
        if b[2][0]==b[2][1]==b[2][2]==o_x:
            return True
        if b[0][0]==b[1][0]==b[2][0]==o_x:
            return True
        if b[0][1]==b[1][1]==b[2][1]==o_x:
            return True
        if b[0][2]==b[1][2]==b[2][2]==o_x:
            return True
        if b[0][0]==b[1][1]==b[2][2]==o_x:
            return True
        if b[2][0]==b[1][1]==b[0][2]==o_x:
            return True
        return False

    x_cnt = len(x_pos)
    o_cnt = len(o_pos)
    if not (x_cnt == o_cnt or x_cnt == o_cnt+1):
        print("invalid")
        continue

    if x_cnt == o_cnt:
        if check(board, "O") and not check(board, "X"):
            print("valid")
            continue
    if x_cnt == o_cnt+1:
        if check(board, "X") and not check(board, "O"):
            print("valid")
            continue
    if x_cnt == 5 and o_cnt == 4:
        if not check(board, "O"):
            print("valid")
            continue

    print("invalid")
