* [variable](#variable-role)
  * [valid role](#valid-role)
  * [Multiple Assignment variable and single value](#multiple-assignment-variable-and-single-value)
* [Input and output](#input-and-output-) 
* [string operation](#string-operation)
* [Data type](#data-type)
  * [Convert data Type](#convert-data-type)
  * [Dictionary](#dictionary-)
  * [List](#)

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
z, u , m  এখানে লোকেশন ভিন্ন । 


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
```python
z = 30
u = 33.44
m = 8j # j chara r hbe na

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