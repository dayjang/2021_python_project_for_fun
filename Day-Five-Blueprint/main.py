import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"

iban_req = requests.get(url)
iban_soup = BeautifulSoup(iban_req.text,"html.parser")

dic = dict()
for i in iban_soup.find_all('tr'):
#     print([td.text for td in i.find_all('td')])
    li = [td.text for td in i.find_all('td')]
    if len(li) == 4 and li[1] != 'No universal currency':
        dic.update({int(li[3]):[li[0],li[1],li[2]]})
        
for k in sorted(dic):
    print("#",k, dic[k][0])
    
def find_currency():
    ctry=input("Plz input the number of country you want to find: ")
    try:
        ctry = int(ctry)
        if ctry in dic.keys():    
            print("You chose", dic[ctry][0], dic[ctry][1])
            print("The currency code is", dic[ctry][2])
            
        else:
            print("please input number from the list ")
            find_currency()
    except: 
        print("you put string.. That is not number!!")
        find_currency()
find_currency()  