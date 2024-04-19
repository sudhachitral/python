class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None


def printLeftToRightManner(head):

    print("left to right")
    curr=head

    while curr!=None:
        print(curr.data,end=" ")
        curr=curr.next
    print()


def printRightLeft(head):
    tail=head
    while tail.next!=None:
        tail=tail.next
    
    curr=tail
    while curr!=None:
        print(curr.data,end=" ") 
        curr=curr.prev   
    print()
     
def addNodeAtTialOfLinkedList(head,val):
    newblock=Node(val)
    if head==None:
        return newblock
    tail=head
    while tail.next!=None:
        tail=tail.next
    tail.next=newblock
    newblock.prev=tail
    return head   
l=[11,22,33,44,55,66,77,88,99,110]
head=None
for ele in l:
     head=addNodeAtTialOfLinkedList(head,ele)
  
printLeftToRightManner(head)
printRightLeft(head)
