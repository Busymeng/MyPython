################################################################
##  Function Features
################################################################

################################################################
## Default and Named Parameters
"""
   * When we pass arguments to parameters, we have a one-to-one mapping 
     between arguments and parameters.
"""


"""
   * There are ways to provide default paramters and named parameters
     - A default parameter takes on a value when no argument is provided.
       > If however argument is provided, then yje parameter takes on the
         of the provided argument.
         
     - A named parameter allows you to set an argument in the invocation
       argument list based on the names of a parameter in the function's
       parameter list.
       > In this way you can have arguments be passed in another order other
         than the parameter list.
         
     - In the parameter list, the equal sign (=) identifies the defaults
       that will be provided if an argument is not given in the invocation.
       
     - In the argument list, the equal sign (=) in conjunction with a 
       parameter name, identifies which parameter value is being set.
       > In this way, arguments can be set out of order to the parameter list.
"""




"""
   * Mixing and matching arg-param passing by name and by order is confusing.
     However, the simple approach is:
     - provide any required paramters (those that do not have defaults) in
       order first.
       > if you don't have any named argument, in order is fine for all
         the arguments.
       > afterwards only provide named arguments
"""




################################################################
## Docstrings
"""
   * When we type a function into IDLE without filling out the arguments,
     IDLE will inform us of some help (a brief description) associated
     with the function. This documentation is useful.
     
   * We can provide the same level of support for functions that we write
     if we provide that information in a function docstring.
     
   * A docstring is simply a string located directly after the colon (:)
     of the function and before any other code. It's often typed in a
     triply-quoted string as that the documentation can be multiple lines.
     
   * This information is placed in a special variable as part of the
     function definition called __doc__ . This information can be used
     by any other program to support better programming.
"""


################################################################
## Arbitrary Number of Arguments
"""
   * Python provides a way to gather arguments beyond any required/named
     arguments as elements of a tuple. One need only mark this special 
     argument with an asterik (*) as shown below.
"""




################################################################
## Passing Mutables
"""
   * We need to understand what happens when we pass a mutable data structure
     (such as a list) to a function.
     
   * When we pass an argument (an integer), the namespaces in both the main
     and the function are associated with that object. 
     - If the function update that association, it doesn't change what is
       associated in the main namespace.
       
   * If we pass a mutable, such as a list, then the two namespaces again 
     share the same object.
     - However, now the function can modify the object in place since it is
       a mutable.
     - Thus, even though the list was not returned, the update in the main
       namespace as well.
"""


#---------------------------------------------------------------------


#---------------------------------------------------------------------




################################################################
## Default Arguments: Mutables
"""
   * When a function's default argument is created, it is only created once
     (at the time function is created), not every time the function is
     called.
     - Thus, if the default is a mutable, it accumulates in place changes!
       Strange!!!
"""


"""
   * The solution is never use a mutable as a default.
     - If you want to initialize a default mutable on a parameter, do it
       in the function code.
"""



################################################################
## More on Manipulation of Mutables
"""
   * The "is" operator
     - Two sequences are equal if they have exactly the same elements,
       in exactly the same order.
     - The "is" operator is a measure of sameness. Two sequences return True
       from "is" if they reference exactly the same object.
       > Not just equal, but the same object!
"""



"""
   * Shallow Copy and Deep Copy
     - Copying is one level deep. Such copying is called shallow copy.
     - There is a special method called deepcopy() to avoid this problem.
       > If a reference to another object is encountered in a copy, 
         it makes a new object instead of just copying the reference.
       > Very nice, but potentially expensive!!
"""

#---------------------------------------------------------------------


#---------------------------------------------------------------------



"""
   * Only a problem for mutables!
     - These issues only come up for mutable datatypes.
       > Because any operation we perform on an immutable datatype must
         create a new object, we never change an immutable object in place.
"""


################################################################
## Automatic Testing: assert
"""
   * How can we be confident our code is correct?
   * Using "assert" statements, which will cause your code to raise an
     AssertionError if your specified condition is not truthy.
"""


# assert things about inputs to functions



################################################################
## defaultdict
"""
   * Imagine that you’re trying to count the words in a document.
   * There are several approaches to do this.
"""




##  Using defaultdict
"""
   * A defaultdict is like a regular dictionary, except that when you try 
     to look up a key it doesn’t contain, it first adds a value for it using 
     a zero-argument function you provided when you created it. 
   * In order to use defaultdicts, you have to import them from collections.
"""



################################################################
## Counter
"""
   * A Counter turns a sequence of values into a defaultdict(int)-like 
     object mapping keys to counts.
"""

