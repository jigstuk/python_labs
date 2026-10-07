def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError
    
    min_num=nums[0]
    max_num=nums[0]
    
    for num in nums:
        if num<min_num:
            min_num=num
        if num>max_num:
            max_num=num
    return (min_num, max_num)

print(min_max([3,-1,5,5,0]))
print(min_max([42,42]))
print(min_max([-5,-2,-9]))
print(min_max([1.5,2,2.0,-3.1]))
print(min_max([]))