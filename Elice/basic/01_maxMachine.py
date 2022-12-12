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