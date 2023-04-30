# Exercise 06

# 1

def power(a, b) -> int:
    # BASE CASE
    if a <= 0 or b <= 0:
        return -1
    elif b == 1:
        return a
    # Recursion
    else:
        return a * power(a, b-1)


result = power(2, 4)
print(result)


# 2

def binary_search(numbers, num):

    # Base Case
    if not numbers:
        return -1

    # find midpoint index and value
    mid = len(numbers) // 2
    mid_val = numbers[mid]

    # if element is found
    if mid_val == num:
        return mid

    # Check if search element is smaller than midpoint value and search left half
    elif num < mid_val:
        return binary_search(numbers[:mid], num)

    # Check if search element is greater than midpoint value and search right half
    else:
        result = binary_search(numbers[mid+1:], num)
        return mid + 1 + result if result != -1 else -1


numbers = [1, 2, 4, 5, 7, 9, 11]
num = 9
index = binary_search(numbers, num)
print(index)
