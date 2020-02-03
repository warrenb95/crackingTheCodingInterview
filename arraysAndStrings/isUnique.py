from collections import defaultdict

'''
Q1 - String has all unique characters?
'''

# My Solution
def isUnique(s):
    if len(s) <= 1: return True

    sDict = defaultdict()

    # O(s)
    for c in s:
        if sDict[c] > 0:
            return False
        else:
            sDict[c] += 1

if __name__ == "__main__":
    print(isUnique('abcaefg'))