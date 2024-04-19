class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def printLinkedList(head):
        curr=head
        while curr!=None:
            print(curr.data,end="-->")
            curr=curr.next
        print(None)

def insertAtEndOfTail(head, ele):
    newBlock=Node(ele)
    if head==None: 
        return newBlock
    curr=head
    while curr.next!=None:
        curr=curr.next
    curr.next=newBlock
    return head
def delAtSpecificPosition(head,position):

    curr=head
    index=1
    while index!=position-1:
        curr=curr.next
        index+=1
    mainNode=curr.next
    nextNode=mainNode.next
    mainNode.next=None
    curr.next=None
    curr.next=nextNode
    return head

l=[11,22,33,44,55,66,77,88,99,110]
head=None
for ele in l:
    head=insertAtEndOfTail(head, ele)

head=delAtSpecificPosition(head,2)
printLinkedList(head)







