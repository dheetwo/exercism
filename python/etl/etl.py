def transform(legacy_data):
    new_dict = {}
    for key in legacy_data:  # value is a list
        for letter in legacy_data[key]:
            new_dict[letter.lower()] = key
    return new_dict