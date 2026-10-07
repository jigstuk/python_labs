def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    
    n = len(mat[0])
    for row in mat:
        if len(row) != n:
            raise ValueError
    
    return [sum(mat[i][j] for i in range(len(mat))) for j in range(n)]
print("1:",col_sums([[1, 2, 3], [4, 5, 6]]))
print("2:",col_sums([[-1, 1], [10, -10]]))
print("3:",col_sums([[0, 0], [0, 0]]))
print("4:",col_sums([[1, 2], [3]]))