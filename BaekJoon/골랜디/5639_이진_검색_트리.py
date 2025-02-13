"""실제 노드를 구현해서 푸는 풀이
"""

# import sys
# sys.setrecursionlimit(10**5)
#
# nodes = []
# while True:
#     try:
#         nodes.append(int(input()))
#     except:
#         break
#
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#
# def insert(node, x):
#     while True:
#         if node.data > x.data:
#             if node.left is None:
#                 node.left = x
#                 break
#             node = node.left
#         else:
#             if node.right is None:
#                 node.right = x
#                 break
#             node = node.right
#
# def postorder(node):
#     if node.left:
#         postorder(node.left)
#     if node.right:
#         postorder(node.right)
#     print(node.data)
#
# root = Node(nodes[0])
# for i in range(1, len(nodes)):
#     x = Node(nodes[i])
#     insert(root, x)
#
# postorder(root)


"""전위 순회 만으로 후위 순회를 얻어내는 풀이
"""

import sys
sys.setrecursionlimit(10**5)

nodes = []
while True:
    try:
        nodes.append(int(input()))
    except:
        break


def postorder(start, end):
    if start > end:
        return
    mid = end+1
    for i in range(start+1, end+1):
        if nodes[i] > nodes[start]:
            mid = i
            break

    postorder(start+1, mid-1)
    postorder(mid, end)
    print(nodes[start])


postorder(0, len(nodes)-1)
