
def binary_search(sequance, Item):
    startPos = 0
    endPos = len(sequance) - 1

    while startPos <= endPos:
        midpoint = startPos + (endPos - startPos)//2
        midpoint_Val = sequance[midpoint]

        if midpoint_Val == Item:
            return midpoint

        elif Item < midpoint_Val:
            endPos = midpoint - 1

        else:
            startPos = midpoint + 1

    return None


sq_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i_1 = 6

print(binary_search(sq_1, i_1))
