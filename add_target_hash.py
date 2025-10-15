arr = [2, 7, 11, 15]
target = 9
c=0
d={}
for i,num in enumerate(arr):
    c=target-num
    if c in d:
        print(d[c],i)
        break
    d[num]=i
    
