'''
orderManager 클래스를 완성하세요.
'''

## 배열 사용

class orderManager :
    '''
    주문을 처리하는 class를 작성합니다.
    '''

    def __init__(self) :
        self.data = []

    def addOrder(self, orderId) :
        '''
        주문번호 orderId를 추가합니다.
        '''
        self.data.append(orderId)

    def removeOrder(self, orderId) :
        '''
        주문번호 orderId를 제거합니다.
        '''
        self.data.remove(orderId)

    def getOrder(self, orderId) :
        '''
        주문번호 orderId가 몇 번째로 처리될지를 반환합니다.

        만약 주문번호 orderId가 존재하지 않으면 -1을 반환합니다. 
        '''
        for i in range(len(self.data)) : 
            if self.data[i] == orderId :
                return (i + 1)
        return -1

## 연결 리스트 

'''
1. LinkedListElement 클래스를 완성하세요.
2. orderManager 클래스를 완성하세요.
'''

class LinkedListElement :
    def __init__(self, data, myPrev, myNext) :
        self.data = data
        self.myPrev = myPrev
        self.myNext = myNext
        
class orderManager :
    def __init__(self) :
        self.start = None
        self.end = None

    def addOrder(self, orderId) :
        o = LinkedListElement(orderId, None, None)

        if self.start == None and self.end == None :
            self.start = o
            self.end = o 
        else:
            self.end.myNext = o 
            o.myPrev = self.end

            self.end = o 

    def removeOrder(self, orderId) :
        
        if self.start == None and self.end == None :
            return 
        current = self.start

        while current != None :
            if current.data == orderId :
                prevElem = current.myPrev
                nextElem = current.myNext

                if prevElem != None:
                    prevElem.myNext = nextElem 
                if nextElem != None:
                    nextElem.myprev = prevElem
                if current == self.end:
                    self.end = prevElem 
                if current == self.start:
                    self.start = nextElem 
            current = current.myNext 

    def getOrder(self, orderId) :
        cnt = 0
        if self.start == None and self.end == None:
            return -1
        current = self.start
        while current != None :
            if current.data == orderId :
                return cnt + 1
            current = current.myNext
            cnt = cnt + 1
        return -1