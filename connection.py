import csv
# todo : read question csv file
# todo : write question csv file

# todo : read answer csv file
# todo : write answer csv file

DATA_FILE_PATH = "sample_data/question.csv"


def get_data_from_file():
    with open(DATA_FILE_PATH, "r") as csv_file:
        reader = csv.DictReader(csv_file)
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
