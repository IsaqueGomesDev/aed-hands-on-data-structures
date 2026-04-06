from src.my_array import MyArray


def linear_search(array: MyArray, target: int) -> int:
    for i in range(0, len(array)):
        if array[i] == target:
            return i
    return -1
