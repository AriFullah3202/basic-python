# এখানে আনেকগুলৌ ডাটা টাইপ থাকে
# এবং শুরুতে এবং শেষে first bracket থাকে ।
firsttuple = ('ai' , 33, "idid" , 8 , True )
print(firsttuple) # ('ai', 33, 'idid', 8, True)
print(type(firsttuple)) # <class 'tuple'>
details = ('create', 'read' , 'update' , 'delete', 30, 84, 84, )
# tuple hocche immutable object , list hocche mutable
print(type(details))
print('Access item range' , details[2])
print("access the range :" , details[:3])
print("Aceess the range " , details[3:])
#update
# tuple k amra change korte pari na
details[2] = "Dajago" # eta exception dibe
print('update item' , details);
# eijonno amra list convert korbo
cd = list(details) #list e convert kore tarpor data change kore abar amar tuple korlam
cd[2] = "dajango"
details = tuple(cd)
print("update item" , details) # update
#Add item
cd = list(details) # list e convert
cd.append('python')# add item

#remove item
cd = list(details)
cd.remove("python")