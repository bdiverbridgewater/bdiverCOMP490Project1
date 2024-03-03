def filter_by_keyword(data, keyword):
    filtered_data = []
    for item in data:
        if keyword in item[1] or item[4]:
            filtered_data.append(item)
    return tuple(filtered_data)


def filter_by_location(data, location):
    filtered_data = []
    for item in data:
        if location in item[3]:
            filtered_data.append(item)
    return tuple(filtered_data)


def filter_by_remote(data):
    filtered_data = []
    for item in data:
        if item[6] == 1:
            filtered_data.append(item)
    return tuple(filtered_data)


def filter_by_min_salary(data, salary):
    filtered_data = []
    for item in data:
        if float(item[8]) >= salary:
            filtered_data.append(item)
    return tuple(filtered_data)
