# swea 코드 
import sys
sys.setrecursionlimit(1000000)

def inorder (cur , node):
    # 왼쪽 자식 노드 방문
    inorder(cur*2 , node)
    if( cur > lastIdx ):
        return 0
    # 현재 노드 방문
    print(node[cur]+ '')
    # 오른쪽 자식노드 방문
    inorder(cur*2+1 , node)

for tc in range(10):
    N = int(input())
    lastIdx = N
    tree = list(map(str,input().split()))
    print(tree)
    inorder(1,tree)