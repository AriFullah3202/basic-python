# লিস্টে অনেক রকমের ডাটা টাইপ থাকে ।
# এবং শুরুতে , শেষে second bracket থাকবে ।

firstset = {
    'aiquest' , 383, 38.8 , 88, True
}
print(firstset) # {True, 38.8, 88, 'aiquest', 383}
print(type(firstset)) # set output --- <class 'dict'>

# set hocche unique , duplicate remove kore dibe
# Access item korte for loop use korte hbe
# discard diye remove kore
# set Union | ei symbol use kori . ekhane sob value nibe
# set intersection hocche commnon value nibe, duplicate remove korbe

duration = {2, 3, 4, 45, 3, 3 ,4}
print(type(duration))
#remove duplicate automatic
print("remove duplicte automatic " , duration) # 2, 3, 4, 45
# access item 1st wa y
# set access korte for loop use korte hbe
for x in duration :
    print("acces item" , x)

# 2nd way to access
print(1001 in duration)     # false

# add item
duration.add(99)
print("add item" , duration) # {2, 99, 3, 4, 45} # buji nai
# discard
duration.discard(3333)  # buji nai
print('discard ' , duration)

# del keyword
#del duration
print('delete set' , duration) # bujij nai # ekane exception dibe

# set union
success = {3, 3, 2, 4}
print("set union" , duration | success)
# set intersection
print('set intersection' , duration & success)