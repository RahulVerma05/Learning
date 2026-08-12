def transform(legacy_data):
    legacy_data_2 = {}
    for point in legacy_data:
        for letter in legacy_data[point]:
            legacy_data_2[letter.lower()] = point
    return legacy_data_2
