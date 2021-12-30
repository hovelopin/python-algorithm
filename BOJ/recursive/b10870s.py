def fi(N):
   if(N==0):
       return 0
   elif(N==1):
       return 1
   else:
        return fi(N-1) + fi(N-2)

N = int(input())

print(fi(N))

