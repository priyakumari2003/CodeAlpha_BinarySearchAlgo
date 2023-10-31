def binary_search(arr, target):
    left = 0  # Initialize the left pointer to the start of the array
    right = len(arr) - 1  # Initialize the right pointer to the end of the array

    while left <= right:
        mid = (left + right) // 2  # Calculate the middle index

        if arr[mid] == target:
            return mid  # The target element is found, return its index
        elif arr[mid] < target:
            left = mid + 1  # If the middle element is less than the target, search the right half
        else:
            right = mid - 1  # If the middle element is greater than the target, search the left half

    return -1  # If the target element is not in the array, return -1

# Example usage:
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 15
result = binary_search(arr, target)
if result != -1:
    print(f"Element {target} is at index {result}")
else:
    print(f"Element {target} is not in the array")
