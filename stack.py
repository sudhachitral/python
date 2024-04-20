class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def push(top,value):
    newblock=Node(value)
    print(value,"is getting inserted")
    if top==None:
        return newblock
    newblock.next=top
    return newblock  


def pop(top):
    if top==None:                             
        print("top is empty")
    print(top.data,"is getting deleted")    
    secondNode=top.next
    top.next=None
    return secondNode


def printStack(top):
    if top==None:
        print("None")
    curr=top
    while curr!=None:
        print(curr.data,end=" ")
        curr=curr.next
    print()

top=None
top=push(top,12)
top=push(top,15)
top=push(top,16)
top=push(top,22)
top=push(top,234)
printStack(top)

top=pop(top)
printStack(top)

top=pop(top)
printStack(top)

top=pop(top)
printStack(top)

top=pop(top)
printStack(top)

top=pop(top)
printStack(top)
