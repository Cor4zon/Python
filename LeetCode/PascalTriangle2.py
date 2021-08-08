from typing import List


def getRow(rowIndex: int) -> List[int]:

    triangle = []
    for i in range(rowIndex):
        if i == 0:
            triangle.append([1])
            continue

        current_row = [0] * (i + 1)
        current_row[0], current_row[-1] = 1, 1

        for j in range(1, len(current_row) - 1):
            current_row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(current_row)
    return triangle[rowIndex-1]

print(getRow(5))