def merge_sort(string):
    if len(string) <= 1:
        return string

    mid = len(string) // 2
    left = merge_sort(string[:mid])
    right = merge_sort(string[mid:])

    return merge(left, right)


def merge(left, right):
    merged = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return ''.join(merged)


def is_anagram(first_string, second_string):
    if first_string == '' or second_string == '':
        return (merge_sort(first_string), merge_sort(second_string), False)

    first_string = first_string.lower()
    second_string = second_string.lower()

    first_string = merge_sort(first_string)
    second_string = merge_sort(second_string)

    return (first_string, second_string, first_string == second_string)
