# BOJ 1991 트리 순회
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

class Node():
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right

def preorder(node): # 루트 - 왼쪽 - 오른쪽
    print(node.item, end ='')
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])

def inorder(node): # 왼쪽 - 루트 - 오른쪽
    if node.left != '.':
        inorder(tree[node.left])
    print(node.item, end='')
    if node.right != '.':
        inorder(tree[node.right])

def postorder(node): # 왼쪽 - 오른쪽 - 루트
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.item, end='')

N = int(input())
tree = {}

for _ in range(N):
    item, left, right = input().split()
    tree[item] = Node(item, left, right)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])