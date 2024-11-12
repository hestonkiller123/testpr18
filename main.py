def bubble_sort(arr):
    n = len(arr)
    # Проходим по всему массиву
    for i in range(n):
        # Последние i элементов уже на своих местах
        for j in range(0, n - i - 1):
            # Меняем элементы местами, если текущий больше следующего
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Пример использования
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Отсортированный массив:", sorted_arr)