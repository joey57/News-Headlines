from distutils.debug import DEBUG


class Config:
  '''
  General configuration parent class
  '''
  pass

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
  