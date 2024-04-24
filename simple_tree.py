class TreeNode:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
root=TreeNode(2)
#root
obj2=TreeNode(7)
obj3=TreeNode(5)
obj4=TreeNode(2)
obj5=TreeNode(6)
#obj6=TreeNode()
obj6=TreeNode(9)
obj7=TreeNode(5)
obj8=TreeNode(11)
obj9=TreeNode(4)

root.left=obj2
root.right=obj3

obj2.left=obj4
obj2.right=obj5

obj3.left=obj6
obj3.right=obj7

obj5.left=obj7
obj5.right=obj8

print(root.data)
print(obj2.data)
print(obj3.data)
print(obj4.data)

print(obj5.data)
print(obj6.data)
print(obj7.data)
print(obj8.data)
print(obj9.data)

