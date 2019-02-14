import connection
import util

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
            for key, value in form_data.items():
                if key == "submission_time":
                    old_data["rows"][i][key] = util.make_timestamp()
                    continue
                old_data["rows"][i][key] = value

    connection.write_data_to_file(path, old_data, "w")


def add_new_row(path, data):
    connection.write_data_to_file(path, data, mode='a')