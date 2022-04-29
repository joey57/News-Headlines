from flask import render_template
from app import app
from app.request import get_news

# views
@app.route('/')
def index():
  '''
  view root page function that returns the index page and its data
  '''
  title = 'Catch up real quick news headlines'

  all_news = get_news('sports')
  general_news = get_news('general')
  tech_news = get_news('technology')

  return render_template('index.html',title=title, sports = all_news, general = general_news, technology = tech_news)

@app.route('/news/<int:news_id>')
def news(news_id):
  '''
  view news page function that returns the news details page and its data
  '''  
  return render_template('index.html', id = news_id)
