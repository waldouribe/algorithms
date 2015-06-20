 # users GET    /users(.:format)                users#index
 #                POST   /users(.:format)                users#create
 #       new_user GET    /users/new(.:format)            users#new
 #      edit_user GET    /users/:id/edit(.:format)       users#edit
 #           user GET    /users/:id(.:format)            users#show
 #                PATCH  /users/:id(.:format)            users#update
 #                PUT    /users/:id(.:format)            users#update
 #                DELETE /users/:id(.:format)            users#destroy
class BaseApiModel:
  def __init__(self, params):
    self.params = params
    self.base_url = "http://localhost:3000/"
    self.class_name = self.__class__.__name__.lower()

  def save(self):
    url = self.base_url + self.class_name + "/new"
    method = "POST"
    params_s = ""
    for key in self.params:
      params_s += key + "=" + self.params[key] + "&"
    params_s = params_s[0: -1]
    return "curl --data" + " \""+ params_s +"\" " + url

if __name__ == '__main__':
    b = BaseApiModel({'name': 'Waldo', 'email': 'uribe.fache@gmail.com'})
    print b.save()
