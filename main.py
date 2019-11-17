# -*- coding: utf-8 -*-


import csv
import re


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
    street = street.strip()
    for i in range(len(quick_name)):
        if quick_name[i] in street.lower():
            street = street.replace(quick_name[i], full_name[i])
            if street.find(full_name[i]) < len(street) - len(full_name[i]):
                street = street.replace(full_name[i], '')
                street = street + ' ' + full_name[i]
    re.sub('\s+', ' ', street).strip()
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

