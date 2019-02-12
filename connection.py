import csv
# todo : read question csv file
# todo : write question csv file

# todo : read answer csv file
# todo : write answer csv file

DATA_FILE_PATH = "sample_data/question.csv"


def get_data_from_file():
    with open(DATA_FILE_PATH, "r") as csv_file:
        dict_reader = csv.DictReader(csv_file)
        headers = []
        rows = []
        for dictionary in dict_reader:
            row = []
            for key, val in dictionary.items():
                if key not in headers:
                    headers.append(key)
                row.append(val)
            rows.append(row)
        return headers, rows