'''
getHeight 함수를 작성하세요.
'''

def getHeight(myTree) :
    '''
    myTree의 높이를 반환하는 함수를 작성하세요.
    '''
    if myTree == None :
        return 0
    else :
        return 1 + max(getHeight(myTree.left),getHeight(myTree.right))
    return 0