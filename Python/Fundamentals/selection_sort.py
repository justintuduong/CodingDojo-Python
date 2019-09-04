li = [8,7,6,5,4,3,2,1,0]

def selection_sort(li):
    for i in range(0, len(li) -1):
        min = i
        for j in range(i+1, len(li)):
            if li[j] < li[min]:
                min = j
        if min != i:
            li[i], li[min] = li[min], li[i]
    return li
print(selection_sort(li))


