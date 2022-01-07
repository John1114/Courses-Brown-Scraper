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

# Header creation
header = {'authority': 'cab.brown.edu',
          'method': 'POST',
          'path': '/api/?page=fose&route=search&keyword=cs&is_ind_study=N&is_canc=N',
          'scheme': 'https',
          'accept': 'application/json, text/javascript, */*; q=0.01',
          'accept-encoding': 'gzip, deflate, br',
          'accept-language': 'en-US,en;q=0.9',
          'content-length'
          'content-type': 'application/json',
          'cookie': '_ga=GA1.2.1916766544.1629846630; _fbp=fb.1.1630269581972.2088654862; TS01b3a32b=014b44e76b615993d6109efc3178436f0c6c60f9367297cb80a0e486bdf1bdc611f80d4c53234a1d0ef4a2b7ab587d2a034579df13; __utmc=117564634; TS016d0986=014b44e76b487ec5df4e490e0fc7b1f4c8e1911babda4b77b8c5fda1de63328b3cbfbd867f2844d92cbb96a86efad6e71dce272f78; _gcl_au=1.1.1486512660.1635255668; _hjid=c2bb7f81-b8b7-4940-90fe-a77349cffc64; optimizelyEndUserId=oeu1635633924794r0.5161157814777972; amplitude_id_9f6c0bb8b82021496164c672a7dc98d6_edmbrown.edu=eyJkZXZpY2VJZCI6Ijg2YzIwZDRiLTJlYjMtNDY2Zi1hMDg3LTJmY2JkNmY4N2EyM1IiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTYzNTYzMzkyNTAzMiwibGFzdEV2ZW50VGltZSI6MTYzNTYzNDYzMjc3MCwiZXZlbnRJZCI6MCwiaWRlbnRpZnlJZCI6Miwic2VxdWVuY2VOdW1iZXIiOjJ9; amplitude_id_408774472b1245a7df5814f20e7484d0brown.edu=eyJkZXZpY2VJZCI6ImVlYjk0MDgyLTVkNDYtNDcyMC1hOGZmLWE0ODFjMjdmYTkxYiIsInVzZXJJZCI6bnVsbCwib3B0T3V0IjpmYWxzZSwic2Vzc2lvbklkIjoxNjM1NjMzOTI1MzgyLCJsYXN0RXZlbnRUaW1lIjoxNjM1NjM0NjMzMjkwLCJldmVudElkIjoyLCJpZGVudGlmeUlkIjo3LCJzZXF1ZW5jZU51bWJlciI6OX0=; gaCustomerId=Unknown; gaTAMId=Unknown; gaInstitutionId=000000574199; _xdClientId=1916766544.1629846630; gaPrevTAMId=Unknown; _rdt_uuid=1635732268235.d46b3c5c-09bb-44d7-b55b-0d15edfe2288; _scid=7d9df212-a1eb-47ac-b139-67bcec92778e; __gads=ID=0cd878d6b7661157:T=1635732269:S=ALNI_MYUWW0B9dEDXpfOy-ZU1SFgws2eEw; _sctr=1|1635652800000; _gaCorpUserId=1635732270174.240396; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid=D7874AE2B7A1CBC932547F55B98B38700; _vwo_ds=3%3At_0%2Ca_0%3A0%241635780348%3A19.41618024%3A%3A%3A2_0%3A0; __utma=117564634.1916766544.1629846630.1634671203.1636407018.11; __utmz=117564634.1636407018.11.10.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); IDMSESSID=C889E6BCFE374EE19515554FB8BEBB457299EF6C90A2749C0D9DB3483E16473D3D74F35D3EB7F15DF6B1B5351C438C4C; __CT_Data=gpv=2&ckp=tld&dm=brown.edu&apv_16427_www03=2; ezproxy=iZWmVHGAIUpxItg; _ce.s=v11.rlc~1640174374217; _hjSessionUser_2580298=eyJpZCI6IjU1M2Y4YzJkLTY0ZmEtNWRhYS1hNzQ4LTRmZGIyYzBiZjk0MSIsImNyZWF0ZWQiOjE2NDAxNzQ0OTcwNDIsImV4aXN0aW5nIjp0cnVlfQ==',
          'origin': 'https://cab.brown.edu',
          'referer': 'https://cab.brown.edu/',
          'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"macOS"',
          'sec-fetch-dest': 'empty',
          'sec-fetch-mode': 'cors',
          'sec-fetch-site': 'same-origin',
          'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36',
          'x-requested-with': 'XMLHttpRequest'}

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


def get_prereqs(desc):
    # pre-req
    # prerequisites
    # prerequisite
    return ""


def retrieve_term_list(url):
    print("Collecting All Terms...")
    driver.get(url)
    dropdown_element = driver.find_element(By.ID, 'crit-srcdb')
    terms = []
    for option in dropdown_element.find_elements(By.TAG_NAME, "option"):
        if option.get_attribute("value") != '999999' and option.get_attribute("value") != '':
            terms.append(option.get_attribute("value"))
    return terms


def retrieve_subject_list(url):
    print("Collecting All Subjects...")
    driver.get(url)
    dropdown_element = driver.find_element(By.ID, 'crit-subject')
    subjects = []
    for option in dropdown_element.find_elements(By.TAG_NAME, "option"):
        subjects.append(option.get_attribute("value"))
    return subjects[1:-1]


def retrieve_courses(subject, term, all_courses_dict):
    driver = webdriver.Chrome(options=options)
    url = 'https://cab.brown.edu/?subject={}&term={}#'.format(subject, term)
    driver.get(url)
    print("Collecting Course Information for {}, term {}... ".format(subject, term))
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    courses_element = soup.findAll(
        'div', attrs={'class': 'result result--group-start'})
    for course in courses_element:
        unique_id = course.findAll('a', attrs={'href': '#'})[0]['data-key'][4:]
        code = course.findAll('span', attrs={'class': 'result__code'})[0].text
        name = course.findAll('span', attrs={'class': 'result__title'})[0].text
        if code in all_courses_dict:
            info_list = all_courses_dict[code]
            info_list[1].append(term)
            all_courses_dict[code] = info_list
        else:
            info_list = [subject, [term], name, [], [], []]
            all_courses_dict[code] = info_list
    print("{} courses collected in total".format(len(all_courses_dict)))
    driver.quit()
    return all_courses_dict


# Creates a dictionary where each key is the course code, and each value is a
# list of information about the course
all_courses = {}
start = time.time()
counter = 0
subjects_list = retrieve_subject_list('https://cab.brown.edu/')
term_list = retrieve_term_list('https://cab.brown.edu/')
speed_list = []
first_run_start = time.time()
for subject in subjects_list:
    end = time.time()
    print("Time Elapsed: {} minutes\n".format(math.floor((end-start)/60)))
    print("Collecting Courses from {}".format(subject))
    # counter2 = 0
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
        run_minutes = (run_end - first_run_start) / 60
        print("Time Running: {} minutes".format(round(run_minutes, 2)))
        print("Estimated Time Remaining: {} minutes\n".format(eta_minutes))
        run_start = time.time()
        all_courses = retrieve_courses(subject, term, all_courses)

        counter += 1
    #     counter2 += 1
    #     if counter2 == 2:
    #         break
    # if counter2 == 2:

    #     break

end = time.time()
print("{} courses collected over {} seconds ({} minutes)".format(
    len(all_courses), end-start, (end-start)/60))


# Goes through bulletin.brown.edu and adds all the pre-reqs to courses
url = "https://bulletin.brown.edu/departments-centers-programs-institutes/"
print("Beginning collection of pre-requisites ... ")
r = requests.get(url, headers=header)
if not r.ok:
    print('Error Code: {}'.format(r.status_code))
    if r.status_code in range(500, 600):
        print("Server Error")
    elif r.status_code in range(400, 500):
        print("Client Error")
else:
    link_list = []
    html_content = r.content
    soup = BeautifulSoup(html_content, 'html.parser')
    col_a = soup.findAll('div', attrs={'class': 'cola'})[0]
    col_b = soup.findAll('div', attrs={'class': 'colb'})[0]
    for link in col_a.findAll('a'):
        link_list.append(
            'https://bulletin.brown.edu{}#courseinventory'.format(link['href']))
    for link in col_b.findAll('a'):
        link_list.append(
            'https://bulletin.brown.edu{}#courseinventory'.format(link['href']))

    for link in link_list:
        print(link)
        page = requests.get(link, headers=header)
        if not page.ok:
            print('Error Code: {}'.format(page.status_code))
            print(link)
            if page.status_code in range(500, 600):
                print("Server Error")
            elif page.status_code in range(400, 500):
                print("Client Error")
        else:
            html_content = page.content
            soup = BeautifulSoup(html_content, 'html.parser')
            for course_block in soup.findAll('div', attrs={'class': 'courseblock'}):
                course_code = course_block.findAll(
                    'p', attrs={'class': 'courseblocktitle'})[0]['data-code']
                course_description = course_block.findAll(
                    'p', attrs={'class': 'courseblockdesc'})[0].text
                if course_code in all_courses:
                    info_list = all_courses[course_code]
                    info_list[-1].append(course_description)
                    # info_list[-3].append(get_prereqs(course_description))
                    all_courses[course_code] = info_list

end = time.time()
print("All pre-requisistes collected over {} seconds ({} minutes)".format(
    len(all_courses), end-start, (end-start)/60))

with open("courses.csv", "w", encoding='UTF8', newline='') as newfile:
    writer = csv.writer(newfile)
    header = ['code', 'subject',
              'terms', 'name', 'prereqs', 'postreqs', 'info']
    writer.writerow(header)

    d = {"name": "python", "version": 3.9}

    all_courses_list = []
    for key, val in all_courses.items():
        all_courses_list.append([key] + val)
    writer.writerows(all_courses_list)

end = time.time()
print("Final Runtime: {} seconds ({} minutes)".format(
    len(all_courses), end-start, (end-start)/60))
