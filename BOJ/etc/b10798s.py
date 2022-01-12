# words라는 2차원배열을 만든다.
words = [input() for i in range(5)]

for j in range(15):
    for i in range(5):
        if j < len(words[i]):
            print(words[i][j], end='')
