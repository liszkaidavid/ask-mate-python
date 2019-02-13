import connection


def read_to_dict():
    reader = connection.get_data_from_file()
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