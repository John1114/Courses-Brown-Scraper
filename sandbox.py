# Make sure to first install selenium ('pip3 install selenium'), and the
# browser driver:
# https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
# https://www.edureka.co/community/52315/how-to-setup-chrome-driver-with-selenium-on-macos
# If you don't already install bs4 (BeautifulSoup)


from requests_html import HTMLSession
from datetime import date
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import os
import time
import math
import csv

# Initial Display of Information
os.system("clear")
print("Collecting Course Information... ")

# Initializing headless WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

# Class Initiliazation


class Course:
    def __init__(self, unique_id, code, subject, term, name, prereqs, postreqs):
        self.unique_id = unique_id
        self.code = code
        self.subject = subject
        self.term = term
        self.name = name
        self.prereqs = prereqs
        self.postreqs = postreqs


def retrieve_term_list(url):
    print("Collecting All Terms...")
    driver.get(url)
    dropdown_element = driver.find_element(By.ID, 'crit-srcdb')
    subjects = []
    for option in dropdown_element.find_elements(By.TAG_NAME, "option"):
        subjects.append(option.get_attribute("value"))
    return subjects[1:-1]


def retrieve_subject_list(url):
    print("Collecting All Subjects...")
    driver.get(url)
    dropdown_element = driver.find_element(By.ID, 'crit-subject')
    subjects = []
    for option in dropdown_element.find_elements(By.TAG_NAME, "option"):
        subjects.append(option.get_attribute("value"))
    return subjects[1:-1]


def retrieve_courses(subject, term):
    driver = webdriver.Chrome(options=options)
    url = 'https://cab.brown.edu/?subject={}&term={}#'.format(subject, term)
    driver.get(url)
    print("Collecting Course Information for {}, term {}... ".format(subject, term))
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    courses = []
    courses_element = soup.findAll(
        'div', attrs={'class': 'result result--group-start'})
    for course in courses_element:
        unique_id = course.findAll('a', attrs={'href': '#'})[0]['data-key'][4:]
        code = course.findAll('span', attrs={'class': 'result__code'})[0].text
        name = course.findAll('span', attrs={'class': 'result__title'})[0].text
        courses.append([unique_id, code, subject, term, name, [], []])
    print("Collected {} courses for {}, term {}.".format(
        len(courses), subject, term))
    driver.quit()
    return courses


all_courses = []
start = time.time()
counter = 0
subjects_list = retrieve_subject_list('https://cab.brown.edu/')
term_list = retrieve_term_list('https://cab.brown.edu/')
speed_list = []

for subject in subjects_list:
    end = time.time()
    print("Time Elapsed: {} minutes\n".format(math.floor((end-start)/60)))
    print("Collecting Courses from {}".format(subject))
    #counter2 = 0
    run_start = time.time()
    for term in term_list:

        print("{}% Completed...".format(round((
            (counter / (len(subjects_list) * len(term_list)))*100), 2)))
        print("Collecting Courses from term {}".format(term))
        run_end = time.time()
        speed_list.append(run_end - run_start)
        average_run_time = (sum(speed_list) / len(speed_list))
        eta_seconds = average_run_time * \
            ((len(subjects_list) * len(term_list)) - counter)
        eta_minutes = math.ceil(eta_seconds / 60)
        print("Estimated Time Remaining: {} minutes\n".format(eta_minutes))
        run_start = time.time()
        all_courses += retrieve_courses(subject, term)
        counter += 1
    #     counter2 += 1
    #     if counter2 == 7:
    #         break
    # if counter2 == 7:
    #     break

end = time.time()

with open("courses.csv", "w", encoding='UTF8', newline='') as newfile:
    writer = csv.writer(newfile)
    header = ['unique_id', 'code', 'subject',
              'term', 'name', 'prereqs', 'postreqs']
    writer.writerow(header)
    writer.writerows(all_courses)

print("{} courses collected over {} seconds ({} minutes)".format(
    len(all_courses), end-start, (end-start)/60))

exit()

# VVV TEST VVV
session = HTMLSession()

r = session.get('http://python-requests.org')
r.html.render()
r.html.search('Python 2 will retire in only {months} months!')['months']
'<time>25</time>'

# ^^^ TEST ^^^

# Initiating variables and classes
r = requests.get('https://cab.brown.edu/')
html_content = r.content
soup = BeautifulSoup(html_content, 'html.parser')


class Course:
    def __init__(self, unique_id, code, subject, term, name, prereqs, postreqs):
        self.unique_id = unique_id
        self.code = code
        self.subject = subject
        self.term = term
        self.name = name
        self.prereqs = prereqs
        self.postreqs = postreqs


# Collecting Departments & Terms to search through
subjects_list = []
for option in soup.findAll('select', attrs={'id': 'crit-subject'}):
    subjects_list = option.findAll('option')

terms_list = []
for option in soup.findAll('select', attrs={'id': 'crit-srcdb'}):
    terms_list = option.findAll('option')

# Collecting Course Information
for subject in subjects_list:
    for term in terms_list:
        page_r = requests.get(
            'https://cab.brown.edu/?subject={}&term={}'.format(subject, term))
        content = page_r.content


cs17 = Course(000, "CSCI 0170", "CSCI", "202110",
              "Computer Science: An Integrated Introduction", [], ["CSCI 0200"])


for i in subjects_list:
    print(i['value'])

for i in terms_list:
    print(i['value'])
