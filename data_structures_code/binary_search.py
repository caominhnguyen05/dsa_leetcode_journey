# Traditional Binary Search - looking if number is in array

# Time: O(log n)
# Space: O(1)

my_list = [-3, -1, 0, 1, 4, 7, 9]

def binary_search(arr, target):
    n = len(arr)
    left = 0
    right = n - 1

    while left <= right:
        mid = left + ((right - left) // 2)
        if arr[mid] == target:
            return True
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return False
print(binary_search(my_list, 6))

# Condition based

B = [False, False, False, False, True]

def binary_search_condition(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid]:
            right = mid
        else:
            left = mid + 1
    return left

print(binary_search_condition(B))

# Range-Based

def guess_number(target, L, R):
    while L <= R:
        M = (L + R) // 2
        if M == target:
            return M  # Found the number
        elif M < target:
            L = M + 1
        else:
            R = M - 1
    return -1  # Target not found


target = 2
result = guess_number(target, 1, 100)
print(f"The guessed number is: {result}")