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

def insertAtHeadOfLinkedlist(head, ele):
    newBlock=Node(ele)
    if head==None:
        return newBlock
    newBlock.next=head
    return newBlock
l=[11,22,33,44,55,66,77,88,99,110]
head=None
for ele in l:
   head=insertAtHeadOfLinkedlist(head, ele)
printLinkedList(head)
