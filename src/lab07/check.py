import random

from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort

def check_sorting(fn, trials=100):
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = nums.copy()
        result = fn(nums)
        assert result == sorted(nums), f"{fn.__name__} ошиблась на {nums}: {result}"
        assert nums == original, f"{fn.__name__} изменила исходный список"

# Проверяем линейный и бинарный поиск
def check_search(trials=100):
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]

        # Линейный поиск
        if nums:
            x = random.choice(nums)
            assert linear_search(nums, x) == nums.index(x), \
                f"Ошибка линейного поиска: {nums}, x={x}"

        # Проверяем отсутствующее число
        x = 101
        try:
            expected = nums.index(x)
        except ValueError:
            expected = -1

        assert linear_search(nums, x) == expected, \
            f"Ошибка линейного поиска: {nums}, x={x}"

        # Бинарный поиск работает с отсортированным списком
        nums_sorted = sorted(nums)

        # Проверяем первый, последний и случайный элементы
        if nums_sorted:
            for x in (nums_sorted[0], nums_sorted[-1],
                      random.choice(nums_sorted)):
                index = binary_search(nums_sorted, x)

                assert 0 <= index < len(nums_sorted), \
                    f"Неверный индекс: {index}, список: {nums_sorted}, x={x}"

                assert nums_sorted[index] == x, \
                    f"Ошибка бинарного поиска: {nums_sorted}, x={x}"

        # Проверяем отсутствующее число
        assert binary_search(nums_sorted, 101) == -1, \
            f"Ошибка бинарного поиска: {nums_sorted}, x=101"

    # Проверяем крайние случаи
    # assert linear_search([], 5) == -1, "Ошибка на пустом списке"
    # assert binary_search([], 5) == -1, "Ошибка на пустом списке"
    # assert binary_search([5], 5) == 0, "Ошибка на списке [5]"
    # assert binary_search([5], 1) == -1, "Ошибка на списке [5], x=1"




# Проверяем оба алгоритма Two Sum
def check_two_sum(trials=100):
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        target = random.randint(-200, 200)

        res_brute = two_sum_brute(nums, target)
        res_fast = two_sum_fast(nums, target)

        # Если один алгоритм не нашёл пару, второй тоже не должен
        assert (res_brute is None) == (res_fast is None), \
            f"Результаты различаются: {nums}, target={target}"

        # Проверяем правильность найденных пар
        for result in (res_brute, res_fast):
            if result is not None:
                i, j = result

                assert 0 <= i < j < len(nums), \
                    f"Неверные индексы: {nums}, result={result}"

                assert nums[i] + nums[j] == target, \
                    f"Неверная сумма: {nums}, target={target}, result={result}"


if __name__ == "__main__":
    random.seed(42)

    for fn in (bubble_sort, insertion_sort, selection_sort):
        check_sorting(fn)

    check_search()
    check_two_sum()

    print("OK: 500 проверок")