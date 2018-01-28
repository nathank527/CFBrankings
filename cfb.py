#! python3
#cfb.py -college football rank retriever
from lxml import html
import requests

hokies = False
try:
    page = requests.get('http://www.espn.com/college-football/rankings')
    tree = html.fromstring(page.content)
    print("Rankings")
    for i in range(1,26):
        path = '//*[@id="main-container"]/div/section[1]/div[3]/div/div[1]/div[1]/table/tbody[1]/tr[' + str(i) + ']/td[2]/a[2]/span/text()'
        test = tree.xpath(path)
        if test[0] == 'Virginia Tech': hokies = True
        print(str(i) + ". " + test[0] )
    if hokies: print("Go Hokies!")
except:
    print("Connection Error: Please check your connection")
