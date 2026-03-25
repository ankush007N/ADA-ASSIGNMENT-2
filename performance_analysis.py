import time
import matplotlib.pyplot as plt
import numpy as np

# Sorting Algorithms

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the elements into 2 halves
        R = arr[mid:]  

        merge_sort(L)  # Sorting the first half
        merge_sort(R)  # Sorting the second half

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Quick Sort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Timing function

def time_algorithm(algorithm, data):
    start_time = time.time()
    algorithm(data)
    return time.time() - start_time

# Performance analysis

def performance_analysis():
    input_sizes = [100, 1000, 10000, 100000, 1000000]
    merge_sort_times = []
    quick_sort_times = []

    for size in input_sizes:
        data = np.random.randint(0, 1000000, size).tolist()
        merge_sort_times.append(time_algorithm(merge_sort, data.copy()))
        quick_sort_times.append(time_algorithm(quick_sort, data.copy()))

    plt.figure(figsize=(10,5))
    plt.plot(input_sizes, merge_sort_times, label='Merge Sort', marker='o')
    plt.plot(input_sizes, quick_sort_times, label='Quick Sort', marker='o')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Input Size')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Algorithms Performance')
    plt.legend()
    plt.savefig('plots/sorting_performance.png')
    plt.clf()

performance_analysis()