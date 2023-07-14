* [variable](#variable-role)
  * [valid role](#valid-role)
  * [Multiple Assignment variable and single value](#multiple-assignment-variable-and-single-value)
* [Input and output](#input-and-output-) 
* [string operation](#string-operation)
* [Data type](#data-type)
  * [Convert data Type](#convert-data-type)
  * [Dictionary](#dictionary-)
  * [List](#list)
    * [list access list](#)
  * [Binary type](#binary-type-)
  * [Data frame](#data-frame)
* [Operator](#operator)
  * [Arithmatic operator](#arithmatic-operator)
  * [Assignment operator](#assignment-operator)
  * [Bitwise operator](#bitwise-operator-)
  * [different-between-equal-to--not-equal-to-and-identity-operator-](#different-between-equal-to--not-equal-to-and-identity-operator-)
  * [Membership operator](#membership-operator)
  * [if-elif-else, if ,else](#if-elif-else--if--else)
  * [while loop](#while)
  * [for loop](#for-loop-)


## variable role
## valid role
1st rule
```python
aiquest = 110
_studernt = 'ai based'
# 2nd rule
django2 = "web development"
print(django2)
```
### kivabe variable likhbo

3.   kind of variable you can use 

1 . camel case

ছোট থেকে বড়
  ```python
helloWorld = 'hello world'
```
2 . pascal case

তার প্রথম অক্ষর বড়

```python
HelloWorld = 'hello world'
```
3. snake case

এখানে একটা শব্দের পরে ড্যাশ থাকে । 
 ```python
hello_world = 'hello world'
```
## Multiple Assignment variable and single value
এ্খানে id দিয়ে লোকেশন চেক করা হয়েছে ।
a, b , c এদের লোকেশন সেইম । 

varible গুলো এক জায়গায় সেইম হচ্ছে । 

```python
a = b = c = 34 # ekhane location same
print(id(a)) # memory location dekte pari
print(id(b)) # id mane location
print(id(c))
```
## Mutiple Assignment variable and multiple value
z, u , m  এখানে মেমোরি লোকেশন ভিন্ন । 


```python
z , u, m  = 10 , 20 , 39 # ekhane location different
print(id(z))
print(id(u))
print(m)
```
## Input and Output 

### input
এখানে ডিফল্ট স্ট্রিং নিবে । 

সুতারাং যদি আমরা ইনফুট হিসেবে সংখ্যা দিই তাহলে ও ।
```python
z = input('enter 1st number') # string input value string hbe bydefault string
y = input('enter 2nd number') # string input value string hbe bydefault string
sum = z + y
print(sum)
print(id(z))
```
যদি আমরা ইনফুট হিসেবে ইনটিজার নিতে চাই , তাহলে 
```python
# input for int =================
z = int(input('enter 1st number')) # string input value string hbe bydefault string
print(id(z))
y = int(input('enter 2nd number')) # string input value string hbe bydefault string
sum = z + y
print(sum)
```
### output
print ফাংশন ২টা আর্গমেন্ট নিবে । 

1. sep // এটা আলাদা করবে 
2. end // এটা 
3. values
4. file
5. flash

```python
print('hello world')
print("hello" , 'world' , sep="&" ,end="]") # hello&world]
```
## String operation
```python
import  sys;
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
print(sys.getsizeof(s))
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
# এখানে byte আকারে আসবে ।
print(type(s.encode()))

```
## Data type
### Numaric Data type
* 3 types of Numaric data typd
  * Integer
  * Float 
  * Complex
##### Integer
#### এখানে 
```python
a = 33
b = -88
c = 88888800000000000000000000000088888888888
print(type(a))
print(type(b))
print(type(c))
```
##### Float
```python
d = 89.9
e = -88.8
f = 888888888888888888888888888888888888888888888888888888888888888.888
print(type(d))
print(type(e))
print(type(f))
```
##### Complex
```python
# complex ekhane kivabe china jay
g = 4+4j
h = 4+8j
print(type(g))
print(type(h))
```
## Convert data type
#### ইন্টিজার থেকে ফ্লোট float to interger কনর্ভাট হয় ।
#### string to integer and float কনভার্ট হয় । 
#### string and interger থেকে  complex এ কনভার্ট হয় । কিন্ত
#### complex থেকে interger and float কনভার্ট করা যায় না । 

```python
z = 30
u = 33.44
m = 8j # j chara r hbe na
num_str = "10"
num_int = int(num_str)  # Converts string to integer
print(num_int)  # Output: 10

num_float = 3.14
num_int = int(num_float)  # Converts float to integer
print(num_int)  # Output: 3

num_str = "10"
num_int = complex(num_str)  # Converts string to complex
print(num_int)  # Output: 10+0j

num_float = 3.14
num_int = complex(num_float)  # Converts float to complex
print(num_int)  # Output: (3.14+0j)


#int to float
l = float(z)
print("int to float" , type(l))
# int to complex
o = complex(z)
print("int to float" , type(o))
# float to complex
r = complex(u)
print('float to complex', type(r))
#float to int
q = int(u)
print('float to int', q)
#Boolean
print(type(True)) #<class 'bool'>
print(type(False))
y = 90<20
print(type(y)) #<class 'bool'>

```
## Dictionary 
```python
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

```
## List
```python
# লিস্টে অনেক রকমের ডাটা টাইপ থাকে ।
# এবং শুরুতে , শেষে third bracket থাকবে ।

firtlist = ['lenebo' , 33 , '83']
print(firtlist) # ['lenebo' , 33 , 83]
print(type(firtlist)) # <class 'list'>
```
#### List access
##### remove and pop এর মধ্যে পাথ্যর্ক হচ্ছে remove parameter নিবে একটা item . যদি ঐ itex না থাকে exception দিবে ।
##### pop হচ্ছে index হিসেবে নিবে যদি ঐ ইনডেক্স না থাকে -১ রিটান করবে 
##### delete method ইনডেক্স আকারে ডিলিট হয় । যদি ইনডেক্স না থাকে তাহলে exception দিবে । আবার সম্পুণ ডিলিট হয় । 
```python
course = ['Math', 'Science', 'History', 'English', 'Geography']
print(len(course))

#access item
print('list item is ' , course[4]) # output Geography এটা জিরো থেকে শুরু হয় ।
print('list item' , course[-4]) # output Science এটা উল্টো দিক থেকে query করে 

# Range
# এটা শুরু এবং শেষ থেকে সার্চ করবে ।
print("Range:", course[2:5])   # Output: ['History', 'English', 'Geography']
# এটা শেষ থেকে search করবে 
print("Range:", course[:5])    # Output: ['Math', 'Science', 'History', 'English', 'Geography']
# এখানে আছে পাচটা item । সুতারাং এখানে শুরুতে পাচটা এর পর সাচ করলে ফাকা array আসবে । 
print("Range:", course[5:])    # Output: []

# Negative range
# এটা টিক উল্টো হবে ।
print("Range:", course[-2:])   # Output: ['English', 'Geography']
print("Range:", course[:-2])   # Output: ['Math', 'Science', 'History']

# Item value change
course[1] = 40
# এখানে চেন্জ করা হয়েছে ।
print('New list:', course)   # Output: ['Math', 40, 'History', 'English', 'Geography']
# Insert method
# এখানে কোন index এ insert করতে চান । 
course.insert(0, "aiQuest")
print('New inserted list:', course)   # Output: ['aiQuest', 'Math', 40, 'History', 'English', 'Geography']
# Append method
# append হচ্ছে একদম শেষে append korbe
course.append("study marts")
print('Append:', course)   # Output: ['aiQuest', 'Math', 40, 'History', 'English', 'Geography', 'study marts']
# Remove method
course.remove('Math')
print('Remove:', course)   # Output: ['aiQuest', 40, 'History', 'English', 'Geography', 'study marts']
# Pop method
course.pop(2)
print('Pop:', course)   # Output: ['aiQuest', 40, 'English', 'Geography', 'study marts']
# Del keyword
del course[2]
print('Del:', course)   # Output: ['aiQuest', 40, 'Geography', 'study marts']
# Sort method
alphabetic = ['python', 'django', 'ML']
alphabetic.sort()
print('Sorted:', alphabetic)   # Output: ['ML', 'django', 'python']

```

## Set
```python
# লিস্টে অনেক রকমের ডাটা টাইপ থাকে ।
# এবং শুরুতে , শেষে second bracket থাকবে ।

firstset = {
    'aiquest' , 383, 38.8 , 88, True
}
print(firstset) # {True, 38.8, 88, 'aiquest', 383}
print(type(firstset)) # set output --- <class 'dict'>


```
## Tuple
```python
# এখানে আনেকগুলৌ ডাটা টাইপ থাকে
# এবং শুরুতে এবং শেষে first bracket থাকে ।
firsttuple = ('ai' , 33, "idid" , 8 , True )
print(firsttuple) # ('ai', 33, 'idid', 8, True)
print(type(firsttuple)) # <class 'tuple'>
```
## Binary Type 
#### এটা বাইনারি নিয়ে কাজ করাে । পরে আলোচনা করা হবে ।
## Data frame
#### এটা টেবিল আকারে আঊটপুট আসে । এটা নিয়ে পরে আলোচনা করা হবে ।
# Operator

## Arithmatic operator
####  modulus হল ভাগ করে যেটা অবশিষ্ট থাকে । 
####  division and floor division মধ্যে পাথক্য আছে ।
#### division মধ্যে যদি ভাগশেষ না থাকলে পূর্ণ সংখ্যা আর থাকলে তাহলে পয়েন্ট আকারে দিবে । floor হচ্ছে ভাগশেষ থাকুক বা না থাকুক পূর্ণ সংখ্যা দিবে ।
কোন সংখ্যায় যদি কোন দশমিক বা ভগ্নাংশ না থাকে তাহলে সেটি পূর্ণ সংখ্যা।

#### exponentiation হচ্ছে পাওয়ার । 
x = 12, 
y = 4
মানে 

12 * 12 * 12 * 12 এখানে 12 4 বার ।
```python
x = 5
y = 2
#Addition
print("Add ", x + y); # 7
# Subtraction
print('sub', x -y) # output : 3
# mutiple
print('multiply' , x * y) # output : 10
# division
print('div' , x / y) # output : 2.5
# modulus
print("modulus" , x % y) # output : 1
# exponentiation
print("exponentiation", x**y) # output : 25
# floor division
print('floor division' , x//y) # output : 2

```
## Assignment Operator
#### এখানে একটা ভ্যলূ আরেকটা ভ্যালু এর মধ্যে এসাইন করা । 
```python
x = 5
y = 3
x =y
print('assign' , x ) # output 3
x += y
print('add and Assgainment' , x) # age 3 chilo , ekhon 3 + 3 = 6
x -= y
print("sub and assign" , x)
x *= y
print("multiply and assign" , x)
x %= y
print("moduls and assign" , x)
```
## Bitwise Operator 


#### এটা মজার জিনিস 
#### এটা বাইনারি নিয়ে কাজ করে 
1. & : bitwise and
2. | : bitwise Or
3. ^ : bitwise Xor
4. ~ : bitwise complement operator
5. << : left shift operator
6. : >> : right shift operator


```python
x = 12
y = 13
print('complement operator', ~x) #~ reverse kore ~1=0 , ~0=1 , output = -13
print('bitwise and ' , x&y) # output 12
print("bitwise or", x|y) # output 13
print("bitwise xor" , x^y) # output 1
a = 12
b = 2
print('left shift ', a<<b) #output 48
print('right shift ', a>>b) # output 3
```
## Comparison operator
< : less than

.> : Greter than

<= : less than or equal to

.>= : Greater than or equal to

== : Equal to

!= : Not Equal to

```python
x = 5
y = 2
print("less than ", x<y) # output False
print("Grater than" , x>y) # output True
print('Less than or eqal to' , x<=y) # output False
print('Greater than or eqal to ', x>=y) # output True
print("Equal to", x==y) # output False
print("Not equal to ", x!=y) # output True
```
## identity operator 
```python
x = 12
y = 12
print(x is y) # True
print(x is not y) # false
```
## Different between Equal to , Not equal to and identity operator 
#### == এটা value চেক করে ।
#### is এটা memory location চেক করে ।
```python
x = 5
y = 2
print(x is y) # True
print(x is not y) # false
print("Equal to", x==y) # output False
print("Not equal to ", x!=y) # output True
```
## Logical operator 
```python
x = 14
y = 3
print(x>y and x<y) # false , এখানে দুটা সত্য হতে হবে 
print(x>y or x<y) # true , এখানে একটা সত্য এবং মিথ্যা হতে হবে 
print(not(x<y and x>y)) # true , এটা ঠিক উল্টো 
```
## Membership Operator
#### এটা লিষ্টে আাছে কিনা চেক করবে ।
```python
x = ['python', 'django']
print("python" in x) # true
print("pythons" not in x) # true
```
## if-elif-else , if , else
### javaScript , java তে second bracket আছে । কিন্ত python এ শুধু কোলন আছে । 
#### এখানে indentation চেক করতে হবে । 
#### elif মানে একদম else if 
```python
motu = 100
patlu = 40
jhatka = 32
if(motu>patlu and motu<jhatka) :
    print('this is if')# ekhane identaion check korte hbe
elif(patlu>motu or patlu>jhatka):
    print("this is else")
else:
    print("this is else")
```
## For loop 
#### for loop সংখ্যা ভিত্তিতে এবং লিষ্টে লুপ করা হয়ে । 
### javaScript , java তে second bracket আছে । কিন্ত python এ শুধু কোলন আছে । 

```python
# এটা list
fruits = ['banana', 'apple', 'orange']
for fruit in fruits:
    if fruit == 'apple':
        continue # এটা apple এর সাথে মিললে স্কিপ করবে ।
    print("Fruits name" ,fruit)
    print('fruit len' , len(fruit))
# এটা range 
# range(stop)=============================
for i in range(10):
    print("this is my range") # 0 theke 9 print korbe
# range(start , end)
for i in range(50, 60): # 50 theke 59 porjonto print korbe because ekhane 60 border hisabe kaj kore
    print("this is my range" , i)
# range(start , end ,
# range(start, stop, step)
for i in range(2 , 100 , 3):
    print("this is ")

```
## while
অনবরত ঘুরতে থাকবে ।

condition দিতে হবে ।
### javaScript , java তে second bracket আছে । কিন্ত python এ শুধু কোলন আছে । 
value increase করার পথ বলে দিতে হবে ।
```python
i = 4
while i<10:
    print(i)
    i+=1 # eta dite hbe
while i<1 :
    i+=1
    if i == 5 : # ekhane
        continue
    print(i)
else:
    print(i)
```