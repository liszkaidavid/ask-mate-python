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
    old_data = read_to_dict(path)
    for i, row in enumerate(old_data['rows']):
        if row["id"] == form_data["id"]:
            print("BEME")
            old_data["rows"][i] = form_data
    print(old_data["rows"])
    # connection.write_data_to_file()


def add_new_row(data):
    connection.write_data_to_file(data, mode='a')