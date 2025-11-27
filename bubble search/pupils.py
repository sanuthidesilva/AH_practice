from dataclasses import dataclass


@dataclass
class pupil:
    name: str
    grade: int


def gradeSorterRecord(records):
    temp = 0
    swapped = True
    n = len(records) - 1

    while swapped is True:
        swapped = False
        for i in range(0, n):
            if records[i].grade < records[i+1].grade:
                temp = records[i]
                records[i] = records[i + 1]
                records[i + 1] = temp
                swapped = True

        n -= 1
    return records
