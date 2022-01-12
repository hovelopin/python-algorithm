while 1 :
    num = input()
    if(num == '0'):
        break
    # 뒤에서부터 읽을수있도록 slice로 짤라주는것이 중요
    if(num == num[::-1]):
        print('yes')
    else:
        print('no')