from mylib.num_chocolate import num_chocolate, calculate_time_memory

data_path = "./nfl-wide-receivers.csv"


def test_average():
    result = num_chocolate("data/candy-data.csv")
    expected_result = 37

    assert result == expected_result, "Test has failed."


def test_calculate_time_memory():
    result = calculate_time_memory("data/candy-data.csv")

    assert result is not None, "Test has failed."


if __name__ == "__main__":
    test_average()
    test_calculate_time_memory()
