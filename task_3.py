import random
import timeit


def insertion_sort(arr: list) -> list:
    arr = arr[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge(left: list, right: list) -> list:
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def merge_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


ALGORITHMS = {
    "insertion": insertion_sort,
    "merge": merge_sort,
    "timsort": sorted,
}

DATASETS = {
    "випадкові": lambda n: random.sample(range(n * 10), n),
    "відсортовані": lambda n: list(range(n)),
    "зворотні": lambda n: list(range(n, 0, -1)),
}

SIZES = [100, 500, 1000, 2000, 5000, 10000, 100000]
SLOW_LIMIT = 5000  # insertion sort O(n^2) пропускаємо для більших масивів


def measure(func, data: list) -> float:
    """Повертає середній час одного виклику в секундах."""
    number = 3 if len(data) <= 2000 else 1
    return timeit.timeit(lambda: func(data), number=number) / number


def main() -> None:
    random.seed(42)

    for data_name, make_data in DATASETS.items():
        print(f"\nНабір даних: {data_name}")
        print(f"{'n':>8} {'insertion':>12} {'merge':>12} {'timsort':>12}")
        for n in SIZES:
            data = make_data(n)
            expected = sorted(data)
            row = [f"{n:>8}"]
            for name, func in ALGORITHMS.items():
                if name == "insertion" and n > SLOW_LIMIT:
                    row.append(f"{'-':>12}")
                    continue
                assert func(data) == expected, f"{name} відсортував невірно"
                row.append(f"{measure(func, data):>12.6f}")
            print(" ".join(row))


if __name__ == "__main__":
    main()
