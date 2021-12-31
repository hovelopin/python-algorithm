N = int(input())

s_list = list(input())

for i in range(N-1):
    new_list = list(input())
    for j in range(len(s_list)):
        if ( s_list[j] != new_list[j] ):
            s_list[j] = '?'
print(''.join(s_list))







