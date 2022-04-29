class News:
  '''
  all news class to define news objects
  '''
  def __init__(self, name, author, url, description, country, category,id):
    self.name = name
    self.author = author
    self.url = url
    self.description = description
    self.country = country
    self.category = category
    self.id = id
