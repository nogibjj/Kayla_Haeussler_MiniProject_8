from mylib.find_average import find_average, calculate_time_memory


def append_to_md_file(
    file_name: str, result: float, duration: float, memory: float
) -> None:
    """
    Append the integration result and elapsed time to a markdown file.
    """
    with open(file_name, "a") as file:
        file.write("\n## Integration Result\n")
        file.write(f"- Result: {result:.5f}\n")
        file.write(f"- Time taken: {duration:.5f} microseconds\n\n")
        file.write(f"- Memory used: {memory: .2f} kilobytes\n\n")

    print(f"Content appended to {file_name} successfully!")


data_path = "data/candy-data.csv"

if __name__ == "__main__":
    data_path = "data/candy-data.csv"  # Updated with the actual CSV file path

    avg_try = find_average(data_path)
    print(f"Average weight: {avg_try:.5}")

    end_mem_usage, elapsed_time = calculate_time_memory(data_path)
    append_to_md_file("python_times.md", avg_try, elapsed_time, end_mem_usage)
    print(f"Final Memory Usage: {end_mem_usage} kilobytes")
    print(f"Total Elapsed Time: {elapsed_time:.7} seconds")
