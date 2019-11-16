import csv


def read_file(name):
    f = open(name, 'r')
    result = []
    for line in f:
        result.append(line)
    return result


def write_file(name, data):
    f = open(name, 'w')
    f.writelines(data)


# main
address = {}
reader = csv.reader(open('live.csv'), delimiter=':')
for row in reader:
    key = row[2]
    if key not in address:
        address[key] = []
    address[key].append(row[3:])


# live.csv
# polygon.csv

