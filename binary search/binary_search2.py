
def bin_search(sequence, item):
    start = 0
    end = len(sequence)

    while start <= end:
        mid = start + (end - start)//2
        midVal = sequence[mid]

        if midVal == item:
            return mid

        elif item < midVal:
            end = mid - 1

        else:
            start = mid + 1

    return None


sq1 = [1, 2, 3, 4, 5, 5, 66, 109, 120]
i1 = int(input("what are you searching for?"))

print(bin_search(sq1, i1))
