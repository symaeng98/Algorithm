import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    n = len(nodeinfo)
    node_dict = {}
    graph = [[None, None] for _ in range(n+1)]
    for i in range(1, n+1):
        node_dict[i] = nodeinfo[i-1]

    s_node_dict = sorted(node_dict.items(), key=lambda x:(x[1][1], -x[1][0]))

    def div_con(top, arr):
        if not arr:
            return
        v, r = top
        rx = r[0]
        ry = r[1]

        left = []
        right = []
        for av, a in arr:
            ax, ay = a[0], a[1]
            if ax < rx:
                left.append((av, [ax, ay]))
            else:
                right.append((av, [ax, ay]))

        if left:
            left.sort(key=lambda x:x[1][1])
            l = left.pop()
            lv, lx, ly = l[0], l[1][0], l[1][1]
            graph[v][0] = lv
            div_con((lv, [lx, ly]), left)
        if right:
            right.sort(key=lambda x:x[1][1])
            r = right.pop()
            rv, rx, ry = r[0], r[1][0], r[1][1]
            graph[v][1] = rv
            div_con((rv, [rx, ry]), right)


    root = s_node_dict.pop()
    div_con(root, s_node_dict)

    pre = []
    post = []

    def preorder(v):
        if v == None:
            return
        pre.append(v)
        left, right = graph[v]
        preorder(left)
        preorder(right)

    def postorder(v):
        if v == None:
            return
        left, right = graph[v]
        postorder(left)
        postorder(right)
        post.append(v)


    preorder(root[0])
    postorder(root[0])
    return [pre, post]