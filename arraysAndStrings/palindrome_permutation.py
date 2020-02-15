def palindrome_permutation(string):
    string = string.strip()

    char_counter = {}
    for char in string:
        if char == ' ':
            continue

        if char in char_counter.keys():
            char_counter[char] += 1
        else:
            char_counter[char] = 1
    
    odd_flag = False

    for val in char_counter.values():
        if val % 2 != 0:
            if odd_flag == True:
                return False
            else:
                odd_flag = True
    
    return True

output = palindrome_permutation('rracecarr')
print(output)