class Node:
     def __init__(self,data):
            self.data=data
            self.next=None
     
 
       
       
def enQueue(head,val):
    newblock=Node(val) 
    if head==None:
        return newblock
    tail=head
    while tail.next!=None:
        tail=tail.next
    tail.next=newblock
    return head


def deQueue(head):
    if head==None:
        return None
        print("deleting",head.data)
        secondnode=head.next
        head.next=None
        return secondnode


def printQueue(head):
    if head==None:
        return None
    curr=head
    while curr!=None:
        print(curr.data,end=" ")
        curr=curr.next
    print()
head=None
head = enQueue(head, 10)
head = enQueue(head, 20)
head = enQueue(head, 100)

printQueue(head)
# head=enQueue(head)
# printQueue(head)
# head=deQueue(head)
  #QUEUE SHORTCUT
Q=[]
    print(Q)
    Q.append(10)
    Q.append(20)
    Q.append(30)
    Q.append(40)
    print(Q)
    de=Q.pop(0)
    print(Q)
    de=Q.pop(0)
    print(Q)
    Q.append(999)
    print(Q)
