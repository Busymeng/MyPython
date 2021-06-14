##############################################################################
##  Introduction to Seaborn
##----------------------------------------------------------------------------

##############################################################################
##  Distribution Plots
##----------------------------------------------------------------------------
"""
   * Let's discuss some plots that allow us to visualize the distribution 
     of a data set. These plots are:
     - distplot
     - jointplot
     - pairplot
     - rugplot
     - kdeplot
"""
import seaborn as sns
# get_ipython().run_line_magic('matplotlib', 'inline')


##  Data
"""
   * Seaborn comes with built-in data sets!
"""



##  distplot
"""
   * The distplot shows the distribution of a univariate set of observations.
"""


##  To remove the kde layer and just have the histogram use:



##  jointplot
""" 
   * jointplot() allows you to basically match up two distplots for bivariate 
     data. With your choice of what **kind** parameter to compare with: 
     - “scatter” 
     - “reg” 
     - “resid” 
     - “kde” 
     - “hex”
"""



##  pairplot
"""
  * pairplot will plot pairwise relationships across an entire dataframe 
    (for the numerical columns) and supports a color hue argument (for 
    categorical columns). 
"""



##  rugplot
"""
   * rugplots are actually a very simple concept, they just draw a dash mark 
     for every point on a univariate distribution. 
     
   * They are the building block of a KDE plot.
"""



##  kdeplot
"""
   * kdeplots are [Kernel Density Estimation plots]
     (http://en.wikipedia.org/wiki/
          Kernel_density_estimation#Practical_estimation_of_the_bandwidth). 
     
   * These KDE plots replace every single observation with a Gaussian (Normal) 
     distribution centered around that value. 
"""
##  Don't worry about understanding this code!
##  It's just for the diagram below


##  Create dataset


##  Create another rugplot


##  Set up the x-axis for the plot


##  100 equally spaced points from x_min to x_max


##  Set up the bandwidth, for info on this:



##  Create an empty kernel list


##  Plot each basis function



##  To get the kde plot we can sum these basis functions.

##  Plot the sum of the basis function


##  Plot figure


##  Add the initial rugplot


##  Get rid of y-tick marks


##  Set title


##  So with our tips dataset:



##############################################################################
##  Categorical Data Plots
##----------------------------------------------------------------------------
"""
   Now let's discuss using seaborn to plot categorical data! 
   There are a few main plot types for this:
       - factorplot
       - boxplot
       - violinplot
       - stripplot
       - swarmplot
       - barplot
       - countplot
"""
import seaborn as sns
# get_ipython().run_line_magic('matplotlib', 'inline')




## barplot and countplot
"""
   * These very similar plots allow you to get aggregate data off a 
     categorical feature in your data. 
     
   * barplot is a general plot that allows you to aggregate the categorical 
     data based off some function, by default the mean:
"""


"""
   * You can change the estimator object to your own function, that converts 
     a vector to a scalar:
"""


### countplot
"""
   * This is essentially the same as barplot except the estimator is 
     explicitly counting the number of occurrences. 
     Which is why we only pass the x value:
"""


## boxplot and violinplot
"""
   * boxplots and violinplots are used to shown the distribution of 
     categorical data. 
     
   * A box plot (or box-and-whisker plot) shows the distribution of 
     quantitative data in a way that facilitates comparisons between 
     variables or across levels of a categorical variable. 
     - The box shows the quartiles of the dataset while the whiskers 
       extend to show the rest of the distribution, except for points that 
       are determined to be “outliers” using a method that is a function of t
       he inter-quartile range.
"""


# Can do entire dataframe with orient='h'


### violinplot
"""
   * A violin plot plays a similar role as a box and whisker plot. 
     - It shows the distribution of quantitative data across several levels 
       of one (or more) categorical variables such that those distributions 
       can be compared. 
     - Unlike a box plot, in which all of the plot components correspond 
       to actual datapoints, the violin plot features a kernel density 
       estimation of the underlying distribution.
"""


## stripplot and swarmplot
"""
   * The stripplot will draw a scatterplot where one variable is categorical. 
     - A strip plot can be drawn on its own, but it is also a good complement 
       to a box or violin plot in cases where you want to show all 
       observations along with some representation of the underlying 
       distribution.

   * The swarmplot is similar to stripplot(), but the points are adjusted 
     (only along the categorical axis) so that they don’t overlap. 
     - This gives a better representation of the distribution of values, 
       although it does not scale as well to large numbers of observations 
       (both in terms of the ability to show all the points and in terms of 
       the computation needed to arrange them).
"""


### Combining Categorical Plots


## factorplot
"""
   * factorplot is the most general form of a categorical plot. 
     - It can take in a **kind** parameter to adjust the plot type.
"""



##############################################################################
##  Matrix Plots
##----------------------------------------------------------------------------
"""
   * Matrix plots allow you to plot data as color-encoded matrices and can 
     also be used to indicate clusters within the data (later in the machine 
     learning section we will learn how to formally cluster data).

   * Let's begin by exploring seaborn's heatmap and clutermap.
"""
import seaborn as sns
# get_ipython().run_line_magic('matplotlib', 'inline')


## Heatmap
"""
   * In order for a heatmap to work properly, your data should already be in 
     a matrix form, the sns.heatmap function basically just colors it in for 
     you. 
"""


# Matrix form for correlation data


# Or for the flights data:



## clustermap
"""
   * The clustermap uses hierarchal clustering to produce a clustered version 
     of the heatmap.
"""


"""
   * Notice now how the years and months are no longer in order, instead they 
     are grouped by similarity in value (passenger count). 
     
   * That means we can begin to infer things from this plot, such as August 
     and July being similar (makes sense, since they are both summer 
     travel months)
"""

# More options to get the information a little clearer like normalization



##############################################################################
##  Grids
##----------------------------------------------------------------------------
"""
   * Grids are general types of plots that allow you to map plot types to 
     rows and columns of a grid, this helps you create similar plots 
     separated by features.
"""


## PairGrid
"""
   * Pairgrid is a subplot grid for plotting pairwise relationships in a 
     dataset.
"""

# Just the Grid

# Then you map to the grid

# Map to upper,lower, and diagonal


## pairplot
"""
   * pairplot is a simpler version of PairGrid (you'll use quite often)
"""


## Facet Grid
"""
   * FacetGrid is the general way to create grids of plots based off of a 
     feature.
"""

# Just the Grid


# Notice hwo the arguments come after plt.scatter call


## JointGrid
"""
   * JointGrid is the general version for jointplot() type grids.
"""




##############################################################################
##  Regression Plots
##----------------------------------------------------------------------------
"""
   * Seaborn has many built-in capabilities for regression plots, however we 
     won't really discuss regression until the machine learning section of 
     the course, so we will only cover the **lmplot()** function for now.

   **lmplot** allows you to display linear models, but it also conveniently 
     allows you to split up those plots based off of features, as well as 
     coloring the hue based off of features.
"""

## lmplot()

### Working with Markers
"""
   * lmplot kwargs get passed through to **regplot** which is a more general 
     form of lmplot(). 
     
   * regplot has a scatter_kws parameter that gets passed to plt.scatter. 
     So you want to set the s parameter in that dictionary, which corresponds 
     (a bit confusingly) to the squared markersize. 
     - In other words you end up passing a dictionary with the base matplotlib 
       arguments, in this case, s for size of a scatter plot. 
     - In general, you probably won't remember this off the top of your head, 
       but instead reference the documentation.
"""
# http://matplotlib.org/api/markers_api.html


## Using a Grid
"""
   * We can add more variable separation through columns and rows with the 
     use of a grid. 
     - Just indicate this with the col or row arguments.
"""

## Aspect and Size
"""
   * Seaborn figures can have their size and aspect ratio adjusted with 
     the **size** and **aspect** parameters:
"""


    
##############################################################################
##  Style and Color
"""
   * We've shown a few times how to control figure aesthetics in seaborn, 
     but let's now go over it formally.
"""


## Styles
"""
   * You can set particular styles.
"""


## Spine Removal


## Size and Aspect
"""
   * You can use matplotlib's **plt.figure(figsize=(width,height) ** to 
     change the size of most seaborn plots.

   * You can control the size and aspect ratio of most seaborn grid plots by 
     passing in parameters: size, and aspect. 
"""
# Non Grid Plot

# Grid Type Plot


## Scale and Context
"""
   * The set_context() allows you to override default parameters.
"""


# Check out the documentation page for more info on these topics:
# https://stanford.edu/~mwaskom/software/seaborn/tutorial/aesthetics.html


