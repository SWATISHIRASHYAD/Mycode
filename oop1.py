#The init method will be called automatically where variables or instances are declared 
#self is the object,with help of  this each object get referenced and they are assigned values and it is required
#these instance variables are specific to an object,if you change the value it will change for thet object.
#But what if u want a variable common to every object???Those are Class variables
class jack:
    haircolor="black" #Class variable
    def __init__(self):
        self.color="orange"
        self.ht=5
    def print(self):
        print("color of jack is orange")
        print("height of jack is ",self.ht,"feet",)
    def update(self):
        self.ht=6
j1=jack() #object creation
j1.update()   #calling the method
j1.print()
j2=jack()
print("this is jack 2")
j2.print()
#working with memory adress
print(id(j1))
print(id(j2))
j2=j1
print(id(j1))
print(id(j2))
j2.print()
j1.print()
#working with class variables
print(j1.haircolor)
print(j2.haircolor)
j1.haircolor="neeli"
print(j1.haircolor)
print(j2.haircolor)

        