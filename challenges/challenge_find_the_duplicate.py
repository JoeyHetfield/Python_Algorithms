def find_duplicate(nums):
    if not nums or type(nums) == str:
        return False

    counter = {}

    nums.sort()

    for numbers in range(len(nums)):
        if nums[numbers] in counter:
            counter[nums[numbers]] += 1
        else:
            counter[nums[numbers]] = 1
        




