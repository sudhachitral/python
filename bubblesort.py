def performBubbleSort(nums):
    n=len(nums)
    for fixThisIndex in range(n - 1, 0, -1):
         for index in range(fixThisIndex):
            if nums[index]>nums[index+1]:
                temp=nums[index]
                nums[index]=nums[index+1]
                nums[index+1]=temp
         print(nums)

   



nums=[12, 2, 34, 20, 56, 43, 45, 100, 89, 50]
print("before sorting:")
print(nums)
#logic to perform sorting
performBubbleSort(nums)
print("after sorting:")
print(nums)

