import requests
from bs4 import BeautifulSoup as BS
from request_URL import url
import re



def test_connection():
    response = requests.get(url=url)
    soup = BS(response.content, 'lxml')
    block = str(soup.findAll('div', {'class': 'tensor_ru-About__block3-image-wrapper'}))
    height = re.findall(r'height="(\d+)', block)
    width = re.findall(r'width="(\d+)', block)

    for i in height:
        a = height[0]
        if a != i:
            result = False
        else:
            result = True

    for j in width:
        b = width[0]
        if b != j:
            res = False
        else:
            res = True


    if res == False or result == False:
        return(False)
    else:
        return(True)


def test_img():
    assert test_connection() != False, 'IMG SIZES NOT EQUAL'
    return 'IMG SIZES EQUAL'




print(test_img())





