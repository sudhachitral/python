def findPivotIndex(nums,left,right):
    pivot=nums[right]
    #step-1 moving pivot to its actual position
    #step-2 moving all smaller elements than pivot to left side of the pivot
    #step-3 moving all the greater elements to right side of th pivot index

    position=left
    for index in range(left,right):
        if nums[index]<pivot:
            temp=nums[position]
            nums[position]=nums[index]
            nums[index]=temp
            position+=1
    temp=nums[right]
    nums[right]=nums[position]
    nums[position]=temp
    return position


        

def performQuickSort(nums,left,right):
    if left>=right:
        return

    pivotIndex=findPivotIndex(nums,left, right)
        #pivot index
    performQuickSort(nums,left,pivotIndex - 1)
    performQuickSort(nums,pivotIndex + 1,right) 




nums=[10,5,100,50,25,80,110,108]
n=len(nums)

print("before sorting",nums)
 
performQuickSort(nums,0,n-1)

print("After sorting",nums)
