def palindrome_permutation(string):
    string = string.replace(' ', '')
    string  = string.strip()

    char_counter = {}
    for char in string:
        if char in char_counter.keys():
            char_counter[char] += 1
        else:
            char_counter[char] = 1
    
    min_count = min(char_counter.values())
    max_count = max(char_counter.values())

    if max_count != min_count:
        single_min = True
        for val in char_counter.values():
            if val == min_count and single_min == False:
                return False
            else:
                single_min = False
    
    return True

output = palindrome_permutation('tact coa')
assert output == True, 'Oops'