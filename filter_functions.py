def filter_by_keyword(data, keyword):
    filtered_data = []
    for item in data:
        if item[1].contains(keyword) or item[4].contains(keyword):
            filtered_data.append(item)
    return tuple(filtered_data)


def filter_by_location(data, location):
    filtered_data = []
    for item in data:
        if item[3].contains(location):
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