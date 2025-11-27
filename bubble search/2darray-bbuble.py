def gradeSorter(list_a):
    temp = 0
    swapped = True
    n = len(list_a) - 1

    while swapped is True:
        swapped = False
        for i in range(0, n):
            if list_a[i] > list_a[i+1]:
                temp = list_a[i]
                list_a[i] = list_a[i + 1]
                list_a[i + 1] = temp
                swapped = True

        n = n - 1
    return list_a


def gradeSorter2d(list_a):
    temp = 0
    swapped = True
    n = len(list_a) - 1

    while swapped is True:
        swapped = False
        for i in range(0, n):
            if list_a[i][1] < list_a[i+1][1]:
                temp = list_a[i]
                list_a[i] = list_a[i + 1]
                list_a[i + 1] = temp
                swapped = True

        n = n - 1
    return list_a


list_1 = []
i = 0
pupil = ""

while pupil != "none":

    pupil = input("what is the users name:\n")
    grade = int(input("enter grade:\n"))
    list_1.append([pupil, grade])

    i = i + 1


# class1 = [pupil1, pupil2, pupil3, pupil4]

print(gradeSorter2d(list_1))
