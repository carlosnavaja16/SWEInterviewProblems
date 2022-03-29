def zeroMatrix(matrix: list[list[int]]) -> list[list[int]]:

    height = len(matrix)
    width = len(matrix[0])

    rows = set()
    columns = set()

    for i in range(height):
        for j in range(width):
            if matrix[i][j] == 0:
                rows.add(i)
                columns.add(j)
    for i in range(height):
        for j in range(width):
            if i in rows or j in columns:
                matrix[i][j] = 0
    return matrix