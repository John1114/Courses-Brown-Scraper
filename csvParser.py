import csv
import re
import string


def useRegexToFindPreReqs(input):
    pattern = re.compile(r"[a-zA-Z]+\\[a-zA-Z]{2}[0-9]{5}")
    return pattern.search(input, re.IGNORECASE)


def useRegexToFilterPreReqs(input):
    pattern = re.compile('(.*?)')
    return pattern.search(input, re.IGNORECASE)


with open('courses.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_writer = csv.writer(csv_file)
    line_count = 0
    out = ""
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            temp = useRegexToFindPreReqs(row[6])
            if temp is not None:
                out += temp.group(0)
            line_count += 1
            print(out)
            out = ""
