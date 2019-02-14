import csv
# todo : read question csv file
# todo : write question csv file

# todo : read answer csv file
# todo : write answer csv file

DATA_FILE_PATH = "sample_data/question.csv"


def get_data_from_file(path):
    with open(path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        rows = [row for row in reader]
        return rows


def write_data_to_file(path, data_to_write, mode):
    with open(path, mode) as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data_to_write["headers"])
        writer.writeheader()
        for row in data_to_write["rows"]:
            writer.writerow(row)


