tired = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
def mine(minerals, tool):
    result = 0
    for s_mineral in minerals:
        mineral = 0
        if s_mineral == "diamond":
            mineral = 0
        elif s_mineral == "iron":
            mineral = 1
        elif s_mineral == "stone":
            mineral = 2
        result += tired[tool][mineral]

    return result

def solution(picks, minerals):
    mineral_five_list = []
    left = sum(picks)
    for i in range(left):
        if 5*i >= len(minerals):
            break
        mineral_five_list.append(minerals[5*i:5*i+5])

    sorted_minerals = sorted(mineral_five_list, key=lambda x:(x.count("diamond"), x.count("iron"), x.count("stone")), reverse=True)

    result = 0
    for sm in sorted_minerals:
        if picks[0] != 0:
            result += mine(sm, 0)
            picks[0] -= 1
        elif picks[1] != 0:
            result += mine(sm, 1)
            picks[1] -= 1
        elif picks[2] != 0:
            result += mine(sm, 2)
            picks[2] -= 1
        else:
            break
    print(result)

solution([0, 1, 0], ["iron", "iron", "iron", "iron", "iron", "diamond", "diamond","diamond","diamond","diamond"])
solution([0, 1, 0], ["diamond", "diamond", "diamond", "diamond", "diamond", "diamond", "diamond"])
solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"])
solution([0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"])
