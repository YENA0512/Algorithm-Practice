def solution(s):

    list = []
    
    for c in s:
        if len(list) == 0:
            list.append(c)
            continue
        if list[-1] == c:
            list.pop()
            
        else:
            list.append(c)
    if len(list) == 0:
        return 1
    else:
        return 0

# use stack