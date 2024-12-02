def lin_search(a_list, x):
     return x in a_list

def binary_search(arr, x, low, high):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] > x:
            return binary_search(arr, x, low, mid - 1)
        else:
            return binary_search(arr, x, mid + 1, high)
    else:
        return False

a_list = [1, 3, 8, 16, 25, 46, 94]
print(lin_search(a_list, 25))
print(binary_search(a_list, 25, 0, 6))