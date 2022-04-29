class Config:
  '''
  General configuration parent class
  '''
  NEWS_API_BASE_URL='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'

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
  