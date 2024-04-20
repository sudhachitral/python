

def push(stack,val):
    stack.insert(0,val)
    print(val,"inserted")




def pop(stack):
    if len(stack)==0:
        print("stack is empty,can,t delete anything")
        return
    print(stack[0],"deleted")
    stack.pop(0)
def printstack(stack):
    if len(stack)==0:
        print("stack is empty,nothing to print")
    print(stack)




stack=[]
push(stack,10) 
push(stack,20) 
push(stack,30)
push(stack,40)
push(stack,50)  
printstack(stack)

pop(stack)
printstack(stack)

pop(stack)
printstack(stack)

pop(stack)
printstack(stack)

pop(stack)
printstack(stack)


pop(stack)
printstack(stack)
