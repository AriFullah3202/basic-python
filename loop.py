"""
two loop primitive loop
1. for loop
2. while loop

"""
fruits = ['banana', 'apple', 'orange']
for fruit in fruits:
    if fruit == 'apple':
        continue # eta present ta skip korbe
    print("Fruits name" ,fruit)
    print('fruit len' , len(fruit))

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


