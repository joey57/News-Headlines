from flask import render_template
from app import app

# views
@app.route('/')
def index():
  '''
  view root page function that returns the index page and its data
  '''
  title = 'Catch up real quick news headlines'
  return render_template('index.html',title=title)