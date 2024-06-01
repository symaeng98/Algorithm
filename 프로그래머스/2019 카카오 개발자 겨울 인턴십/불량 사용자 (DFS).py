def solution(user_id, banned_id):
    def check(s, v):
        if len(s) != len(v):
            return False

        for i in range(len(s)):
            if s[i] == "*":
                continue
            if s[i] != v[i]:
                return False

        return True

    result = []
    def dfs(bid, index):
        if len(index) == len(banned_id):
            s_index = tuple(sorted(index))
            if s_index in result:
                return
            result.append(s_index)
            return

        for i in range(len(user_id)):
            if i not in index:
                if check(banned_id[bid], user_id[i]):
                    index.append(i)
                    dfs(bid+1, index)
                    index.pop()

    dfs(0, [])

    return len(result)