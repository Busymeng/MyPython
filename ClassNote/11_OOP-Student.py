##############################################################################
##  Object-Oriented Programming
##############################################################################

##############################################################################
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
     
   * A class contains 3 major components:
     1. Data fields: to describe object's properties, characteristics
     2. Methods: to describe object's action, behavior.
     3. Constructor: to create an object.
"""


##############################################################################
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


##############################################################################
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


##############################################################################
## Constructing an instance
"""
   * How do we make an instance?
     - We already did
     
   * Every class has a constructor.
     - It is a function which creates instances of the class.
     - The name of the constructor is the same as the name of the type, 
       only called as a function.
"""




##############################################################################
## Building Our Own Class
"""
   * Three key elements in a class:
     - Data fields: properties/characteristics of a class
       - Class data fields ==> used bu all class
       - Object data fields ==> used for specific object
       
     - Methods: actions/behaviors of a class
     
     - Constructor: create the objects
"""
##  Class with nothing


##  Creating class variable through class name


##  Creating instance variable through object name


##  Relationship between class variable and instance variables


##  When an instance is created, the class from which it was created is 
##  recorded in the special attribute name __class__ in the instance.



##############################################################################
## Creating Data Attibutes in Instances
"""
   * For user defined classes, you can add a new data attribute to an 
     instance by simple assignment using "dot assignment" to an instance.
     
   * Just like assignment can create a variable, assignment can create an
     attribute inside an instance, any instance that is of a user 
     defined type.
"""
##----------------------------------------------------------------------------



##----------------------------------------------------------------------------
##  self.x_coord is a public data field





##############################################################################
## Calling a Method, a Functional Attribute
"""
   * A method is a function that is particular to a particular type.
     - A method is called using the "dot" call, in the context of 
       a particular instance.
     - A method can only be used on an instance of the correct type.
     - We define methods in a class so that all instances of the class
       have access to that method.
"""





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



##----------------------------------------------------------------------------



##############################################################################
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





##############################################################################
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



##----------------------------------------------------------------------------
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




##----------------------------------------------------------------------------
"""
   * Version 3: Clock Arithmetic
"""





##----------------------------------------------------------------------------
"""
   * Version 4: print_clock() method
"""




##----------------------------------------------------------------------------
"""
   * Version 5: add_clocks() method
     - The method should not modify the existing clock instance, only 
       return a new clock. That means we call the constructor in the 
       add_clocks() method.
     - When we make a new clock instance, we don't have to enforce
       restrictions on attribute values. The constructor will do that for us!
"""





##############################################################################
## Indicating Privacy Using Double Underscores (__)
"""
   * All methods and instance variables in Python class are public.
   * Whenever a designer names an attribute with two leading underscores, 
     this is a message to anyone using the class that the designer considers 
     this a private variable. 
     - No one should change or modify its value.
     
   * To prevent this change from accidentally happening, Python mangles the 
     name of the attribute for outside use (outside of the class). 
     - The verb “mangle” here means that the attribute name is actually 
       changed. 
     - The transformation is as follows: an attribute named attribute is 
       changed to be ClassName attribute for outside use.
       
   * This change of name does not prevent the programmer from accessing the 
     attribute value. 
     - It only provides a layer of obfuscation. 
     - The programmer can get around the class designer if they choose, but 
       they do so in violation of the designer’s intent. 
       
"""
##----------------------------------------------------------------------------


