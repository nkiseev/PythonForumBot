from bs4 import BeautifulSoup
import requests

URL = 'https://itfy.org/forums/python-help/index.rss'


def get_xml(url):
    resp = requests.get(url)
    return resp.text


def get_content():
    xml = get_xml(URL)
    content = []
    soup = BeautifulSoup(xml, 'lxml')
    items = soup.find_all('item')

    for item in items:
        title = item.find('title').text
        link = item.find('guid').text
        content.append({'title': title, 'link': link})
    return content


if __name__ == '__main__':
    from pprint import pprint
    s = get_content()
    pprint(s)
