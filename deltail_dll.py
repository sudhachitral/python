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
    tail = head 
    while tail.next != None:
        tail = tail.next 
 
    curr = tail
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.prev 
    print()
 


def addNodeAtHeadOfLinkedList(head, val):
    newBlock = Node(val)
    if head == None:
        return newBlock
    newBlock.next = head
    head.prev = newBlock
    return newBlock

     
def delTailnodeInDoublyLinkedKist(head):
    if head==None or head.next==None:
        return None
    curr,previous=head,None
    while curr.next!=None:
        previous=curr
        curr=curr.next
    previous.next=None
    curr.prev=None
    return head
    
l=[11,22,33,44,55,66,77,88,99,110]
head=None
for ele in l:
    head=addNodeAtHeadOfLinkedList(head, ele)
printLeftToRightManner(head)
printRightLeft(head)    

head=delTailnodeInDoublyLinkedKist(head)

printLeftToRightManner(head)
printRightLeft(head)
