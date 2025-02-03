import time

def search_time(lst, target):
    start = time.perf_counter_ns()
    for item in lst:
        if item == target:
            break
    end = time.perf_counter_ns()
    return end - start

def binary_search(lst, target):
    start = time.perf_counter_ns()
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            end = time.perf_counter_ns()
            return end - start
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    end = time.perf_counter_ns()
    return end - start

def set_search(s, target):
    start = time.perf_counter_ns()
    s = set(lst)
    found = target in s
    end = time.perf_counter_ns()
    return end - start

def direct_search(s, target):
    start = time.perf_counter_ns()
    x = target in s      
    end = time.perf_counter_ns()
    return end - start

lst = [i for i in range(1, 101)]  
target = 87

linear_time = search_time(lst, target)
binary_time = binary_search(lst, target)
set_time = set_search(lst, target)
direct_search_time = direct_search(lst, target)

print()
print(f"Time to iterate: {linear_time} nanoseconds")
print(f"Time for binary search: {binary_time} nanoseconds")
print(f"Time for set lookup: {set_time} nanoseconds")
print(f"Time for direct search: {direct_search_time} nanoseconds")
print()



