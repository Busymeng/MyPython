####
# Place Source Header here!
####

from operator import itemgetter
import csv
import pylab as py

def open_file():
    '''
        Write docstring here!
            
    '''
    
    pass
    

def read_journal_file(fp):
    '''
        Write docstring here!
            
    '''
    
    pass

def read_category_file(fp):
    '''
        Write docstring here!
            
    '''
    
    pass

def display_table(data):
    '''
        Write docstring here!
            
    '''
    
    pass
    
def sort_data(data, column):
    '''
        Write docstring here!
            
    '''
    
    
   pass

def prepare_plot_data(data):
    '''
        Write docstring here!
            
    '''
    
    pass

def plot_data(name,impact_factor):
    '''
        Plots the bar chart of the Journal Impact Factor
        
        Input:
            data (list) -> List of journals and their impact factor
            
        Returns:
            None
    '''
    
    
    py.barh(name,impact_factor)

    py.title("Journal Impact Factor")
    py.xlabel('Impact Factor')
    py.ylabel('Journal Name')
    
    py.show()
    

def main():
    
    pass

if __name__ == "__main__":
    main()