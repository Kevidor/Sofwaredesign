import time

start_time = time.perf_counter()

sum = 0
for i in range(0, 10000):
    sum += i*i

end_time = time.perf_counter()

delta_time = end_time - start_time
print(f"delta_time = {delta_time * 1e3}")