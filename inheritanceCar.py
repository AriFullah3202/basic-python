class A :
    def detail(self):
        print("this is details")
    def details(self):
        print("this is details method")

class B(A) :
    def chd(self):
        print('this is child')
    def chd2(self):
        print("this si child2")
a = A()
a.details()
b = B()
b.details()
b.detail()
b.chd()