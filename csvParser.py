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
    writableFile = open('courses2.csv', "w")
    csv_writer = csv.writer(writableFile)
    line_count = 0
    out = ""
    out_list = []
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            temp = useRegexToFindPreReqs(row[6])
            if temp is not None:
                out += temp.group(0)
            row[4] = out
            csv_writer.writerow(row)
            line_count += 1
            out_list.append(out)
            print(out)
            out = ""
