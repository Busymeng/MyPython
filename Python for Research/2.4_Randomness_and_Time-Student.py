#######################################################################
##  Simulating Randomness
##
"""
   * Many processes in nature involve randomness in one form or another.
     Whether we investigate the motions of microscopic molecules
     or study the popularity of electoral candidates, we see randomness, 
     or at least apparent randomness, almost everywhere.
     
   * We often use randomness when modeling complicated systems to abstract 
     away those aspects of the phenomenon for which we do not have useful 
     simple models.
     
   * We can use the random choice() function to carry out perhaps the simplest 
     random process -  the flip of a single coin.
"""
#-----------------------------------------------------------------------


#-----------------------------------------------------------------------
## Create 3 dices wit 6 faces, 8 faces, and 10 faces


#-----------------------------------------------------------------------
##  Takes the sum of 10 random integers between 0 and 9



#######################################################################
##  Examples Involving Randomness
##

"""
   Example #1:
   * Roll the die 100 times and plot a histogram of the outcomes, meaning
     a histogram that shows how frequent the numbers from 1 to 6 appeared 
     in the 100 samples..
"""
#-----------------------------------------------------------------------


#-----------------------------------------------------------------------
## Law of large Numbers
"""
   * Use 10000 or 1000000 instead of 100
"""


#-----------------------------------------------------------------------
"""
   Example #2:
   * Now consider rolling 10 dice instead of one dice. Our new random variable 
     y is going to be equal to x1 plus x2 plus all the way up to x10.
     - What is the distribution of y?
"""



######################################################################
##  Central Limit Theorem
##
"""
   * The so-called central limit theorem, or CLT, states that the sum 
     of a large number of random variables regardless of their distribution 
     will approximately follow a normal distribution.
     
   * For example, the height of a person probably depends on a large number 
     of factors that are related to things like genetics, nutrition, 
     environment, and so on.
     - If we think of height as being a random variable that itself consists
       of a large number of other random variables that are added together,
       we would expect the height of a person in a population to follow the 
       normal distribution.
"""



######################################################################
##  Using the NumPy Random Module
##
"""
   * Reasons to use the NumPy random module:
     - It has a broad range of different kinds of random variables.
     - It's very fast. Generally, using NumPy can result in code that 
       runs over 10 times faster than standard Python code.
"""
#-----------------------------------------------------------------------



"""
   * Standard Normal Distribution:
     - The normal distribution with mean 0 and standard deviation 1.
"""
#-----------------------------------------------------------------------


"""
   * Generate random integer: np.random.randint(1,7)
"""
#-----------------------------------------------------------------------




######################################################################
##  Measureing Time
##
"""
   * Reasons to measure the time:
     - You have two or more ways of coding up the same task and you'd like 
       to know which one is faster.
     - Another reason might be that you have a large dataset and you'd like 
       to have a sense ahead of time how long it might take to run your code.
"""
#-----------------------------------------------------------------------


#-----------------------------------------------------------------------



#-----------------------------------------------------------------------





######################################################################
##  Random Walks
##
"""
   * Usage of Random Walks:
     - They can be used to model random movements of molecules, but they can 
       also be used to model spatial trajectories of people, the kind 
       we might be able to measure using GPS or similar technologies.
       
   * There are many different kinds of random walks, and properties of 
     random walks are central to many areas in physics and mathematics.
     
   * Random walks in math:
       x(t=k) = x0 + dx(t=1) + dx(t=2) + ... + dx(t=k)
       
   * Let's try coding up random walker in NumPy, where we start at the origin,
     take 100 steps, and where each step is sampled from the standard normal 
     distribution. The normal distribution having mean 0 and standard 
     deviation equal to 1.
     - We're also going to assume that the x displacement and the y 
       displacement for any given step are independent, such that the 
       displacement in the horizontal direction has nothing to do with the 
       displacement in the vertical direction.
"""
#-----------------------------------------------------------------------


## Cumulative sum: np.cumsum()




## Put the original point to array: np.concatenate()
"""
   * Takes an iterable of np.arrays as arguments, and binds them along the 
     axis argument
"""


