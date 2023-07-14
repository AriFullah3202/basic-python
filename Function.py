# python function def keyword diye

# def keyword eta dite hbe
# then methon name
# first bracket
# then :
# then body

def hello() :
    print("hello world")
hello()
# with parameter
def hello(name) :
    print(name)
hello("Arif")
# with return type , eta java deklam na
def cacutation (x, y):
    d = x+y
    e = x-y
    f= x*y
    g = x/y
    return  d , e , f, g
sum , sub , mul , div = cacutation(20 , 4)
print("sum :" , sum , "sub" , sub , "mul" , mul , "div" , div)