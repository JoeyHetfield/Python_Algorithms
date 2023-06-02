def find_duplicate(nums):
    if not nums or type(nums) == str:
        return False

    nums.sort()
    for i in range(len(nums)):
        if nums[i] == nums[i + 1]:
            return nums[i]
    return False
    
