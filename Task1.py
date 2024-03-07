import requests
from bs4 import BeautifulSoup as BS
from urls import url_2, url_3
import regex


response = requests.get(url_2)
result = requests.get(url_3)

soup = BS(response.content, 'lxml')
soup_1 = BS(result.content, 'lxml')


def check_region():

    title = str(soup.findAll('span', {'class': 'sbis_ru-Region-Chooser__text sbis_ru-link'}))
    region = regex.findall(r'>([\p{Cyrillic} \.]+)<', title)

    title_1 = str(soup_1.findAll('span', {'class': 'sbis_ru-Region-Chooser__text sbis_ru-link'}))
    region_1 = regex.findall(r'>([\p{Cyrillic} \.]+)<', title_1)

    # if region[0] == region_1[0]:
    #     return 'Регион не изменился'
    # else:
    #     return 'Регион изменился'

    return region[0], region_1[0]




def check_partners():
    title = str(soup.findAll('div', {'class': 'sbisru-Contacts-List__col-1'}))
    partner = regex.findall(r'title="[\p{Cyrillic}\. «»""-]+">([\p{Cyrillic}\. «»"" -]+)</div>', title)

    title_1 = str(soup_1.findAll('div', {'sbisru-Contacts-List__col-1'}))
    partner_1 = regex.findall(r'title="[\p{Cyrillic}\. «»""-]+">([\p{Cyrillic}\. «»"" -]+)</div>', title_1)

    return partner, partner_1



def check_title():
    title = str(soup.findAll('title'))
    title_1 = str(soup_1.findAll('title'))

    return title, title_1


def check_url():
    url = str(soup.findAll('link', {'rel': 'canonical'}))
    url_1 = str(soup_1.findAll('link', {'rel': 'canonical'}))

    re_url = regex.findall(r'href="(.+)" rel', url)
    re_url_1 = regex.findall(r'href="(.+)" rel', url_1)

    return re_url, re_url_1


def test_url():
    assert check_url()[0] != check_url()[1], 'URL TEST FAILED'
    return 'URL TEST PASSED'

def test_title():
    assert check_title()[0] != check_title()[1], 'TITLE TEST FAILED'
    return 'TITLE TEST PASSED'

def test_partners():
    assert check_partners()[0] != check_partners()[1], 'PARTNERS TEST FAILED'
    return 'PARTNERS TEST PASSED'

def test_region():
    assert check_region()[0] != check_region()[1], 'REGION TEST FAILED'
    return 'REGION TEST PASSED'

print(test_url())
print(test_title())
print(test_partners())
print(test_region())
