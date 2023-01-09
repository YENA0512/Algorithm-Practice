import heapq
def find_mid(nums) :
    '''
    n개의 정수들을 담고 있는 배열 nums가 매개변수로 주어집니다.
    nums의 각 정수들이 차례대로 주어질 때, 매 순간마다 
    "지금까지 입력된 수 중에서 중간값"을 리스트로 저장하여 반환하세요.
    '''
    n = len(nums)

    result = []
    
    l = []
    r = []
    for i in range(n) :
        x = nums[i]
        if not l or not r :
            heapq.heappush(l, -x)
        else :
            if x >= -l[0] :
                heapq.heappush(r,x)
            else :
                heapq.heappush(l, -x)
    # 두 힙의 크기를 조정
    # l, r이 갖고 있는 자료의 개수는 같아야 하며,홀수라면 l이 하나 더 많이 들고있도록.
        while not (len(l) == len(r) or len(l) == len(r) + 1) :
            # 크기 조정 
            if len(l) > len(r) :
                #l 에서 값을 뽑아와서 r에 넣어준다 
                heapq.heappush(r, -heapq.heappop(l))
            else :
                heapq.heappush(l, -heapq.heappop(r))
        result.append(-l[0])
    return result