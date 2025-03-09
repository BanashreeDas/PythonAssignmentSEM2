def ThirdSmallest(nums):
    for i in range(0,3):
        smallestIndex=i
        for j in range(i+1,len(nums)):
            if nums[smallestIndex]>nums[j]:
                smallestIndex=j
        nums[i],nums[smallestIndex]=nums[smallestIndex],nums[i]
    return nums[2]
nums = [4, 2, 4, 10,100,5,1]
print(ThirdSmallest(nums))
