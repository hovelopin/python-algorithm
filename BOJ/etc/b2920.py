sound_num = list(map(str,input().split()))

stand = ''.join(sound_num)

if(stand == '12345678'):
    print('ascending')
elif(stand == '87654321'):
    print('descending')
else:
    print('mixed')

