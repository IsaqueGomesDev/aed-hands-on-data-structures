from src.my_array import MyArray


def binary_search(array: MyArray, target: int) -> int:
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left+right)//2
        value = array[mid]

        if value == target:
            return mid
        elif value > target:
            right = mid-1
        else:
            left = mid+1
            
    return -1