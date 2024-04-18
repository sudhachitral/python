class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def printLinkedList(head):
        curr=head
        while curr!=None:
            print(curr.data,end="-->")
            curr=curr.next
        print("None")

def insertAtHeadOfLinkedlist(head, ele):
    newBlock=Node(ele)
    if head==None:
        return newBlock
    newBlock.next=head
    return newBlock
def insertAtSpecificPosition(head,position,ele):

    newBlock=Node(ele)
    index=1
    curr=head
    if position==1:
        newBlock.next=head
        return newBlock
    while index!=position-1:
        curr=curr.next
        index+=1
    newBlock.next=curr.next
    curr.next=newBlock
    return head
    
l=[11,22,33,44,55,66,77,88,99,110]
head=None
for ele in l:
    head=insertAtHeadOfLinkedlist(head, ele)

head=insertAtSpecificPosition(head,2,98)
printLinkedList(head)
