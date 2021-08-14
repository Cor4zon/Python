from typing import List


def minOperations(boxes: str) -> List[int]:
    result = [0] * len(boxes)
    for i in range(len(boxes)):
        for j in range(len(boxes)):
            if j == i:
                continue
            if boxes[j] != "0":
                result[i] += abs(j - i)

    return result

print(minOperations("110"))
# print(minOperations([0, 0, 1, 0, 1, 1]))
print