def getBinaryNum(n,lists):
    a = n // 2
    b = n % 2
    lists.append(b)
    if a == 0 :
        return lists
    else :
        return getBinaryNum(a,lists)
def solution(n):
    list = []
    #getBinaryNum(n,list)
    c = bin(n).count('1')
    for m in range(n+1, n*2):
        if bin(m).count('1') == c:
            return m
    

'''
이진수 : bin()
세기 : count()
'''