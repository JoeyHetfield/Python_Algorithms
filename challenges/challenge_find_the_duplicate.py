def find_duplicate(nums):
    if not nums or type(nums) == str:
        return False

    counter = {}

    for numbers in range(len(nums)):
        if nums[numbers] in counter:
            counter[nums[numbers]] += 1
        else:
            counter[nums[numbers]] = 1

    most_found = max(counter, key=counter.get)

    if counter[most_found] > 1:
        return most_found
    else:
        return False
