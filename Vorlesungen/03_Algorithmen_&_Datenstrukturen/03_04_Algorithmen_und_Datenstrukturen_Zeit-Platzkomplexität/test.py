from functools import wraps
import time
import random
from collections import Counter

def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'@timeit: {func.__name__} took {(total_time*1e3):.4f} milliseconds')
        #return result, total_time
        return result
    return timeit_wrapper

@timeit
def find_majority_element_efficient(a_list):
    counter = Counter(a_list)
    value, count = counter.most_common(1)[0]
    if count > len(a_list)/2: return value
    return False

my_list = [2, 8, 7, 4, 1, 5, 2, 3, 1, 2, 2]
my_list_2 = [2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]

print(find_majority_element_efficient(my_list))
print(find_majority_element_efficient(my_list_2))