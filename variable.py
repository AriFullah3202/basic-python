import sys
#1st rule
aiquest = 110
_studernt = 'ai based'
# 2nd rule
django2 = "web development"
print(django2)
# 3rd rule
# this is invalid variable
#22
# special character , numaric value surute dile invalid hbe
# majkane space dite parbo na
# paython er build in key word dite parbo na
# case sensative hte hbe
# Abir Hasan = 10
# print(Abir Hasan)
# .saiful = 38;
# print(saiful)
# ekhon amra kivabe likhbo
# camal case ---mane example  helloWorld
# Pascal Case : mane example HelloWorld
# snake case : mane example hello_world
# ======================================================
# Multiple Assignment variable and single value ==========================
# kokhon eta use korbo ?
# memory location kothai hocche?
a = b = c = 34 # ekhane location same
print(id(a)) # memory location dekte pari
print(id(b)) # id mane location
print(id(c))

# Mulitiple variable and multiple value ==============================
z , u, m  = 10 , 20 , 39 # ekhane location different
print(id(z))
print(id(u))
print(m)
# uporer jodi amre z , u , m  = 10 , 20 ,  ekane error dibe because varibele 3ta ache a value 2 ta ache
# string niye kotha
a = 'imran'
print(type(a)) # output <class 'str'>

# input string ==========================
z = input('enter 1st number') # string input value string hbe bydefault string
y = input('enter 2nd number') # string input value string hbe bydefault string
sum = z + y
print(sum)
print(id(z))

# input for int =================
z = int(input('enter 1st number')) # string input value string hbe bydefault string
print(id(z))
y = int(input('enter 2nd number')) # string input value string hbe bydefault string
sum = z + y
print(sum)
# slicing you can return ===============
s = '          WelcoMMMe To python with django'

s = 'welcome to python with django'
# এখানে কোন ইনডেক্সে কি আছে , এটা চেক করা
print(s[0:3]) # wel
print(s[0:3333])
# upper case
print(s.upper()) # WELCOME TO PYTHON...
# lower case
print(s.lower())  # welcome...
# white space remove
# যেমন : s = '    welcome to python with django'
# এখানে capital কে small করে দিবে ।
print(s.capitalize()) #
# white space remove
print(s.strip())
# repalace string
print(s.replace('o' , 'a')) #
# split string
print(s.split()) # 'welcome' , 'to' , 'python'
print(s.split()[0]) # welcome মানে প্রথম শব্দটা রির্টান করবে ।
# stirng Concatination
v = '23'
print(s+ "" + v)  # welcome to ... '23'
# counting
print(s.count("o")) # 3 ta o ache
# lenth
print(len(s))
# ওই কত বাইট সাইজ এটা প্রিন্ট করবে মানে ও্ই ভ্যরিয়েবল কত সাইজ দখল ঋবে আছে ।
# index , find এই মেথড দুইটা ইনডেক্স নাম্বার রির্টান করবে ।
# যদি ভালু না থাকে index এ ইরর find এ -1 return করবে ।
print(s.index('w' , 0 , 8))
print(s.find('y' , 4 , 8))
# এটা যেগুলো বড় হাতের আছে ওটা ছোট হাতের , ছেট থাকলে বড় ।
print(s.swapcase())
# এটা প্রত্যেকটা শব্দের প্রথম অক্ষর বড় হাতের হবে ।
print(s.title())
# এগুলো বড় হাতের কিনা এবং ছোট হাতের কিনা চেক কররে ।
print(s.isupper())
print(s.islower())
# এখানে ১০০ ঘর পরে welcome to ... এভাবে আসবে ।
print(s.center(100))
# স্ট্রিং ফরমেট
# এখানে 1000 {} এর মধ্যে বসে যাবে ।
x = 1000
print('this si {} taka'.format(x)) # this is 1000 taka
print(s.encode())
print(type(s.encode()))