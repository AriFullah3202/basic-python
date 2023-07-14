#dictionary
# {} set , dictionary হল second bracket শুরুতে এবং শেষে হয় ।
# তবে python এ dictionary কি এবং ভালু java তে map এর মতো ।
firstdict = {
    "name" : 'Arif',
    "id" : 222,
    "year" : 2333
}
print(firstdict) # {'name': 'Arif', 'id': 222, 'year': 2333}
print(type(firstdict)) # <class 'dict'>
# dictionary er key k access korte chaile
x = firstdict.keys() # eta key gulo print korbe
print(x)
# dictionary value
y = firstdict.values() # sob value print korbe
print(y)
x = firstdict['name'] # etar value print korbe
print(x)
y = firstdict.get('Dl')
print(y)
# Adding item
# Removing item
# item add
firstdict['Da'] = 30 # firsdict er vitor e ei item ta add hobe
# update method
firstdict.update({'year' : 2032}) #year er moddhe value change holo
print(firstdict)
# remove methon
firstdict.pop()



