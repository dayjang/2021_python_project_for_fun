import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""




# print(format_currency(5000, "KRW", locale="ko_KR"))
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
            print("#",str(ctry))
            print(dic[ctry][0])
            return dic[ctry][2]
            
        else:
            print("please input number from the list ")
            find_currency()
    except: 
        print("you put string.. That is not number!!")
        find_currency()

def find_amount():
    try:
        amt =float(input())
        return amt
    except TypeError:
        print("that's not number. please Enter the NUMBER!! ")
        find_amount()
        
print("please choose your country  by number ")
first_cur = find_currency()
print("Now choose the other country by number.")
second_cur = find_currency()
print("Let us know many",first_cur,"do you want to conver to ",second_cur)
amt = find_amount()

url2= "https://wise.com/gb/currency-converter/"+first_cur.lower()+"-to-"+second_cur.lower()+"-rate?amount=" + str(amt)
transwise_req=requests.get(url2)


tran_soup = BeautifulSoup(transwise_req.text,"html.parser")
rate = tran_soup.find("h3",attrs={"class":"cc__source-to-target"}).find("span",attrs={"class":"text-success"}).text

# print( first_cur+str(amt)+" is " + second_cur + str(float(rate)*amt) )

print(format_currency(amt, first_cur, locale="ko_KR"),"is",format_currency((float(rate)*amt), second_cur, locale="ko_KR") )