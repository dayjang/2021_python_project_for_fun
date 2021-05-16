
import requests
from bs4 import BeautifulSoup
import json

def extract_article(url,db):
  articles=[]
  page=requests.get(url)
  article = json.loads(page.text)

  for i in art:
    link,title,points,author,num_comments,obj_id = article['title'], article['points'], article['author'], article['num_comments'], artitle['objectID']
    articles.append(obj_id)
    if db.get(obj_id):
      pass
    else:
      db.update({obj_id:[article['title'], article['points'], article['author'], article['num_comments'], artitle['objectID']]})
       
  return db, articles

def detail_article(url_id):
  page=requests.get(make_detail_url(url_id))
  aa = json.loads(page.text)
  comments=[]
  for d in aa['children']:
      if d['author']:
          comments.append([d['author'],d['text']])
      else:
          comments.append(['','deleted'])  
  return aa['title'],aa['points'], aa['author'],aa['url'],comments
