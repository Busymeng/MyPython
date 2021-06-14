##############################################################################
##  Pandas Built-in Data Visualization
##----------------------------------------------------------------------------
""" 
   * In this lecture we will learn about pandas built-in capabilities for 
     data visualization! 
     - It's built-off of matplotlib, but it baked into pandas for easier usage!  
"""
## Imports



## The Data
"""
   * There are some fake data csv files you can read in as dataframes.
"""


## Style Sheets
"""
   * Matplotlib has [style sheets]
     (http://matplotlib.org/gallery.html#style_sheets) you can use to make 
     your plots look a little nicer. 
     - These style sheets include plot_bmh,plot_fivethirtyeight,plot_ggplot 
       and more. 
     - They basically create a set of style rules that your plots follow. 
     - I recommend using them, they make all your plots have the same look 
       and feel more professional. 
     - You can even create your own if you want your company's plots to all 
       have the same look (it is a bit tedious to create on though).
"""

# **Before plt.style.use() your plots look like this:**


# Call the style:



# Now your plots look like this:



# Let's stick with the ggplot style and actually show you how to utilize 
# pandas built-in plotting capabilities!

# Plot Types
"""
  There are several plot types built-in to pandas, most of them statistical 
  plots by nature:

    * df.plot.area     
    * df.plot.barh     
    * df.plot.density  
    * df.plot.hist     
    * df.plot.line     
    * df.plot.scatter
    * df.plot.bar      
    * df.plot.box      
    * df.plot.hexbin   
    * df.plot.kde      
    * df.plot.pie

   You can also just call df.plot(kind='hist') or replace that kind argument 
   with any of the key terms shown in the list above (e.g. 'box','barh', 
   etc..)
"""
## Area

## Barplots


## Histograms

## Line Plots

## Scatter Plots


"""
   * You can use c to color based off another column value.
   * Use cmap to indicate colormap to use. 
   * For all the colormaps, check out: 
       http://matplotlib.org/users/colormaps.html
"""


"""
   * Or use s to indicate size based off another column. s parameter needs to 
     be an array, not just the name of a column.
"""

## BoxPlots

## Hexagonal Bin Plot
"""
   * Useful for Bivariate Data, alternative to scatterplot.
"""


## Kernel Density Estimation plot (KDE)


