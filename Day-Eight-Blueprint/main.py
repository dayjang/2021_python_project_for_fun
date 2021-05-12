import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"
alba_req = requests.get(alba_url)
alba_soup = BeautifulSoup(alba_req.text,"html.parser")
company = []
for i in alba_soup.find_all("div",attrs={"id":"MainSuperBrand"})[0].find("ul",attrs={"class":"goodsBox"}): #.find_all("li").find("a")["href"]#.find("li"):
    try:
        company.append([i.find("span",attrs={"class":"company"}).text,i.find("a",attrs={"class":"goodsBox-info"})["href"]])
    except:
        pass

def job_list(c_url):
    c_url = "http://emart.alba.co.kr/job/brand/"
    c_req = requests.get(c_url)
    c_soup = BeautifulSoup(c_req.text,"html.parser")
    job_li = [['place','title','time','pay','date']]
    for job in c_soup.find("table").find_all("tr",attrs={"class":""})[1:]:
        location=job.find("td").text
        name=job.find("span",attrs={"class":"company"}).text#.find("span",attrs={"class":"number"}).text
        hour=job.find("td",attrs={"class":"data"}).text#.find("span",attrs={"class":"number"}).text
        pay1=job.find("td",attrs={"class":"pay"}).find_all("span")[0].text 
        pay2=job.find("td",attrs={"class":"pay"}).find("span",attrs={"class":"number"}).text
        date=job.find("td",attrs={"class":"regDate last"}).text
#         print(name,location,hour,str(pay1)+str(pay2),date)
        job_li.append([location,name,hour,str(pay1)+str(pay2),date])
    return job_li

       
for name, c_url in company:
    with open(name+'.cvs', 'w') as f:
        write = csv.writer(f)
        write.writerows(job_list(c_url))