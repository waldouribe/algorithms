from base_api_model import *

class User(BaseApiModel):
  pass

if __name__ == '__main__':
  b = User({'name': 'Waldo', 'email': 'uribe.fache@gmail.com'})
  print b.save()