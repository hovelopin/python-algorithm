n = int(input())

def starPrinting(n):
    if n == 3:
        return ['*']
    star = starPrinting(n//3 * (3/2))
    L = []

    for i in star:
        L.append(i*1)
    for i in star:
        L.append(i + ' '+ i)
    for i in star:
        L.append(i*5)

    return L

print('\n'.join(starPrinting(n)))