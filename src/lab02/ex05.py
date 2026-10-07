def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    
    n=len(mat[0])
    for row in mat:
        if len(row)!=n:
            raise ValueError
    return [sum(row) for row in mat]
print("1:",row_sums([[1, 2, 3], [4, 5, 6]]))
print("2:",row_sums([[-1, 1], [10, -10]]))
print("3:",row_sums([[0, 0], [0, 0]]))
print("4:",row_sums([[1, 2], [3]]))