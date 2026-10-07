def unique_sorted(nums: list[float | int]) -> list[float | int]:
    unique=list(set(nums))

    n= len(unique)
    for i in range(n):
        for j in range(0,n-i-1):
            if unique[j]>unique[j+1]:
                unique[j],unique[j+1]=unique[j+1],unique[j]
    return unique

print(unique_sorted([3,1,2,1,3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))


