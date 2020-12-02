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


# Inherits username, displays recipe options
class Savory(Welcome):
    def __init__(self, username, hunger = True, chosen_item = ""):
        super().__init__(username, hunger)
        self.chosen_item = ""

    def known_info(self):
        """Prints user's information"""

        print(f"Username: {self.username}")
        print(f"{self.username} wants savory")

    def display_recipes(self):
        """Display savory recipes"""

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


#------------------- Object Creation -------------------
test_user = Savory("testuser")
test_user.known_info()
test_user.display_recipes()