import requests
import os

def urlcheck():
  print("please input your URLs. Seperated by Comma! ")
  urls=input()
  urls= urls.split(",")
  
  for url in urls:
    url = url.strip()
    if url[:7] != "http://" : 
      url = "http://"+url
    try:
      if requests.get(url).status_code == 200:
        print(url, "is up!") 
    except:
      print(url, "is down!")
      
  print("DO you wanna start over? y/n")
  start=input()
  if start == "y":
    urlcheck()
  else:
    return "Done!"

urlcheck()
