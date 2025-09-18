#lst=[1,2,2,4,5]
#my_s={1,2,3,4}
#tuple_=(1,2,3,4)
#my_str="satyam"

#print(type(lst))
#print(type(my_s))
#print(type(tuple_))
#print(type(my_str))

from proj import chatbook
user1=chatbook()
#print(user1._chatbook__name)
#print(user1.get_name())
#user1.set_name("agent x")
#print(user1.get_name())
print(user1.id)
user2=chatbook()
print (user2.id)
chatbook.set_id(10)
user3=chatbook()
print(user3.id)
