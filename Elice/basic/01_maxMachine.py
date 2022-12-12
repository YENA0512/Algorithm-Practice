'''
maxMachine 클래스를 완성하세요
'''
class maxMachine :
    def __init__(self):
        self.numbers = []
    def addNmuber(self,n):
        self.numbers.append(n)
    def removeNumber(self,n):
        self.numbers.remove(n)
    def getMax(self):
        return max(self.numbers)

def sorting(myList) :
    '''
    myList를 내림차순으로 정렬하여 반환하는 함수를 작성하세요.

    예를 들어, myList = [5, 2, 3, 1] 이라면 [5, 3, 2, 1] 을 반환해야 합니다.

    단, maxMachine class를 이용하도록 합니다. 
    '''

    myMachine = maxMachine()
    result = []

    for x in myList:
        myMachine.addNumber(x)
    
    for i in range(len(myList)) :
        myMax = myMachine.getMax()

        result.append(myMax)

        myMachine.removeNumber(myMax)

    return result