# -*- coding: utf-8 -*-


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


def compute_street(street):
    quick_name = [
        'ул.',
        'пр.',
        'пер.',
        'наб.',
        'ш.',
        'дор.',
        'бульв.',
        'пл.'
    ]
    full_name = [
        'улица',
        'проспект',
        'переулок',
        'набережная',
        'шоссе',
        'дорога',
        'бульвар',
        'площадь'
    ]
    street = street.replace(',', '')
    for i in range(len(quick_name)):
        if quick_name[i] in street.lower():
            street = street.replace(quick_name[i], full_name[i])
    for j in range(len(full_name)):
        if street.find(full_name[j]) == len(street) - len(full_name[j]) & street.find(full_name[j]) >= 0:
                street = street.replace(full_name[j], '')
                street = street + ' ' + full_name[j] 
    street = street.strip()
    street = street.replace('  ', ' ')
    print (street)
    return street


# main
address = {}
polygon = {}
reader = csv.reader(open('live.csv'), delimiter=':')
for row in reader:
    key = compute_street(row[2])
    if key not in address:
        address[key] = []
    address[key].append(row[3:])
reader = csv.reader(open('polygon.csv'), delimiter=':')
for row in reader:
    key = compute_street(row[4])
    if key not in polygon:
        polygon[key] = []
    polygon[key].append(row[0:])

# live.csv
# polygon.csv

