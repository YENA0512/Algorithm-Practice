'''
preorder, inorder, postorder 함수를 구현하세요.
'''

def preorder(tree) :
    '''
    tree를 전위순회 하여 리스트로 반환하는 함수를 작성하세요.
    '''
    #순회를 한 결과를 방문한 노드들을 순서대로 담고 있는 리스트
    # Result에 값을 추가한다 = 현재 노드 방문 
    result = []
    result.append(tree.index)
    # root node + left side + right side
    if tree.left != None :
        result = result + preorder(tree.left)
    if tree.right != None :
        result = result + preorder(tree.right)
    return result

def inorder(tree) :
    '''
    tree를 중위순회 하여 리스트로 반환하는 함수를 작성하세요.
    '''
    result = []

    # left side + root node + right side
    if tree.left != None :
        result = result + inorder(tree.left)
    result.append(tree.index)
    if tree.right != None :
        result = result + inorder(tree.right)
    return result

def postorder(tree) :
    '''
    tree를 후위순회 하여 리스트로 반환하는 함수를 작성하세요.
    '''
    result = []
    # left side + root node + right side
    if tree.left != None :
        result = result + postorder(tree.left)
    if tree.right != None :
        result = result + postorder(tree.right)
    result.append(tree.index)
    return result