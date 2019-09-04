from werkzeug.security import safe_str_cmp
from models.user import UserModel





def authenticate(username,password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password,password):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)




#
# users = {
#     Users(1 , 'nifty' , 'noob457')
#
# }
#
#
# user_mapping = {u.username: u for u in users}
# userid_mapping = {u.id: u for u in users}
# # users ={
# #
# #     'id'=1,
# #     'username'='nifty',
# #     'password'='noob457'
# # }
# #
# # user_mapping = {'nifty':{
# #         'id'=1,
# #         'username'='nifty',
# #         'password'='noob457'
# #     }
# # }
# #
# # userid_mapping = {1:{
# #     'id'=1,
# #     'username'='nifty',
# #     'password'='noob457'
# # }}
