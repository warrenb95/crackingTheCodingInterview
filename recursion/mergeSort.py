def mergeSort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]

        mergeSort(leftarr)
        mergeSort(rightarr)

        i = j = k = 0

        while len(leftarr) > i and len(rightarr) > j:
            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i +=1
            else:
                dataset[k] = rightarr[j]
                j += 1
            k += 1

        while len(leftarr) > i:
            dataset[k] = leftarr[i]
            i += 1
            k += 1

        while len(rightarr) > i:
            dataset[k] = rightarr[j]
            j += 1
            k += 1

        return dataset

print(mergeSort([1,3,2,4]))