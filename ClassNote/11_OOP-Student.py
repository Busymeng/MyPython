################################################################
##  Object-Oriented Programming
################################################################

################################################################
## OOP Concepts
"""
   * Classes are data types like dict or set or tuple. They share two 
     characteristics:
     - They have some internal structure (data) associated with the class.
     - There are some methods which can be used to manipulate this data.
     
   * We can create a new class as a new data type, suitable for whatever
     problems we wish to solve.
     
   * Programmer vs. Users vs. class designer
   
   * Object-oriented programming uses classes to create a different model
     of programming.
     - We think of a program more as a set of "objects we communicate with",
       a higher level of abstraction than just code.
       
   * Imagine how you interact with a car. It is very complicated piece of
     machinery, machinery mostly hidden from you.
     - However, there are some well defined interfaces that allow you to 
       control your car, the accelerator, the brake pedal, and steering
       wheel.
       
   * The complicated machinery is encapsulated, a complicated bundle that 
     has a well-defined way to access the bundle's capabilities.
"""


################################################################
## Refactoring
"""
   * If there is a better way doing sort, we can change the underlying
     implementation of the sort method without affecting anyone who use it.
     
   * Updating existing code to make it better in some way is called
     refactoring.
     - Refactoring requires the changes do not affect programmers who use
       the improved module, and you can see that OOP is a good way to 
       accomplish that.
"""


################################################################
## Classes and Instances
"""
   * Cookie cutter and individual cookie.
   
   * Cookie cutter is the class and cookie is the instance.
     - The class acts as a template for stamping out instance of itself.
     
   * What do you do with a class/cutter?
     - Create instances/cookies.
     
   * What do you do with an instance/cookie?
     - All instances have same methods associated with them.
     - You can decorate a cookie, make a cookie and eat a cookie.
     
   * Each instance is an example of a class, but it is the instances of
     the class we do work with.
     
   * Classes are for making instances, instances do the work once made.   
"""


################################################################
## Constructing an instance
"""
   * How do we make an instance?
     - We already did
     
   * Every type has a constructor.
     - It is a function which creates instances of the class.
     - The name of the constructor is the same as the name of the type, 
       only called as a function.
"""
dict1 = dict([("a",1),("b",2),("c",3)])
dict1
print(type(dict1),dict1)

tup1 = tuple([1,2])
print(type(tup1),tup1)

set1 = set("abcde")
print(type(set1),set1)



################################################################
## Building Our Own Class
"""
   * Three key elements in a class:
     - Data fields: properties/characteristics of a class
     - Methods: actions/behaviors of a class
     - Constructor: create the objects
"""
class Point(object):
    def __init__(self, x = 0, y = 0):
        self.x_coord = x
        self.y_coord = y
    
    def translate(self, x = 0, y = 0):
        self.x_coord += x
        self.y_coord += y
        
    def print_point(self):
        print("({:d},{:d})".format(self.x_coord,self.y_coord))

point1 = Point()
point1.print_point()

point2 = Point(10,20)
point2.print_point()

print(type(point1))
print(dir(point1))



################################################################
## Creating Data Attibutes in Instances
"""
   * For user defined classes, you can add a new data attribute to an 
     instance by simple assignment using "dot assignment" to an instance.
     
   * Just like assignment can create a variable, assignment can create an
     attribute inside an instance, any instance that is of a user 
     defined type.
"""
point3 = Point(x=100, y=100)
point3.new1 = 1000

print("point1 'stuff':",dir(point1))
print("point3 'stuff':",dir(point3))



################################################################
## Calling a Method, a Functional Attribute
"""
   * A method is a function that is particular to a particular type.
     - A method is called using the "dot" call, in the context of 
       a particular instance.
     - A method can only be used on an instance of the correct type.
     - We define methods in a class so that all instances of the class
       have access to that method.
"""
list1 = [10,20,30]
print(type(list1))
print(list1.pop())
print(dir(list1))

list1.upper()
point3.print_point()



################################################################
## Class Methods and the Variable self
"""
   * self is the first parameter of every method. It is always called self.
   
   * When we make a "dot call" on an instance and a method, the instance 
     in front of the "dot call" is bound to self.
     
   * Python automatically associates slef with the calling instance.
     - In this way, we can apply a method to a particular instance: the 
       calling instance; the one that gets bount to self.
       
   * Every reference to attributes of the instance now must be proceeded 
     by self, the instance that called the method.
"""
p1 = Point()
p1.translate(2,3)
p1.print_point()



################################################################
## Special Python Method Names
"""
   * Python uses special names, beginning and ending with two underlines,
     for special tasks.
     
   * __init__()
     - When Python constructs an instance using the constructor call, it
       performs a set of standard instance building operations.
     - It then gives the class designer an oppertunity to affect the 
       construction process.
     - If the instance has an associated __init__() method, then the
       default instance is passed, via the self parameter, to be initialized.
     - If not __init__() is provided, Python returns a default instance.
     - No return in __init__().
     - Because a __init__() is called in the context of a Python pipeline,
       a series of operations needed to make an instance. Python deals with
       the manipulation of the default instance.
"""
p0 = Point()
p1 = Point(y = 100)
p2 = Point(x=50, y=50)
print(p0.x_coord, p1.x_coord, p2.x_coord)



################################################################
## Making a Clock class
"""
   * Requirements:
     - Each Clock instance will represent the current time in hours, minutes,
       and seconds.
       > Thus each instance will have three data fields: hours, minutes,
         seconds.
     - The default instance will have all attributes set to 0.
     - We need to be able to nicely print a Clock instance.
     - We need to be able to add two Clock instances, yielding a new Clock
       instance.
       > No hour will greater than 23, no minutes or seconds greater than 59
       > We will use Clock arithmetic: when a sum larger than limit, a carry
         is added.
       > As our Clock instance has no days represented, there is no carry 
         recorded for hours.
"""

"""
   * Version 1: The Do-Nothing Version
     - Actually, it did do something.
     - A constructor was created and we can call it.
     - The constructor makes instance (though only default instance).
     - We can print the instance (it is the address of the instance).
     _ The instance of type Clock, and it has stuff in it according to dir.
"""
class Clock(object):
    pass # means do nothing
    
c1 = Clock()
print("My clock is:", c1)
print("Type is:", type(c1))
print(dir(c1))


"""
   * Version 2: Constructor
     - Let's make a constructor that adds the three attributes to each 
       instance, initializing them after Python creates the default instance.
     - self is bound to the default instance that Python has created, given
       us an oppertunity to initialize the default.
     - self.hours = hours
       > It means that the default instance, now associated with the variable
         self, will have created with in that instance an attribute hours.
       > The value of that attribute will be the value of the parameter hours.
"""
class Clock(object):
    def __init__(self,hours=0,minutes=0,seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

c2 = Clock()
print("My clock is:", c2)
print("Type is:", type(c2))
print(dir(c2))

c3 = Clock(hours = 10, minutes = 10, seconds = 10)
print(c3.hours,c3.minutes,c3.seconds)



"""
   * Version 3: Clock Arithmetic
"""
class Clock(object):
    def __init__(self,hours=0,minutes=0,seconds=0):               
        self.seconds = seconds % 60
        total_minutes = minutes + (seconds//60)
        self.minutes = total_minutes % 60
        self.hours = (hours + (total_minutes//60)) % 24
        
c4 = Clock(23,59,60)
print(c4.hours,c4.minutes,c4.seconds)


"""
   * Version 4: print_clock() method
"""
class Clock(object):
    def __init__(self,hours=0,minutes=0,seconds=0):               
        self.seconds = seconds % 60
        total_minutes = minutes + (seconds//60)
        self.minutes = total_minutes % 60
        self.hours = (hours + (total_minutes//60)) % 24
        
    def print_clock(self):
        print("{:02d}:{:02d}:{:02d}".format(self.hours,\
              self.minutes,self.seconds))

c5 = Clock(10,5,5)
c5.print_clock()



"""
   * Version 5: add_clocks() method
     - The method should not modify the existing clock instance, only 
       return a new clock. That means we call the constructor in the 
       add_clocks() method.
     - When we make a new clock instance, we don't have to enforce
       restrictions on attribute values. The constructor will do that for us!
"""
class Clock(object):
    def __init__(self,hours=0,minutes=0,seconds=0):               
        self.seconds = seconds % 60
        total_minutes = minutes + (seconds//60)
        self.minutes = total_minutes % 60
        self.hours = (hours + (total_minutes//60)) % 24
        
    def print_clock(self):
        print("{:02d}:{:02d}:{:02d}".format(self.hours,\
              self.minutes,self.seconds))
    
    def add_clocks(self,clock):
        seconds = self.seconds + clock.seconds
        minutes = self.minutes + clock.minutes
        hours = self.hours + clock.hours
        return Clock(hours, minutes, seconds)


c6 = Clock(10,59,59)
c7 = Clock(1,1,1)
c8 = c6.add_clocks(c7)

c6.print_clock()
c7.print_clock()
c8.print_clock()





