def linear_search(nums: list[int], x: int) -> int:
    """Индекс первого вхождения x или -1.
 
    linear_search([4, 2, 7, 2], 2) -> 1
    linear_search([4, 2, 7, 2], 9) -> -1
    linear_search([], 1) -> -1
    """
    for i in range(len(nums)):
        if nums[i]==x:
            return i
    return -1

def binary_search(sorted_nums: list[int], x: int) -> int:
    """
    Индекс x в отсортированном по возрастанию списке или -1
    На неотсортированном списке результат не определён.
    Возвращает индекс найденного элемента или -1, если элемент отсутствует.

    binary_search([1, 3, 5, 7], 5) -> 2
    binary_search([1, 3, 5, 7], 4) -> -1
    binary_search([5], 5) -> 0
    binary_search([], 5) -> -1
    """
    lo=0
    hi=len(sorted_nums)-1
    while lo<=hi:
        mid=(lo+hi)//2
        if sorted_nums[mid]==x:
            return mid
        elif sorted_nums[mid]<x:
            lo=mid+1
        else:
            hi=mid-1
    return -1

def two_sum_brute(nums, target):
    """Пара индексов (i, j), i < j, nums[i] + nums[j] == target, или None.
 
    two_sum_brute([2, 7, 11, 15], 9) -> (0, 1)
    two_sum_brute([1, 2], 10) -> None
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)

    return None

def two_sum_fast(nums: list[int], target: int) -> tuple[int, int] | None:
    """То же, что two_sum_brute, но за один проход со словарём 

    two_sum_fast([2, 7, 11, 15], 9) -> (0, 1)
    """
    seen = {}       # значение -> его индекс
    for i, x in enumerate(nums):
        need = target - x 
        if need in seen:
            return (seen[need], i)
        seen[x] = i
    return None


