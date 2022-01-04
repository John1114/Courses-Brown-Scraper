import csv
import re

<<<<<<< HEAD

def useRegex(input):
    pattern = re.compile(r"[a-zA-Z]+\\[a-zA-Z]{2}[0-9]{5}")
    return pattern.search(input, re.IGNORECASE)

=======
def useRegex(input):
    pattern = re.compile(r"[a-zA-Z]+\\[a-zA-Z]{2}[0-9]{5}")
    return pattern.match(input, re.IGNORECASE)
>>>>>>> 0297db78fd20043718f2f66768b7f0182c86f89b

with open('courses.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            temp = useRegex(row[6])
<<<<<<< HEAD
            if temp is not None:
                print(temp)
            line_count += 1
=======
            if temp != None:
                print(temp)
            line_count+=1


>>>>>>> 0297db78fd20043718f2f66768b7f0182c86f89b
