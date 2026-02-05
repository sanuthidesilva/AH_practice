def insertion(list_1):

    for i in range(1, len(list_1)):
        value = list_1[i]
        index = i

        while (index > 0) and (value < list_1[index-1]):
            list_1[index] = list_1[index - 1]
            index = index - 1

        list_1[index] = value

    return list_1
