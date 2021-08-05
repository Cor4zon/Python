from typing import List


def maxIncreaseKeepingSkyline(grid: List[List[int]]) -> int:
    maxRow = [grid[i][0] for i in range(len(grid))]
    maxCol = [j for j in grid[0]]

    print(maxRow)
    print(maxCol)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] > maxRow[i]:
                maxRow[i] = grid[i][j]
                maxCol[j] = grid[i][j]

    for i in grid:
        print(i)
    print()

    print(maxRow)
    print(maxCol)


maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3]])