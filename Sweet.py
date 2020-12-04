from Welcome import Welcome

# Inherits username from Welcome class, provides method to display sweet recipe options
class Sweet(Welcome):
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
        print(f"{self.username} wants sweet")


    def display_recipes(self):
        """Display recipes"""

        while True:
            recipe_name = input("Got a sweet tooth eh? I've got pie and cake on the menu. What'll it be? ")

            if recipe_name.lower() == "pie":
                print("I see you want pie.")
                self.chosen_item = "pie"
                break
            elif recipe_name.lower() == "cake":
                print("I see you want cake.")
                self.chosen_item = "cake"
                break
            else:
                print("I have no idea what that is my dude. Try again.")
                continue

        return self.chosen_item