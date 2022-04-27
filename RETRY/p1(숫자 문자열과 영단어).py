def solution(s):
    answer = ''
    dict = {"zero":0 ,"one":1 ,"two":2 , "three":3 , "four":4 , "five":5 , "six":6 ,"seven" : 7 ,"eight":8 ,"nine":9}
    for x in dict.keys():
        if x in s:
            s = s.replace(x,str(dict[x]))
    return int(s)

solution("one4seveneight")