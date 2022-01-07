from collections import deque
import sys

deq = deque()

N = int(sys.stdin.readline())

def push(word):
    deq.append(word)
    # print(word)

def pop():
    if(len(deq) == 0):
        print(-1)
    else:
        print(deq.popleft())

def size():
    print(len(deq))

def empty():
    if(len(deq) == 0):
        print(1)
    else:
        print(0)

def front():
    if(len(deq) == 0):
        print(-1)
    else:
        print(deq[0])

def back():
    if (len(deq) == 0):
        print(-1)
    else:
        print(deq[-1])



for i in range(N):
    word = list(sys.stdin.readline().split())
    first_word = word[0]

    if  (first_word == 'push'):
        push(word[1])
    elif(first_word == 'pop'):
        pop()
    elif(first_word == 'size'):
        size()
    elif(first_word == 'empty'):
        empty()
    elif(first_word == 'front'):
        front()
    elif(first_word == 'back'):
        back()


