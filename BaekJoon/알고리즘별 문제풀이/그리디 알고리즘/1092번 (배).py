n = int(input())
ships = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

ships.sort(reverse=True)
boxes.sort(reverse=True)

time = 0
if boxes[0] > ships[0]:
    print(-1)
else:
    while boxes:
        for ship in ships:
            if len(boxes) == 0:
                break
            for box in boxes:
                if box <= ship:
                    boxes.remove(box)
                    break
        time += 1

    print(time)