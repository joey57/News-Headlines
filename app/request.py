from app import app
import urllib.request,json
from .models import news, articles
import urllib.request,json
from .models import news
News = news.News
Articles = articles.Articles

# getting api key
api_key = app.config['NEWS_API_KEY']
# getting the news base url
base_url = app.config['NEWS_API_BASE_URL']

def get_news(category):
  '''
  function that gets the json response to the url request
  '''
  get_news_url=base_url.format(category,api_key)

  with urllib.request.urlopen(get_news_url)as url:
      get_news_data = url.read()
      get_news_response = json.loads(get_news_data)

      news_results = None

      if get_news_response['sources']:
         news_results_list = get_news_response['sources']
         news_results = process_results(news_results_list)
      return news_results

def process_results(news_list):
  '''
  function that processes the news result and transform them to a list of objects
  '''
  news_results = []
  for news_items in news_list:
    name = news_items.get('name')
    author = news_items.get('author')
    url = news_items.get('url')
    country = news_items.get('country')
    description = news_items.get('description')
    category = news_items.get('category')

    news_object = News(name, author, url, country, description, category)
    news_results.append(news_object)

  return news_results

def get_articles(source_id):
  '''
  get articles based on articles source id
  '''
  get_source_url = articles_url.format(source_id,api_key)
  with urllib.request.urlopen(get_source_url)as url:
    get_articles_data = url.read()
    get_aerticles_response =json.loads(get_articles_data)

    articles_results = None
    get_aerticles_response['articles']
    articles_results = process_articles(get_aerticles_response['articles'])
  return articles_results

def process_articles(this_articles):
  '''
  '''  
      


