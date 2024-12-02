def quick_sort(a_list, first, last):
   if first<last:
       splitpoint = partition(a_list, first, last)

       quick_sort(a_list, first, splitpoint-1)
       quick_sort(a_list, splitpoint+1, last)


def partition(a_list, first, last):
    pivotvalue = a_list[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and a_list[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while a_list[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            a_list[leftmark], a_list[rightmark] = a_list[rightmark], a_list[leftmark]

    a_list[first], a_list[rightmark] = a_list[rightmark], a_list[first]
    return rightmark

a_list = [16, 8, 25, 3, 1, 94, 46]
quick_sort(a_list, 0, len(a_list)-1)
print(a_list)
