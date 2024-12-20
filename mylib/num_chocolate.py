import pandas as pd
import time
import psutil


def num_chocolate(file_path):
    df = pd.read_csv(file_path)
    num_chocolate = df["chocolate"].sum()
    return num_chocolate


def calculate_time_memory(path):
    # Record the start time
    start_time = time.time()

    # Measure the initial memory usage
    process = psutil.Process()  # Get current process
    start_mem_usage = process.memory_info().rss  # Memory usage in bytes

    # find number of candies containing chocolate
    num_chocolate(path)

    # Record the end time
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    # Measure the final memory usage
    end_mem_usage = process.memory_info().rss  # Memory usage in bytes

    # Convert memory usage from bytes to kilobytes
    memory_usage_change = (end_mem_usage - start_mem_usage) / 1024

    print(f"Python-Elapsed Time: {elapsed_time:.7f} seconds")
    print(f"Python-Memory Usage Change: {memory_usage_change:.2f} kilobytes")

    return end_mem_usage, elapsed_time
