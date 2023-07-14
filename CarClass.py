class Car:
    # constractor create kora
    # ekhane ekta parameter jar name holo name
    def __init__(self , name , price , color):
        print("this is one parameterize constructor is " , name)
        self.price = price
        self.color = color
        self.name = name
    # eta method
    def details(self):
        print('Car name' , self.name , self.price , self.color)
    def color(self):
        print("this is color method")

car1 = Car("bm" , "333" , 'blue')

car2 = Car('bw' , '3383' , 'green')
car2.details()
car1.details()

