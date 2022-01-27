a , b ,c = map(int,input().split())

stack = []

stack.append(a) ; stack.append(b) ;stack.append(c)
stack.remove(max(a,b,c))
print(max(stack))



