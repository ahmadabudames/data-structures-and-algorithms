def marge(arr, start, mid, end):
    num1 = mid - start + 1
    num2 = end - mid
    left = [0] * (num1)
    right = [0] * (num2)



    for i in range(0, num1):
        left[i] = arr[start+i]
    for j in range(0, num2):
        right[j] = arr[mid+1+j]
    i = 0
    j = 0
    k = start
    while i < num1 and j < num2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < num1:
        arr[k] = left[i]
        i += 1
        k += 1
    while j < num2:
        arr[k] = right[j]
        j += 1
        k += 1


def marge_sort(arr, start, end):
    if start < end:
        mid = (start+(end-1))//2
        marge_sort(arr, start, mid)
        marge_sort(arr, mid+1, end)
        marge(arr, start, mid, end)
    return arr



arr=[4,23,55,77,10,200]
print(marge_sort(arr,0,5))


