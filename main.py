# Welcome class, includes username entry, hunger status input, change name option
class Welcome:

    # Instantiate user with a name and hunger automatically set to True
    def __init__(self, username, hunger = True):
        self.username = username
        self.hunger = hunger


    def known_info(self):
        """Prints current user's information"""

        print(f"Username: {self.username}")
        print(f"Hunger Status: {self.hunger}")


    def is_hungry(self):
        """Is the user hungry?"""

        # Alter hunger class attribute to whatever user inputs
        while True:
            hunger_status = input("Are you hungry? Y/N ")

            if hunger_status.upper() == "Y":
                self.hunger = True
                break
            elif hunger_status.upper() == "N":
                self.hunger = False
                break
            else:
                print("Invalid hunger status. Try again.")
                continue
        
        print(f"Hunger status set to {self.hunger}")


    def change_name(self):
        """Change user's name"""

        new_name = input("What would you like your new name to be? ")
        self.username = new_name
        print(f"User's name changed to: {self.username}")


# Inherits from Welcome class, provides method to display savory recipe options
class Savory(Welcome):

    # Instantiate object with inherited username and empty chosen_item
    def __init__(self, username, hunger = True, chosen_item = ""):
        super().__init__(username)
        self.chosen_item = ""


    def change_name(self):
        """Change user's name"""

        new_name = input("What would you like your new name to be? ")
        self.username = new_name
        print(f"User's name changed to: {self.username}")


    def known_info(self):
        """Prints user's information"""

        print(f"Username: {self.username}")
        print(f"{self.username} wants savory")


    def display_recipes(self):
        """Display recipes"""

        while True:
            recipe_name = input("What tickles your fancy today? Some good ol' meat between buns or an Italian pie? ")

            if recipe_name.lower() == "burger" or recipe_name.lower() == "meat between buns" or recipe_name.lower() == "meat":
                print("I see you want a burger.")
                self.chosen_item = "burger"
                break
            elif recipe_name.lower() == "pizza" or recipe_name.lower() == "italian pie" or recipe_name.lower() == "pie":
                print("I see you want a pizza.")
                self.chosen_item = "pizza"
                break
            else:
                print("I have no idea what that is my dude. Try again.")
                continue

        return self.chosen_item


# Inherits from Welcome class, provides method to display sweet recipe options
class Sweet(Welcome):

    # Instantiate object with inherited username and empty chosen_item
    def __init__(self, username, hunger = True, chosen_item = ""):
        super().__init__(username)


    def change_name(self):
        """Change user's name"""

        new_name = input("What would you like your new name to be? ")
        self.username = new_name
        print(f"User's name changed to: {self.username}")


    def known_info(self):
        """Prints user's information"""

        print(f"Username: {self.username}")
        print(f"{self.username} wants sweet")


    def display_recipes(self):
        """Display recipes"""

        while True:
            recipe_name = input("A bit of a sweet tooth eh? I've got flan and bread pudding on the menu. What'll it be? ")

            if recipe_name.lower() == "flan":
                print("I see you want flan.")
                self.chosen_item = "flan"
                break
            elif recipe_name.lower() == "bread pudding":
                print("I see you want bread pudding.")
                self.chosen_item = "bread pudding"
                break
            else:
                print("I have no idea what that is my dude. Try again.")
                continue

        return self.chosen_item


class Burger(Savory):

    def __init__(self, username, type = 0, patties_count = 0, ingredients = []):
        super().__init__(username)

    def burger_type(self):
        """Does the user want a sandwhich or burger?"""

    def burger_creator(self):
        """Create a burger graphic from user inputs"""

        # Create variables with graphics pertaining to ingredients
        top_bun = " ┌──────┐"
        patty = "▄▄▄▄▄▄▄▄▄▄"
        lettuce = " ~~~~~~~~"
        pickle = " ********"
        tomato = " oooooooo"
        cheese = "──────────"
        bottom_bun = " └──────┘"

        # Automatically add a bun to ingredients list. A burger isn't a burger without a bun. I don't care if you're on keto.
        burger_ingredients = [top_bun]

        while True:
            # Ingredient selection prompt
            new_ingredient = (input("\n Choose an ingredient: \n 1. Patty \n 2. Lettuce \n 3. Pickle \n 4. Tomato \n 5. Cheese \n 6. Done \n Your Choice: ")).lower()

            # Append ingredient to list or end loop
            if new_ingredient == "1" or new_ingredient == "patty":
                burger_ingredients.append(patty)
                print("Patty added")
                continue
            elif new_ingredient == "2" or new_ingredient == "lettuce":
                burger_ingredients.append(lettuce)
                print("Lettuce added")
                continue
            elif new_ingredient == "3" or new_ingredient == "pickle":
                burger_ingredients.append(pickle)
                print("Pickle(s) added")
                continue
            elif new_ingredient == "4" or new_ingredient == "tomato":
                burger_ingredients.append(tomato)
                print("Tomato added")
                continue
            elif new_ingredient == "5" or new_ingredient == "cheese":
                burger_ingredients.append(cheese)
                print("Cheese added")
                continue
            elif new_ingredient == "6" or new_ingredient == "done":
                print("Burger completed \n")
                burger_ingredients.append(bottom_bun)
                break
            else:
                print("Invalid option")
                continue

        # Present the burger to the user
        if len(burger_ingredients) == 2:
            print(top_bun)
            print("")
            print(bottom_bun)
            print("You really just wanted buns, hun?")
        else:
            print("\n Here's your burger \n")
            for item in burger_ingredients:
                print(item)


#------------------- Object Creation -------------------

test_user = Burger("testuser")
test_user.burger_creator()