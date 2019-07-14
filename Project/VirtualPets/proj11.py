from cse231_random import randint
from edible import *

MIN, MAX = 0, 10
dog_edible_items = [DogFood]
cat_edible_items = [CatFood]
dog_drinkable_items = [Water]
cat_drinkable_items = [Water]

class Pet(object):
    def __init__(self, name='fluffy', species='dog', gender='male',color='white'):
	# insert docstring
        # modify the following code
        self._name = None
        self._species = None
        self._gender = None
        self._color = None
        self._edible_items = None
        self._drinkable_items = None

        self._hunger = None
        self._thirst = None
        self._smell = None
        self._loneliness = None
        self._energy = None

        self._reply_to_master('newborn')

    def _time_pass_by(self, t=1):
        # this function is complete
        self._hunger = min(MAX, self._hunger + (0.2 * t))
        self._thirst = min(MAX, self._thirst + (0.2 * t))
        self._smell = min(MAX, self._smell + (0.1 * t))
        self._loneliness = min(MAX, self._loneliness + (0.1 * t))
        self._energy = max(MIN, self._energy - (0.2 * t))

    def get_hunger_level(self):
	# insert docstring
        pass  # replace with your code

    def get_thirst_level(self):
	# insert docstring
        pass  # replace with your code

    def get_energy_level(self):
	# insert docstring
        pass  # replace with your code
    
    def drink(self, liquid):
	# insert docstring
        if isinstance(liquid, tuple(self._drinkable_items)):
		pass  # replace with your code
	else:
		pass  # replace with your code
        
        self._update_status()

    def feed(self, food):
	# insert docstring
        if isinstance(food, tuple(self._edible_items)):
		pass  # replace with your code
	else:
		pass  # replace with your code

        self._update_status()


    def shower(self):
	# insert docstring
	pass  # replace with your code

    def sleep(self):
	# insert docstring
	pass  # replace with your code

    def play_with(self):
	# insert docstring
	pass  # replace with your code

    def _reply_to_master(self, event='newborn'):
	# insert docstring
        # this function is complete #
        faces = {}
        talks = {}
        faces['newborn'] = "(๑>◡<๑)"
        faces['feed'] = "(๑´ڡ`๑)"
        faces['drink'] = "(๑´ڡ`๑)"
        faces['play'] = "(ฅ^ω^ฅ)"
        faces['sleep'] = "୧(๑•̀⌄•́๑)૭✧"
        faces['shower'] = "( •̀ .̫ •́ )✧"

        talks['newborn'] = "Hi master, my name is {}.".format(self._name)
        talks['feed'] = "Yummy!"
        talks['drink'] = "Tasty drink ~"
        talks['play'] = "Happy to have your company ~"
        talks['sleep'] = "What a beautiful day!"
        talks['shower'] = "Thanks ~"

        s = "{} ".format(faces[event])  + ": " + talks[event]
        print(s)

    def show_status(self):
	# insert docstring
        # partially formatted string for your guidance
        #s = "{:<12s}: [{:<20s}]".format() + "{:5.2f}/{:2d}".format()
        pass  # replace with your code
        
    def _update_status(self):
	# insert docstring
        # this function is complete #
        faces = {}
        talks = {}
        faces['default'] = "(๑>◡<๑)"
        faces['hunger'] = "(｡>﹏<｡)"
        faces['thirst'] = "(｡>﹏<｡)"
        faces['energy'] = "(～﹃～)~zZ"
        faces['loneliness'] = "(๑o̴̶̷̥᷅﹏o̴̶̷̥᷅๑)"
        faces['smell'] = "(๑o̴̶̷̥᷅﹏o̴̶̷̥᷅๑)"

        talks['default'] = 'I feel good.'
        talks['hunger'] = 'I am so hungry ~'
        talks['thirst'] = 'Could you give me some drinks? Alcohol-free please ~'
        talks['energy'] = 'I really need to get some sleep.'
        talks['loneliness'] = 'Could you stay with me for a little while ?'
        talks['smell'] = 'I am sweaty'

class Cat(Pet):
	# insert docstring
    	# your code goes here #
        
class Dog(Pet):
	# insert docstring
    	# your code goes here #

def main():
    print("Welcome to this virtual pet game!")
    prompt = "Please input the species (dog or cat), name, gender (male / female), fur color of your pet, seperated by space \n ---Example input:  [dog] [fluffy] [male] [white] \n (Hit Enter to use default settings): "

    # error checking for user input
    # your code goes here #

    # create a pet object
    # your code goes here #

    intro = "\nYou can let your pet eat, drink, get a shower, get some sleep, or play with him or her by entering each of the following commands:\n --- [feed] [drink] [shower] [sleep] [play]\n You can also check the health status of your pet by entering:\n --- [status]."
    print(intro)

    prompt = "\n[feed] or [drink] or [shower] or [sleep] or [play] or [status] ? (q to quit): "

    # your code to handle commands goes here

    print("Bye ~")

if __name__ == "__main__":
    main()
