from mylib.find_average import average, calculate_time_memory

data_path = "./nfl-wide-receivers.csv"


def test_average():
    result = find_average("./nfl-wide-receivers.csv")
    expected_result = 935.9090788204381

    assert result == expected_result, "Test has failed."


def test_calculate_time_memory():
    result = calculate_time_memory("./nfl-wide-receivers.csv")

    assert result is not None, "Test has failed."


if __name__ == "__main__":
    test_average()
    test_calculate_time_memory()
