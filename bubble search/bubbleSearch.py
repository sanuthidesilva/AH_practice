
def bubble(list_a):
    n = len(list_a)-1
    sorted = False

    while not sorted:
        sorted = True
        swapped = False
        for i in range(0, n):
            if list_a[i] > list_a[i+1]:
                sorted = False

                # list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
                # sorting
                temp = list_a[i]
                list_a[i] = list_a[i+1]
                list_a[i+1] = temp

                swapped = True

        n = n - 1
    return list_a


list1 = [1, 3, 4, 5, 7, 23, 5, 7]

print(bubble(list1))
