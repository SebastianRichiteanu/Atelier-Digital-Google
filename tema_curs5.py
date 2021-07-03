import requests
from bs4 import BeautifulSoup
import json


def web_scraper():
    f = open("FRSah_leaders.json", 'w')

    URL = "http://frsah.ro/index.php/conducere/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    leaders_table = soup.find(class_="td-pb-span8 td-main-content td-sidebar-left-content")
    leaders_sub_table = leaders_table.find(class_="td-page-content")
    leaders_by_roles = leaders_sub_table.find_all('p')
    leaders_with_roles = [x.text.split("\n") for x in leaders_by_roles]

    leaders = {}
    current_role = None
    for leader in leaders_with_roles:
        offset = 0
        if len(leader) > 2:
            current_role = leader[0]
            offset = 1
        leaders[current_role] = (leader[offset], leader[offset+1])
    del leaders['Membri']

    f.write(json.dumps(leaders))
    f.close()


def read_and_print():
    f = open("FRSah_leaders.json", 'r')
    leaders = f.read()
    f.close()
    leaders = json.loads(leaders)
    print(leaders)


def read_and_complete():
    f = open("FRSah_leaders.json", 'r+') # can't use 'a' because it's a dictionary
    leaders = f.read()
    leaders = json.loads(leaders)
    leaders['test'] = ('test', 'test@test.com')
    f.write(json.dumps(leaders))
    f.close()


while True:
    option = input('What would you like to do? \n 1. Use web scraper \n 2. Read and print \n 3. Read and add info \n')
    if option == '1':
        web_scraper()
        break
    elif option == '2':
        read_and_print()
        break
    elif option == '3':
        read_and_complete()
        break
