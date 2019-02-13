import csv
# todo : read question csv file
# todo : write question csv file

# todo : read answer csv file
# todo : write answer csv file

DATA_FILE_PATH = "sample_data/question.csv"


def get_data_from_file():
    with open(DATA_FILE_PATH, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        rows = [row for row in reader]
        return rows
