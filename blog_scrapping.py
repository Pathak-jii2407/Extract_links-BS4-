import requests
from csv import writer
from bs4 import BeautifulSoup


response=requests.get('https://www.sauravdhyani.com/')

soup=BeautifulSoup(response.text,'html.parser')

posts=soup.find_all(class_='centered-top')

with open('posts.csv','w') as csv_file:
    csv_writer=writer(csv_file)
    headers=['Title','link','date']
    csv_writer.writerow(headers)


    for post in posts:
        # print(post)
        # print(post.get_text())
        title=post.find(class_='post-title').get_text().replace('\n',' ')
        # print(title)
        link=post.find('a')['href']
        print(link)
        date=post.select('.post-date')[0].get_text()
        # print(date)
        csv_writer.writerow([link,title,date])

    
    
    


