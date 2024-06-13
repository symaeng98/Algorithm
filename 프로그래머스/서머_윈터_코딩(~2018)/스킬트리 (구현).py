def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        tmp = ""
        for s in skill_tree:
            if skill.count(s) == 0:
                continue
            tmp += s
        if tmp == skill[0:len(tmp)]:
            answer += 1

    return answer