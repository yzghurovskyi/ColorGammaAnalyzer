def calculate_ranges(brightness_data, intervals_count):
    diapason_length = round(1.0 / intervals_count, 3)
    ranges = [0] * intervals_count
    for index in range(len(brightness_data)):
        number_of_diapason = int(brightness_data[index] // diapason_length)
        ranges[number_of_diapason] += 1
    return ranges
