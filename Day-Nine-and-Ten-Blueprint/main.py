import requests
from flask import Flask, render_template, request
# from scrapper import extract_article, detail_article -- redundant fucntions... 

base_url = "http://hn.algolia.com/api/v1"
# 
# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"


# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def make_detail_url(id):
  return f"{base_url}/items/{id}"

db = {}
app = Flask("DayNine")

@app.route("/")

def home():
  ordby=request.args.get('order_by', "popular")
  #get(key: _K, default: _D) 
  #popular is default value.. if there is no {order_by} value
  if ordby not in db:
    print("Loading.........")
    if order_by == 'new':
      articles = requests.get(new)
    elif order_by == 'popular':
      articles = request.get(popular)
    results = articles.json()['hits']
    db[ordby] = results
  return render_template("index.html",orderby=ordby, results=results)

# @app.route("/?order_by=new")
# def new():
#   db, articles= extract_article(new,db)
#   return render_template("index.html", articles=articles)
# @app.route("/?order_by=popular")
# def new():
#   db, articles = extract_article(popular, db)
#   return render_template("index.html", articles=articles,db=db)
# @app.route("/＜id＞")

@app.rounte("/<id>")
def show_article(id):
  detail_url = make_detail_url(id)
  detail_request = requests.get(detail_request).json()
  return render_template('detail.html',result=detail_request)

app.run(host="0.0.0.0")