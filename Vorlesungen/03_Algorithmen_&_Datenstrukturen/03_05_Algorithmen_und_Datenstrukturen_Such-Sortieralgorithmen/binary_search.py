#%%
def binary_search_recursive(arr, x, low, high):
    """
    Uses binary search to find x in arr. Requires arr to be sorted!
    Time Complexity: O(log n)
    Space Complexity: O(log n) --> for all the created stack frames
    """
    if high >= low:
        mid = (high + low) // 2 #integer division as mid will be index
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            # if the middle element is larger than x
            # we need to look in the lower half of the array
            return binary_search_recursive(arr, x, low, mid - 1)
        else:
            # if the middle element is lower than x
            # we need to look in the upper half of the array
            return binary_search_recursive(arr, x, mid + 1, high)
    else:
        # we have converged with our values for low and high
        return None


#%%


def binary_search_iterative(arr, x):
     """
     Uses binary search to find x in arr. Requires arr to be sorted!
     Time Complexity: O(log n)
     Space Complexity: O(1)
     """
     low = 0
     high = len(arr) - 1

     while low <= high:
         mid = (high + low) // 2 #integer division as mid will be index

         if arr[mid] > x:
             # if the middle element is larger than x
             # we need to look in the lower half of the array by reducing "high"
             high = mid - 1
         elif arr[mid] < x:
             # if the middle element is lower than x
             # we need to look in the upper half of the array by increasing "low"
             low = mid + 1
         else:
             return mid

     return None

#%%

a_list = [1, 3, 8, 16, 25, 46, 94]
element = 25

print(binary_search_recursive(a_list, element, 0, len(a_list) - 1))

#%%

print(binary_search_iterative(a_list, element))