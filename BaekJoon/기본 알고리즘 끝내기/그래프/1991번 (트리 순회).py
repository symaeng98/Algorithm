from collections import defaultdict
n = int(input())
tree = defaultdict(list)

for _ in range(n):
    a, b, c = input().split()
    tree[a] = [b, c]

def preorder(v):
    if v == ".":
        return
    print(v, end="")
    preorder(tree[v][0])
    preorder(tree[v][1])

preorder("A")
print()

def inorder(v):
    if v == ".":
        return
    left = tree[v][0]
    right = tree[v][1]
    inorder(left)
    print(v, end="")
    inorder(right)

inorder("A")
print()

def postorder(v):
    if v == ".":
        return
    left = tree[v][0]
    right = tree[v][1]
    postorder(left)
    postorder(right)
    print(v, end="")

postorder("A")
