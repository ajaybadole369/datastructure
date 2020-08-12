def selection_sort(list_):
    for i in range(len(list_)):
        min_li = i
        for j in range(i + 1, len(list_)):
            if list_[min_li] > list_[j]:
                min_li = j
        list_[i], list_[min_li] = list_[min_li], list_[i]


list_ = [2, 3, 22, 24, 12, 33, 53, 6]
selection_sort(list_)
print(list_)
