def merge_sort(string):
    if len(string) <= 1:
        return string or ''

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
    first_string_lower = first_string.lower()
    second_string_lower = second_string.lower()

    first_string_sorted = merge_sort(first_string_lower)
    second_string_sorted = merge_sort(second_string_lower)

    if first_string == '' or second_string == '':
        return (first_string_sorted, second_string_sorted, False)

    return (
        first_string_sorted,
        second_string_sorted,
        first_string_sorted == second_string_sorted
        )
