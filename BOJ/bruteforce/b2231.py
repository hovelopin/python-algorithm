N = int(input())

sum = 0

while 1:
    sum+=1
    result_list = list(str(sum))
    renumber = int(''.join(result_list))

    result_list = list(map(int,result_list))
    print(result_list)
    result = renumber+sum(result_list)

    if(result == N):
        print(renumber)
        break
    result_list = []

