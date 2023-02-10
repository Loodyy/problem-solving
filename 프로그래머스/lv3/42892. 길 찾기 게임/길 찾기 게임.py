import sys
sys.setrecursionlimit(int(1e5))

class Node:
    def __init__(self, x, y, idx):
        self.x = x
        self.y = y
        self.idx = idx
        self.left = None
        self.right = None

class BST:
    def __init__(self, srcNode: Node):
        self.root = srcNode
        
    def insert(self, newNode: Node) -> None:
        comp = self.root
        while True:
            x = newNode.x
            if x < comp.x:
                if comp.left == None:
                    comp.left = newNode
                    break
                comp = comp.left
            else:
                if comp.right == None:
                    comp.right = newNode
                    break
                comp = comp.right
    
    def preorder(self, node: Node, res: list):
        if node == None:
            return res
        res.append(node.idx)
        self.preorder(node.left, res)
        self.preorder(node.right, res)
        return res
        
    def postorder(self, node: Node, res: list):
        if node == None:
            return res
        self.postorder(node.left, res)
        self.postorder(node.right, res)
        res.append(node.idx)
        return res

def solution(nodeinfo): 
    nodeList = []
    for i, node in enumerate(nodeinfo):
        x, y = node
        nodeList.append(Node(x, y, i + 1))

    nodeList.sort(key = lambda n: -n.y)
    srcNode = nodeList.pop(0)
    
    bst = BST(srcNode)
    for node in nodeList:
        bst.insert(node)
            
    return [bst.preorder(bst.root, []), bst.postorder(bst.root, [])]