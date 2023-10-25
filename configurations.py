import numpy as np
import random
import time
import pandas as pd
import re

def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y %I:%M %p', prop)

example_data = pd.read_csv("example_data.csv", header=None)
print(example_data)

def random_value(index):
    num = np.random.randint(0, 3)
    value = example_data.loc[index, num]
    print(value)
    return value



#def replace_line(line) takes a single string and replaces the value surrounded by %% with the value from the data_index dictionary
def replace_line(line):
    data_index = {
    "pageID": random_value(0),
    "url": random_value(1),
    "pageCategory": random_value(2),
    "productID": np.random.randint(0, 1000000),
    "productName": random_value(3),
    "productCategory": random_value(4),
    "productPrice": np.random.randint(0, 10000),
    "cartID": np.random.randint(0, 1000000),
    "totalItems": np.random.randint(0, 100),
    "totalPrice": np.random.randint(0, 1000000),
    "itemID": np.random.randint(0, 1000000),
    "itemQuantity": np.random.randint(0, 1000),
    "transactionID": np.random.randint(0, 1000000),
    "transactionTotalValue": np.random.randint(0, 1000000),
    "transactionCurrency": random_value(5),
    "eventID": np.random.randint(0, 1000000),
    "eventName": random_value(6),
    "eventGroup": random_value(7),
    "eventTimestamp": random_date("1/1/2022 1:30 PM", "1/1/2023 4:50 AM", random.random()),
    "compnentID": np.random.randint(0, 1000000),
    "componentType": random_value(8),
    "componentLabel": random_value(9),
    "userID": np.random.randint(0, 1000000),
    "userSessionID": np.random.randint(0, 1000000),
    "userDeviceType": random_value(10)
    }
    for key, value in data_index.items():
        line = re.sub(rf"%{key}%", str(value), line)
    return line

def create_new_data(num):
    #create a new file for each iteration
    #write the data to the file
    #close the file
    for i in range(num):
        with open("example_json.txt", "r") as f:
            with open(f"output{np.random.randint(0, 1000)}.txt", "w") as f1:
                np.random.seed(i)
                for line in f:
                    new_line = replace_line(line)
                    f1.write(new_line)
        f.close()
        f1.close()

create_new_data(10)

