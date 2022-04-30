import os
class Config:
  '''
  General configuration parent class
  '''
  NEWS_API_BASE_URL='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
  ARTICLES_API_BASE_URL='https://newsapi.org/v2/everything?sources={}&apiKey={}'
  NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

class ProdConfig(Config):
  '''
  Production configuration child class
  args config:the parent configuration class with general settings
  '''
  pass

class DevConfig(Config):
  '''
  Development configuration child class
  args config: the parent configuration class with general configuration settings
  '''
  DEBUG = True

config_options = {
  'development':DevConfig,
  'production' :ProdConfig
}
  