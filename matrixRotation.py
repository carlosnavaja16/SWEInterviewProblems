def rotate(self, matrix: List[List[int]]) -> None:
    size = len(matrix)

    left = 0
    right = size - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right

            temp = matrix[top][left + i]
            matrix[top][left + i] = matrix[bottom - i][left]
            matrix[bottom - i][left] = matrix[bottom][right - i]
            matrix[bottom][right - i] = matrix[top + i][right]
            matrix[top + i][right] = temp
        left += 1
        right -= 1
        
    return matrix