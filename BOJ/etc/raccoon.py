def raccoon(n):
    if( n== 0 ):
        return 2
    elif ( n== 1 ):
        return 4
    else:
        return raccoon(n-1) + raccoon(n-2)

print(raccoon(5))