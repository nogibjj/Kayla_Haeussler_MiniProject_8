from mylib.num_chocolate import num_chocolate, calculate_time_memory


def append_to_md_file(
    file_name: str, result: float, duration: float, memory: float
) -> None:
    """
    Append the result and elapsed time to a markdown file.
    """
    with open(file_name, "a") as file:
        file.write("\n## Number of Chocolate (Python) Result\n")
        file.write(f"- Number of Chocolate Candies: {result}\n")
        file.write(f"- Time taken: {duration:.5f} microseconds\n")
        file.write(f"- Memory used: {memory: .2f} kilobytes\n\n")

    print(f"Content appended to {file_name} successfully!")


data_path = "data/candy-data.csv"

if __name__ == "__main__":
    data_path = "data/candy-data.csv"  # Updated with the actual CSV file path

    number_chocolate = num_chocolate(data_path)
    print(f"Number of Chocolate Candies in our Data: {num_chocolate}")

    end_mem_usage, elapsed_time = calculate_time_memory(data_path)
    append_to_md_file("python_times.md", number_chocolate, elapsed_time, end_mem_usage)
    print(f"Final Memory Usage: {end_mem_usage} kilobytes")
    print(f"Total Elapsed Time: {elapsed_time:.7} seconds")
