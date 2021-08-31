def quickSort(arr, l, h):
    if l < h:
        pi = partition(arr, l, h)
        quickSort(arr, l, pi-1)
        quickSort(arr, pi+1, h)
    return arr



def partition(arr, l, h):
    i = l - 1
    marker = arr[h]
    for j in range(l,h):
        if arr[j] <= marker:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[h] = arr[h], arr[i+1]
    return (i+1)


list=[2,4,9,33,10,22]
print(quickSort(list,0,5))
