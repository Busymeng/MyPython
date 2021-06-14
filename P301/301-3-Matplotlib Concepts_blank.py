##############################################################################
##  Introduction to Matplotlib
##---------------------------------------------------------------------------- 
"""
   * Matplotlib is the "grandfather" library of data visualization with Python. 
     
   * It was created by John Hunter. He created it to try to replicate MatLab's 
     (another programming language) plotting capabilities in Python. So if you 
     happen to be familiar with matlab, matplotlib will feel natural to you.
     
   * It is an excellent 2D and 3D graphics library for generating scientific 
     figures. 
     
   * Some of the major Pros of Matplotlib are:
     - Generally easy to get started for simple plots
     - Support for custom labels and texts
     - Great control of every element in a figure
     - High-quality output in many formats
     - Very customizable in general
     
   * Matplotlib allows you to create reproducible figures programmatically. 
     Let's learn how to use it! Before continuing this lecture, I encourage 
     you just to explore the official Matplotlib web page: 
     http://matplotlib.org/
     
   * Installation
     - You'll need to install matplotlib first with either:
          conda install matplotlib
       or
          pip install matplotlib
          
   * Importing
     - Import the 'matplotlib.pyplot' module under the name 'plt'
"""
import matplotlib.pyplot as plt

##  You'll also need to use this line to see plots in the notebook:
##  'get_ipython().run_line_magic('matplotlib', 'inline')'


##  That line is only for jupyter notebooks, if you are using another editor, 
##  you'll use: plt.show() at the end of all your plotting commands to have 
##  the figure pop up in another window.


##############################################################################
##  Example
##---------------------------------------------------------------------------- 
"""
   * Let's walk through a very simple example using two numpy arrays. 
   
   * You can also use lists, but most likely you'll be passing numpy arrays 
     or pandas columns (which essentially also behave like arrays).
""" 

##  The data we want to plot:



##  Basic Matplotlib Commands
"""
   * We can create a very simple line plot using the following ( I encourage 
     you to pause and use Shift+Tab along the way to check out the document 
     strings for the functions we are using).
"""




##  Creating Multiplots on Same Canvas

##  plt.subplot(nrows, ncols, plot_number)


##############################################################################
##  Matplotlib Object Oriented Method
##---------------------------------------------------------------------------- 
"""
   * Now that we've seen the basics, let's break it all down with a more 
     formal introduction of Matplotlib's Object Oriented API. 
     
   * This means we will instantiate figure objects and then call methods or 
     attributes from that object.
     
   * The main idea in using the more formal Object Oriented method is to 
     create figure objects and then just call methods or attributes off of 
     that object. 
     
   * This approach is nicer when dealing with a canvas that has multiple plots 
     on it. 
""" 

##  To begin we create a figure instance. Then we can add axes to that figure:

##  Create Figure (empty canvas)


##  Add set of axes to figure
##    left, bottom, width, height (range 0 to 1)


##  Plot on that set of axes



##  Code is a little more complicated, but the advantage is that we now have 
##  full control of where the plot axes are placed, and we can easily add more 
##  than one axis to the figure:

# Creates blank canvas


# Larger Figure Axes 1


# Insert Figure Axes 2



##############################################################################
##  subplots()
##---------------------------------------------------------------------------- 
"""
   * The plt.subplots() object will act as a more automatic axis manager.
""" 
##  Basic use cases:

##  Use similar to plt.figure() except use tuple unpacking to grab fig and axes


##  Now use the axes object to add stuff to plot


##  Then you can specify the number of rows and columns when creating the 
##  subplots() object:

##  Empty canvas of 1 by 2 subplots


##  Axes is an array of axes to plot on


##  We can iterate through this array:


##  Display the figure object    


##  A common issue with matplolib is overlapping subplots or figures. 
##  We ca use fig.tight_layout() or plt.tight_layout() method, which 
##  automatically adjusts the positions of the axes on the figure canvas 
##  so that there is no overlapping content:




##############################################################################
##  Figure size, aspect ratio and DPI
##---------------------------------------------------------------------------- 
"""
   * Matplotlib allows the aspect ratio, DPI and figure size to be specified 
     when the Figure object is created. 
     
   * You can use the 'figsize' and 'dpi' keyword arguments. 
     - 'figsize' is a tuple of the width and height of the figure in inches
     - 'dpi' is the dots-per-inch (pixel per inch).
""" 


##  The same arguments can also be passed to layout managers, such as the 
##  `subplots` function:



##############################################################################
##  Saving figures
##---------------------------------------------------------------------------- 
"""
   * Matplotlib can generate high-quality output in a number formats, 
     including PNG, JPG, EPS, SVG, PGF and PDF. 
     
   * To save a figure to a file we can use the savefig() method in the 
     Figure class.
""" 


## Here we can also optionally specify the DPI and choose between different 
## output formats:



##############################################################################
##  Legends, labels and titles
##---------------------------------------------------------------------------- 
"""
   * Now that we have covered the basics of how to create a figure canvas 
     and add axes instances to the canvas, let's look at how decorate a figure 
     with titles, axis labels, and legends.
""" 
##  Figure titles
"""
   * A title can be added to each axis instance in a figure. 
   * To set the title, use the set_title() method in the axes instance.
"""



##  Axis labels
"""
   * Similarly, with the methods set_xlabel() and set_ylabel(), we can set 
     the labels of the X and Y axes.
"""



##  Legends
"""
   * You can use the label="label text" keyword argument when plots or other 
     objects are added to the figure, and then using the legend() method 
     without arguments to add the legend to the figure.
"""


## Notice how are legend overlaps some of the actual plot!
"""
   * The legend() function takes an optional keyword argument "loc" that 
     can be used to specify where in the figure the legend is to be drawn. 
     - The allowed values of "loc" are numerical codes for the various places 
       the legend can be drawn. 
       See the [documentation page]
       (http://matplotlib.org/users/legend_guide.html#legend-location) 
       for details. 
       
   * Some of the most common **loc** values are:
"""
# Lots of options....


# Most common to choose


##############################################################################
##  Setting colors, linewidths, linetypes
##---------------------------------------------------------------------------- 
"""
   * Matplotlib gives you *a lot* of options for customizing colors, 
     linewidths, and linetypes.
     
   * There is the basic MATLAB like syntax (which I would suggest you avoid 
     using for more clairty sake).
   
   * With matplotlib, we can define the colors of lines and other graphical 
     elements in a number of ways. 
     - First of all, we can use the MATLAB-like syntax where "b" means blue, 
       "g" means green, etc. 
     - The MATLAB API for selecting line styles are also supported: where, 
       for example, 'b.-' means a blue line with dots.
""" 
##  MATLAB style line color and style 


##  Colors with the color= parameter
"""
   * We can also define colors by their names or RGB hex codes and optionally 
     provide an alpha value using the `color` and `alpha` keyword arguments. 
     - Alpha indicates opacity.
"""



##  Line and marker styles
"""
   * To change the line width, we can use the 'linewidth' or 'lw' keyword 
     argument. 
   * The line style can be selected using the 'linestyle' or 'ls' keyword 
     arguments.
"""


##  possible linestype options ‘-‘, ‘–’, ‘-.’, ‘:’, ‘steps’


##  custom dash


##  possible marker symbols: marker = '+', 'o', '*', 's', ',', '.', '1', 
##                                    '2', '3', '4', ...


##  marker size and color



##############################################################################
##  Control over axis appearance
##---------------------------------------------------------------------------- 
"""
   * In this section we will look at controlling axis sizing properties in a 
     matplotlib figure.
""" 
##  Plot range
"""
   * We can configure the ranges of the axes using the set_ylim() and 
     set_xlim() methods in the axis object, or axis('tight') for automatically 
     getting "tightly fitted" axes ranges.
"""



##  Special Plot Types
"""
   * There are many specialized plots we can create, such as barplots, 
     histograms, scatter plots, and much more. 
     
   * Most of these type of plots we will actually create using seaborn, 
     a statistical plotting library for Python. But here are a few examples 
     of these type of plots.
"""


# rectangular box plot
 



##############################################################################
##  Advanced Matplotlib Concepts
##---------------------------------------------------------------------------- 
"""
   * In this lecture we  cover some more advanced topics which you won't 
     usually use as often. You can always reference the documentation for 
     more resources!
""" 
##  Logarithmic scale
"""
   * It is also possible to set a logarithmic scale for one or both axes. 
   * This functionality is in fact only one application of a more general 
     transformation system in Matplotlib. 
   * Each of the axes' scales are set seperately using set_xscale() and 
     set_yscale() methods which accept one parameter (with the value "log" 
     in this case).
"""



##  Placement of ticks and custom tick labels
"""
   * We can explicitly determine where we want the axis ticks with set_xticks()
     and set_yticks(), which both take a list of values for where on the axis 
     the ticks are to be placed. 
     
   * We can also use the set_xticklabels() and set_yticklabels() methods to 
     provide a list of custom text labels for each tick location.
     
   * There are a number of more advanced methods for controlling major and 
     minor tick placement in matplotlib figures, such as automatic placement 
     according to different policies. 
     See http://matplotlib.org/api/ticker_api.html for details.
"""


# use LaTeX formatted labels



##  Scientific notation
"""
   * With large numbers on axes, it is often better use scientific notation.
"""



##  Axis number and axis label spacing

# distance between x and y axis and the numbers on the axes



##  padding between axis label and axis numbers



##  restore defaults


##  Axis position adjustments
"""
   * Unfortunately, when saving figures the labels are sometimes clipped, 
     and it can be necessary to adjust the positions of axes a little bit. 
     - This can be done using subplots_adjust().
"""



##  Axis grid
"""
   * With the grid() method in the axis object, we can turn on and off 
     grid lines. 
     
   * We can also customize the appearance of the grid lines using the same 
     keyword arguments as the plot() function.
"""


##  default grid appearance


##  custom grid appearance



##  Axis spines

##  We can also change the properties of axis spines:


##  turn off axis spine to the right



## Twin axes
"""
   * Sometimes it is useful to have dual x or y axes in a figure; for example, 
     when plotting curves with different units together. 
     
   * Matplotlib supports this with the twinx() and twiny() functions.
"""



##  Axes where x and y is zero



##  Other 2D plot styles
"""
   * In addition to the regular plot() method, there are a number of other 
     functions for generating different kind of plots. 
     
   * See the matplotlib plot gallery for a complete list of available plot 
     types: http://matplotlib.org/gallery.html. 
"""


##  Text annotation
"""
   * Annotating text in matplotlib figures can be done using the text() 
     function. 
     
   * It supports LaTeX formatting just like axis label texts and titles.
"""


##  Figures with multiple subplots and insets
"""
   * Axes can be added to a matplotlib Figure canvas manually using 
     fig.add_axes() or using a sub-figure layout manager such as subplots(), 
     subplot2grid(), or gridspec().
"""
##  subplots



##  subplot2grid



##  gridspec


##  add_axes
"""
   * Manually adding axes with add_axes() is useful for adding insets 
     to figures.
"""


##  inset


##  set axis range


##  set axis tick locations



##  Colormap and contour figures
"""
   * Colormaps and contour figures are useful for plotting functions of two 
     variables. 
     
   * In most of these functions we will use a colormap to encode one dimension 
     of the data. 
     
   * There are a number of predefined colormaps. It is relatively 
     straightforward to define custom colormaps. 
     
   * For a list of pre-defined colormaps, 
     see: http://www.scipy.org/Cookbook/Matplotlib/Show_colormaps
"""



##  pcolor




## imshow



## contour


##  3D figures
"""
   * To use 3D graphics in matplotlib, we first need to create an instance 
     of the Axes3D() class. 
     
   * 3D axes can be added to a matplotlib figure canvas in exactly the same 
     way as 2D axes; or, more conveniently, by passing a "projection='3d'" 
     keyword argument to the add_axes() or add_subplot() methods.
"""


##  Surface plots


##  `ax` is a 3D-aware axis instance because of the projection='3d' keyword 
##  argument to add_subplot


##  surface_plot with color grading and color bar



## Wire-frame plot


## Coutour plots with projections





##############################################################################
##  Further reading
##---------------------------------------------------------------------------- 
"""
   * The project web page for matplotlib
     http://www.matplotlib.org
     
   * The source code for matplotlib
     https://github.com/matplotlib/matplotlib
     
   * A large gallery showcaseing various types of plots matplotlib can create. 
     Highly recommended!
     http://matplotlib.org/gallery.html 
     
   * A good matplotlib tutorial
     http://www.loria.fr/~rougier/teaching/matplotlib
     
   * Another good matplotlib reference
     http://scipy-lectures.github.io/matplotlib/matplotlib.html

""" 