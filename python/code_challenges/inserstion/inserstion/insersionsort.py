def insertion_sort(list):

    for i in range(1, len(list)):
        key = list[i]
        j = i-1
        while j >=0 and key < list[j] :
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key


list = [8,4,23,42,16,15]
insertion_sort(list)
print ("Sorted listay is:")
for i in range(len(list)):

    print (list[i])
