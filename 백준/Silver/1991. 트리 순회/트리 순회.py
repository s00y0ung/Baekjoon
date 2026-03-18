import sys
input = sys.stdin.readline

def preorder(tree,s):
    if s == -1:
        return
    print(chr(s+65), end='')
    preorder(tree,tree[s][0])
    preorder(tree,tree[s][1])

def inorder(tree,s):
    if s == -1:
        return
    inorder(tree,tree[s][0])
    print(chr(s+65), end='')
    inorder(tree,tree[s][1])

def postorder(tree,s):
    if s == -1:
        return
    postorder(tree,tree[s][0])
    postorder(tree,tree[s][1])
    print(chr(s+65), end='')

def main():
    n = int(input())
    tree = [[] for _ in range(n)]
    for _ in range(n):
        a,b,c = map(str,input().split())
        tree[ord(a)-65] = [max(-1,ord(b)-65), max(-1,ord(c)-65)]

    preorder(tree,0)
    print()
    inorder(tree,0)
    print()
    postorder(tree,0)

if __name__ == '__main__':
    main()