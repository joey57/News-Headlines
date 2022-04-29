from flask import render_template
from app import app
from app.request import get_articles, get_news

# views
@app.route('/')
def index():
  '''
  view root page function that returns the index page and its data
  '''
  title = 'Catch up on the news'

  all_news = get_news('sports')
  general_news = get_news('general')
  tech_news = get_news('technology')

  return render_template('index.html',title=title, sports = all_news, general = general_news, technology = tech_news)

@app.route('/news/<int:id>')
def news(id):
  '''
  view news page function that returns the news details page and its data
  '''  
  news = get_news(id)
  return render_template('index.html', news = news)

@app.route('/articles/<source_id>')
def articles(source_id):
  '''
  function that returns articles by source_id
  '''
  article_source = get_articles(source_id)
  title = f'{source_id} | Articles'
  return render_template('articles.html', title = title, name = source_id, news = article_source)