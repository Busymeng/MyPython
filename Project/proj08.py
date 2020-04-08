from operator import itemgetter # optional, if you use itemgetter when sorting
import matplotlib.pyplot as plt

def Open_file(): 
    '''
        Place Docstring here!
    '''
    
    pass


def Get_athlete_stats(fp): 
    '''
        Place Docstring here!
    '''
    
    pass


def Get_country_stats(fp, Athlete): 
    '''
        Place Docstring here!
    '''
    
    pass


def Display_best_athletes_per_sport(Athlete, Country, Sports):
    '''
        Place Docstring here!
    '''
    
    pass

def Display_top_countries_by_sport(Country, answer):
    '''
        Place Docstring here!
    '''
       
    pass

def Prepare_plot(Country_lst):
    
    '''
        Place Docstring here!
    '''
    
    pass

def plot_country_medals_per_year(year, gold, silver, bronze, country):
    
    plt.plot(year, gold, 'yo')
    plt.plot(year, silver, 'bs')
    plt.plot(year, bronze, 'ro')
    plt.title("Number of Medals Over the Years For {}".format(country))
    plt.xlabel('Years'), plt.ylabel('Number of medals')
    plt.legend(['gold','silver','bronze'])
    plt.show()
    
def main():
    '''
        Place Docstring here!
    '''
    
    pass

###### Main Code ######
if __name__ == "__main__":
    main()
