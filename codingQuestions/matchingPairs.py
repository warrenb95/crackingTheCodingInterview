'''
Take a valid list of positive integers and return the pair of numbers that sum to a target
'''
def matchingPair(arr, target):
    pairDict = {}

    for num in arr:
        t = target - num
        if t in pairDict:
            print(f'{t} and {num}')
            return
        else:
            pairDict.update({num: 1})

    print('No valid pairs')

if __name__ == "__main__":
    arr = [14, 13, 6, 7, 8, 10, 1, 2]
    target = 15

    matchingPair(arr, target)