def calculate_ranges(brightness_data: list, intervals_count: int) -> list:
    diapason_length = round(1.0 / intervals_count, 3)
    lst = [0] * intervals_count

    for index in range(len(brightness_data)):
        number_of_diapason = int(brightness_data[index] // diapason_length)
        lst[number_of_diapason] += 1
    return [
        (round(diapason_length * i, 2), round(diapason_length * (i + 1), 2), lst[i])
        for i in range(intervals_count)
    ]
