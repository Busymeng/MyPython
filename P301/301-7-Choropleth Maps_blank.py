##############################################################################
##  Choropleth Maps
##----------------------------------------------------------------------------

## Offline Plotly Usage
"""
   * Get imports and set everything up to be working offline.
"""


# Now set up everything so that the figures show up in the notebook:


# More info on other options for Offline Plotly usage can be found [here]
# (https://plot.ly/python/offline/).

## Choropleth US Maps
"""
   * Plotly's mapping can be a bit hard to get used to at first, remember to 
     reference the cheat sheet in the data visualization folder, or [find it 
     online here](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf).
"""


# Now we need to begin to build our data dictionary. 
# Easiest way to do this is to use the **dict()** function of the general form:
"""
    * type = 'choropleth',
    * locations = list of states
    * locationmode = 'USA-states'
    * colorscale= 
    
    Either a predefined string:
    
        'pairs' | 'Greys' | 'Greens' | 'Bluered' | 'Hot' | 'Picnic' | 'Portland' | 'Jet' | 'RdBu' | 'Blackbody' | 'Earth' | 'Electric' | 'YIOrRd' | 'YIGnBu'
    
    or create a [custom colorscale](https://plot.ly/python/heatmap-and-contour-colorscales/)
    
    * text= list or array of text to display per point
    * z= array of values on z axis (color of state)
    * colorbar = {'title':'Colorbar Title'})
"""
# Here is a simple example:


# Then we create the layout nested dictionary:



# Then we use: 
# 
#     go.Figure(data = [data],layout = layout)
#     
# to set up the object that finally gets passed into iplot()


### Real Data US Map Choropleth
"""
   * Now let's show an example with some real data as well as some other 
     options we can add to the dictionaries in data and layout.
"""

# Now out data dictionary with some extra marker and colorbar arguments:

# And our layout dictionary with some more arguments:


# # World Choropleth Map
# 
# Now let's see an example with a World Map:


# # Great Job!
