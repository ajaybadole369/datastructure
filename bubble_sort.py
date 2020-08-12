def bubble_sort(list_):
    for i in range(len(list_)-1,0,-1):
        for j in range(i):
            if list_[j] > list_[j + 1]:
                temp = list_[j]
                list_[j] = list_[j+1]
                list_[j+1] = temp


list_ = [67, 33, 2, 23, 44, 53, 66]
bubble_sort(list_)
print(list_)
