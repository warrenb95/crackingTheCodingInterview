def checkPermutation(s1, s2):
    if len(s1) != len(s2):
        return False

    n = len(s1)
    d1 = dict()
    d2 = dict()

    for i in range(n):
        if s1[i] not in d1.keys():
            d1[s1[i]] = 1
        else:
            d1[s1[i]] += 1

        if s2[i] not in d2.keys():
            d2[s2[i]] = 1
        else:
            d2[s2[i]] += 1

    # print(f'{d1}\n{d2}')

    if len(d1.keys()) != len(d2.keys()):
        return False

    for key in d1.keys():
        if key not in d2.keys():
            return False
        else:
            if d1[key] != d2[key]:
                return False

    return True

print(checkPermutation('abcabcabcabcabcabcabcabcabcabcabcabc', 'cbacbacbacbacbacbacbacbacbgacbacbacba'))
print(checkPermutation('bc', 'cba'))
print(checkPermutation('ab', 'ac'))