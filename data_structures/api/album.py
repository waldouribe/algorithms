from base_api_model import *

class Album(BaseApiModel):
  pass

if __name__ == '__main__':
  album = Album({'name': 'Mi Album'})
  print album.save()