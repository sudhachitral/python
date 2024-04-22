nums=[12, 34, 2, 56, 90, 33, 89, 120, 20]
nums=sorted(nums)


target=34

left=0
right=len(nums)
found =False

while left <= right:
    mid=(left+right)//2
    if nums[mid]==target:
        print("found element in list")
        found=True
        break
    elif nums[mid]>target:
        right=mid-1
    else:
        left=mid+1
    print("Not found")
if found==True:
    print("element is found in the list")
else:
    print("element is not found in list")
