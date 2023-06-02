def find_duplicate(nums):
    if not nums or type(nums) == str:
        return False

    counter = counter_numbers(nums)

    for numbers in range(len(nums)):
        if not isinstance(nums[numbers], int) or nums[numbers] < 0:
            return False

    most_found = max(counter, key=counter.get)

    if counter[most_found] > 1:
        return most_found
    else:
        return False


def counter_numbers(nums):
    counter = {}

    for number in nums:
        if number in counter:
            counter[number] += 1
        else:
            counter[number] = 1

    return counter
