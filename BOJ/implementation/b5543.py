hamburger = []
beverage = []

for i in range(5):
    if(i<3):
        hamburger.append(int(input()))
    else:
        beverage.append(int(input()))
print(min(hamburger)+min(beverage)-50)
