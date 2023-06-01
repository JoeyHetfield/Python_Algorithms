def is_anagram(first_string, second_string):
    if first_string == '' or second_string == '':
        return False
    
    first_string = first_string.lower()
    second_string = second_string.lower()

    if len(first_string) != len(second_string):
        return False
    
