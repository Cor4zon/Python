from typing import List


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                self.rectangle[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]


obj = SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]])
print(obj.rectangle)

param_2 = obj.getValue(0, 2)
print(param_2)

obj.updateSubrectangle(0,0,3,2,5)
print(obj.rectangle)

param_2 = obj.getValue(0, 2)
print(param_2)
param_2 = obj.getValue(3, 1)
print(param_2)
print(obj.rectangle)

obj.updateSubrectangle(3,0,3,2,10)
print(obj.rectangle)

param_2 = obj.getValue(3, 1)
print(param_2)
param_2 = obj.getValue(0, 2)
print(param_2)


# ["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue","getValue"]
# [0,2],[0,0,3,2,5],[0,2],[3,1],[3,0,3,2,10],[3,1],[0,2]]