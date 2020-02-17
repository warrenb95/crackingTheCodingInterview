'''
Q1 - String has all unique characters?
'''

# My Solution
def isUnique(s):
    if len(s) < 1: return False
    if len(s) == 1: return True

    sDict = {}

    # O(s)
    for c in s:
        if c not in sDict.keys():
            sDict[c] = 1
        else:
            return False

    return True

if __name__ == "__main__":
    print(isUnique('a'))
    print(isUnique('aa'))
    print(isUnique('qwertyui'))