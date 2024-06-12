import time
import random

def linear_search(arr, target):

    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

def main():
    
    # Create a dataset of 1,000,000 values
    dataset = random.sample(range(1, 2000000), 1000000)
    # Prompt user for the value to search
    target = int(input("Enter the value you want to search for: "))   
    # Measure the start time
    start_time = time.time()   
    # Perform linear search
    result_index = linear_search(dataset, target)   
    # Measure the end time
    end_time = time.time()
    # Calculate the time taken for the search
    time_taken = end_time - start_time
    # Output the result
    if result_index != -1:
        print(f"Value {target} found at index {result_index}.")
    else:
        print(f"Value {target} not found in the dataset.")
    # Output the time taken for the search
    print(f"Time taken to search: {time_taken:.6f} seconds")

main()
