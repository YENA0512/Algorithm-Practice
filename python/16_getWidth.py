'''
getWidth 함수를 작성하세요.
'''

def inorder(tree, depth) :
    result = []
    if tree.left != None :
        result += inorder(tree.left, depth+1)
    tree.setDepth(depth)
    result.append(tree)
    if tree.right != None :
        result += inorder(tree.right, depth+1)
    return result
def getWidth(myTree) :
    '''
    myTree의 너비가 가장 넓은 레벨과 그 레벨의 너비를 반환하는 함수를 작성하세요.
    가장 넓은 레벨 l과 그 레벨의 너비 w를 튜플로 반환해야 합니다.
    
    반환값 형식 : (l, w)
    '''

    result = inorder(myTree, 1)
    n = len(result)
    #left[i] = 깊이가 i 인 모든 노드들 중 가장 왼쪽에 있는 노드의 행 
    left = [1001 for i in range(1001)]
    right = [-1 for i in range(1001)]
    maxDepth = 0
    for i in range(n) :
        d = result[i].depth
        left[d] = min(left[d], i)
        right[d] = max(right[d], i)

        maxDepth = max(maxDepth, d)

        ansDepth = 0
        ans = 0
        for i in range(1, maxDepth+1) :
            temp = right[i] - left[i] + 1
            if ans < temp :
                ansDepth = i
                ans = temp 
    return (ansDepth, ans)
   