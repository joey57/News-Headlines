from app import app
import urllib.request,json
from .models import news
import urllib.request,json
from .models import news
News =news.News

# getting api key
api_key = app.config['NEWS_API_KEY']
# getting the news base url
base_url = app.config['NEWS_API_BASE_URL']

def get_news(category):
  '''
  function that gets the json response to the url request
  '''
  get_news_url = base_url.formart(category, api_key)
  print(get_news_url)
  with urllib.request.urlopen(get_news_url)as url:
    get_news_data = url.read()
    get_news_response = json.loads(get_news_data)

    news_results = None
    if get_news_response['sources']:
      news_results_list = get_news_response['sources']
      news_results = process_results(news_results_list)
    return news_results  
