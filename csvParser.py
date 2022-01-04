import csv
import re


def useRegex(input):
    pattern = re.compile(r"[a-zA-Z]+\\[a-zA-Z]{2}[0-9]{5}")
    return pattern.search(input, re.IGNORECASE)


with open('courses.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            temp = useRegex(row[6])
            if temp is not None:
                print(temp)
            line_count += 1
