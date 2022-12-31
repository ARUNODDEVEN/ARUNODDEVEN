def bubble_sort(list):
    for i in range(0, len(list)-1):
        for j in range(0, len(list)-1-i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

    return list


l = bubble_sort([12, 43, 7, 57, 78])
print(l)
