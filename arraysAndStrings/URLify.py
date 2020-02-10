'''
    URLify: Write a method to replace all spaces in a string with
    '%20'. You may assume that the string has sufficient space to 
    hold the additional characters, and that you are given the 
    length of the string.
'''

def urlify(string, string_len):
    return string.strip().replace(' ',  '%20')

# This is the correct ans
def replace_spaces(string, true_len):
    num_of_spaces = string.count(' ', 0, true_len)
    new_index = true_len - 1 + num_of_spaces * 2

    if new_index + 1 < len(string):
        string[new_index] = '\0'
    for old_index in range(true_len - 1, 0, -1):
        if string[old_index] == ' ':
            string[new_index] = '0'
            string[new_index - 1] = '2'
            string[new_index - 2] = '%'

            new_index -= 3
        else:
            string[new_index] = string[old_index] # does not work in python
            new_index -= 1

    return string

output = urlify('Mr John Smith    ', 13)
assert output == 'Mr%20John%20Smith', 'urlify returned incorrect ans! ' + output 