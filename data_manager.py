import connection


def read_to_dict(path):
    reader = connection.get_data_from_file(path)
    header = []
    rows = []
    for row in reader:
        rowdata = dict()
        if not header:
            for title in row:
                header.append(title)
        for key, value in row.items():
            rowdata[key] = value
        rows.append(rowdata)
    data = {"headers": header, "rows": rows}
    return data


def prepare_data_to_write(path, form_data):
    old_data = read_to_dict()
    pass