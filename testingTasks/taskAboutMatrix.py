def get_rows_sum(matrix):
    result = []
    for i in matrix:
        result.append(sum(matrix[i]))

    return result

def get_cols_sum(matrix):
    result = [0] * len(matrix[0])
    for i in range(matrix):
        for j in range(matrix[0]):
            result[j] += matrix[i][j]
    return result


def solve (A, queries):
    # Type your code here
    rows_sum = get_rows_sum(A)
    cols_sum = get_cols_sum(A)
    result_list = []

    for i in queries:
        result = 0
        for j in range(rows_sum):
            if queries[i][0] <= rows_sum[i] <= queries[i][1]:
                result += 1

        for k in range(cols_sum):
            if queries[j][0] <= cols_sum[i] <= queries[j][1]:
                result += 1
        result_list.append(result)

    print(result_list)
    return result_list


N = int(input())
M = int(input())
A = []
queries = []

for i in range(N):
    A.append(list(map(int, input().split())))

queries_num = int(input())
# why????
assert input() == '2'

for i in range(queries_num):
    queries.append(tuple(map(int, input().split())))

out_ = solve(A, queries)
print(*out_)

