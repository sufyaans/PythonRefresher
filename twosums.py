def twoSum( nums, target: int):
    i = 0
    j = len(nums) - 1
    num2 = []
    while i < j:
        x = nums[i] + nums[j]
        if x == target:
            num2.append(nums[i])
            num2.append(nums[j])
            

    return num2

twoSum(nums=[2,1,7,6], target= 8)