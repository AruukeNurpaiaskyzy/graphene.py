import graphene 
from mutation import CreateUser, UpdateUser, DeleteUser
from query import Query
from type import User
from dataclasses import Field
from graphene import Field, String, List
class MyMutations(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()

class MyQuery(Query):
    user = Field(User)
    get_user = Field(User, id=String())
    get_users = List(User)
schema = graphene.Schema(query = MyQuery, mutation = MyMutations)
# result = schema.execute(
#     '''
#     mutation {
#         createUser(id: "1", name: "Aruuke", email: "arruke@gmail.com", password: "23345") {
#             user {
#                 id
#                 name
#                 email
#                 password
#             }
#         }
#     }
#     '''
# )

# print(result.data)

# result = schema.execute(
#     '''
#     mutation {
#         updateUser(id: "1", name: "Aruuk333e", email: "arruke@gmail.com", password: "233453") {
#             user {
#                 id
#                 name
#                 email
#                 password
#             }
#         }
#     }
#     '''
# )

# print(result.data)

# result = schema.execute(
#     '''
#     mutation {
#         deleteUser(id: "1" ) {
#             user {
#                 id
#                 name
#                 email
#                 password
#             }
#         }
#     }
#     '''
# )

# print(result.data)

# result = schema.execute(
#     '''
#     query {
#         deleteUser(id: "1" ) {
#             user {
#                 id
#                 name
#                 email
#                 password
#             }
#         }
#     }
#     '''
# )

# print(result.data)

result = schema.execute(
    '''
    query {
        deleteUser {
            user {
                id
                name
                email
                password
            }
        }
    }
    '''
)

print(result.data)




