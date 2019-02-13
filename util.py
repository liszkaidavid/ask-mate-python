import time
from datetime import datetime
# todo timestamp + format


def make_timestamp():
    timestamp = time.time()
    return int(timestamp)



def make_timestamp_readable(timestamp):
    timestamp = datetime.fromtimestamp(timestamp)
    return timestamp