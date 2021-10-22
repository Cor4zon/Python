grid = [[0, 0, 0],
        [0, 0, 0]]

num_row = 2
num_col = 3
grid = []

for _ in range(num_row):
        row = []
        for _ in range(num_col):
                row.append(0)
        grid.append(row)

print(grid)

grid = [[0 for _ in range(num_col)] for _ in range(num_row)]
print(grid)
