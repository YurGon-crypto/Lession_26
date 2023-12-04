def binary_search_recursive(arr, target, low, high):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_recursive(arr, target, mid + 1, high)
        else:
            return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
print(f"Елемент {target} знайдений на позиції {result}" if result != -1 else "Елемент не знайдений")
