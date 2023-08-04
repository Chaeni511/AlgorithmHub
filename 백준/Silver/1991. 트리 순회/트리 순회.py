import sys


# 전위 순회
def preorder_traverse(r):
    global res1
    if r != ".":
        res1 += r
        preorder_traverse(tree[r][0])
        preorder_traverse(tree[r][1])


# 중위 순회
def inorder_traverse(r):
    global res2
    if r != ".":
        inorder_traverse(tree[r][0])
        res2 += r
        inorder_traverse(tree[r][1])


# 후위 순회
def postorder_traverse(r):
    global res3
    if r != ".":
        postorder_traverse(tree[r][0])
        postorder_traverse(tree[r][1])
        res3 += r


N = int(sys.stdin.readline())

tree = {}
for _ in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]

res1 = ""
res2 = ""
res3 = ""

preorder_traverse("A")
inorder_traverse("A")
postorder_traverse("A")

print(res1)
print(res2)
print(res3)
