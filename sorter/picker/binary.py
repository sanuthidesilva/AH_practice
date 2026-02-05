def binarySearch(list_1, target):
    low = 0
    high = len(list_1)-1

    while low <= high:
        mid = (high + low)//2

        if target == list_1[mid]:
            return mid + 1
        elif target < list_1[mid]:
            high = mid - 1
        else:
            low = mid + 1
