import requests
from bs4 import BeautifulSoup
from googlesearch import search
from csv import writer
import threading


def remove_opr(url):
    opr = "&`~!@#|$^*()_}{][;''?,"
    for char in opr:
        if char in url:
            url = url.replace(char, '')
    return url


def Searching(url):
    response=requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    title = soup.find('title').get_text().replace('/',',')
    print(title)
    with open(f'{title}', 'w', newline='', encoding='utf-8') as file:
        csv_writer=writer(file)
        headers=['sr.','link','Text']
        csv_writer.writerow(headers)
        links=soup.find_all('a')
        for i, link in enumerate(links, start=1):
            main=link.get('href','')
            doc=link.get_text(strip=True).replace(' ','').lower()
            csv_writer.writerow([i,main,doc])
            if subject in doc:
                print(doc,main,end='\n')
def google_search(query, num_results=3):
    try:
        for url in search(query, num_results=num_results):
            Searching(remove_opr(url))
    except Exception as e:
        print(e)



subject=input('What You are searching: ')
google_search(subject)