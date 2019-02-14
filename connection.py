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
        fieldnames = data_to_write.keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if data_to_write is not list:
            writer.writerow(data_to_write)
        else:
            for row in data_to_write:
                writer.writerow(data_to_write)

