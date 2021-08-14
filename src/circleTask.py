from typing import List


def isPointInCircle(x, y, xc, yc, r):
    if ((x - xc) ** 2 + (y - yc) ** 2) < (r * r):
        return True
    return False


def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
    result = [0] * len(queries)
    for i in range(len(queries)):
        for j in range(len(points)):
            if isPointInCircle(points[j][0], points[j][1], queries[i][0], queries[i][1], queries[i][2]):
                result[i] += 1

    return result


print(isPointInCircle(3, 1, 4, 4, 3))