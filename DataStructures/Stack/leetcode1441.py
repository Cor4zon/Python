# Build an Array With Stack Operations
from typing import List


def buildArray(target: List[int], n: int) -> List[str]:
    operations = []
    lst = [i for i in range(1, n+1)]
    while target:
        target_pop = target.pop(0)
        list_pop = lst.pop(0)

        if target_pop == list_pop:
            operations.append("Push")
        else:
            target.insert(0, target_pop)
            operations.append("Push")
            operations.append("Pop")

    return operations
