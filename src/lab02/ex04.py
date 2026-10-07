def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat: 
        return []
    n =len(mat[0])
    for row in mat:
        if len(row)!=n:
            raise ValueError
    return [[mat[i][j] for i in range(len(mat))]for j in range(n) ]
print("1:", transpose([[1, 2, 3]]))
print("2:", transpose([[1], [2], [3]]))
print("3:", transpose([[1, 2], [3, 4]]))
print("4:", transpose([]))
print("5:", transpose([[1, 2], [3]]))