from models import ToDoModel, User, MemberModel




class ToDoService:
   def __init__(self):
       self.model = ToDoModel()


   def create(self, params):
       return self.model.create(params)


   def update(self, item_id, params):
       return self.model.update(item_id, params)


   def delete(self, item_id):
       return self.model.delete(item_id)


   def list(self):
       response = self.model.list_items()
       return response
  
   def get_by_id(self, item_id):
       response = self.model.get_by_id(item_id)
       return response

class MembershipService:
    def __init__(self):
        self.model = MemberModel()

    def create(self,params):
        return self.model.create(params)
    
    def update(self,member_id, params):
        return self.model.update(member_id,params)
    
    def list(self):
        return self.model.list_items()
    
    def get_by_id(self, item_id):
        return self.model.get_by_userID(item_id)
    

class UserService:
    def __init__(self):
        self.model = User()

    def create(self,params):
        if('name' not in params or 'email' not in params):
            raise Exception("Trying to add a user without proper parameters")
        return self.model.create(params['name'],params['email'])
    
    def list(self):
        return self.model.list_items()
    
    def get_by_id(self, user_id):
        return self.model.get_by_id(user_id)

