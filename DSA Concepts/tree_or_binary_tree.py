#Creating  a simple Tree using a python list

# class TreeNode:
#     def __init__(self,data,child=[]):
#         self.data=data
#         self.child=child
    
    
#     #Just to print a tree
#     def __str__(self, level=0):
#         result=" " * level + str(self.data) + "\n"
#         for child in self.child:
#             result += child.__str__(level + 1)
#         return result
    
#     def addChild(self, Node):
#         self.child.append(Node)
        
        
# tree=TreeNode("Drinks",[])
# hot=TreeNode("Hot",[])
# cold=TreeNode("Cold",[])

# tea=TreeNode("Tea",[])
# coffee=TreeNode("Coffee",[])

# cola=TreeNode("Coke",[])
# maaza=TreeNode("Mango Juice",[])

# tree.addChild(hot)
# tree.addChild(cold)

# hot.addChild(tea)
# hot.addChild(coffee)

# cold.addChild(cola)
# cold.addChild(maaza)

# print(tree)


#Preorder traversal

class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
    
    
newBT=TreeNode("Drinks")
leftchild=TreeNode("Hot")
rightchild=TreeNode("Cold")

newBT.leftchild=leftchild
newBT.rightchild=rightchild

def preOrderTraversal(rootNode):
    if not rootNode: #-------------------------------O(1)
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftchild) #-----------O(n/2)
    preOrderTraversal(rootNode.rightchild) #-----------O(n/2)
    
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftchild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightchild)
    
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftchild)
    postOrderTraversal(rootNode.rightchild)
    print(rootNode.data)
    
preOrderTraversal(newBT)
inOrderTraversal(newBT)
postOrderTraversal(newBT)


#Level Order Traversal





