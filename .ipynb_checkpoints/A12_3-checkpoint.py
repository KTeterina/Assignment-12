def custom_sort(numbers):

    n = len(numbers)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i] # Swap elements if they are in the wrong order
    return numbers

test_list_short = [5, 2, 8, 1, 9]
test_list_long = [12, 4, 7, 1, 10, 9, 3, 5, 8, 2]

print("Original Short List:", test_list_short)
print("Sorted Short List:", custom_sort(test_list_short))

print("\nOriginal Long List:", test_list_long)
print("Sorted Long List:", custom_sort(test_list_long))
