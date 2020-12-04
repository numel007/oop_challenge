from Welcome import Welcome

class Savory(Welcome):
    """Instantiate with username"""

    def __init__(self, username, hunger = True, chosen_item = ""):
        super().__init__(username)
        self.hunger = hunger
        self.chosen_item = chosen_item


    def change_name(self):
        """Change user's name"""

        new_name = input("What would you like your new name to be? ")
        self.username = new_name
        print(f"User's name changed to: {self.username}")


    def known_info(self):
        """Prints user's information"""

        print(f"Username: {self.username}")
        print(f"{self.username} wants savory")


    def display_categories(self):
        """Display category options"""

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