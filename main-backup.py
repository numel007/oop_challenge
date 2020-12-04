# Welcome class, includes username entry, hunger status input, change name option
class Welcome:
    """Instantiate with username"""

    def __init__(self, username, hunger=True):
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
        return self.hunger

    def change_name(self):
        """Change user's name"""

        new_name = input("What would you like your new name to be? ")
        self.username = new_name
        print(f"User's name changed to: {self.username}")

    def savory_or_sweet(self):
        """Pick which food category to switch to"""

        selected_option = (input("Savory or sweet? ")).lower()

        if selected_option == "savory":
            user = Savory(self.username)
            user.display_categories()
        elif selected_option == "sweet":
            user = Sweet(self.username)
            user.display_recipes()
        else:
            print("invalid input")


# Inherits username from Welcome class, provides method to display savory recipe options
class Savory(Welcome):
    """Instantiate with username"""

    def __init__(self, username, hunger=True, chosen_item=""):
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
            recipe_name = input(
                "What tickles your fancy today? A burger or pizza? ")

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

        if self.chosen_item == "burger":
            user = Burger(self.username)
            user.burger_creator()
            user.update_total()
        elif self.chosen_item == "pizza":
            user = Pizza(self.username)
            user.pizza_creator()
            user.update_total()


# Inherits username from Welcome class, provides method to display sweet recipe options
class Sweet(Welcome):
    """Instantiate with username"""

    def __init__(self, username, hunger=True, chosen_item=""):
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
            recipe_name = input(
                "Got a sweet tooth eh? I've got pie and cake on the menu. What'll it be? ")

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

        if self.chosen_item == "pie":
            user = Pie(self.username)
            user.pie_picker()
            user.update_total()
        elif self.chosen_item == "pizza":
            user.Cake(self.username)
            user.cake_picker()
            user.update_total()

# Inherits username from Savory class, provides methods for ordering a burger


class Burger(Savory):
    """Instantiate with username"""

    # Burger ingredient costs
    patty_cost = 1.49
    lettuce_cost = 0.05
    pickle_cost = 0.15
    tomato_cost = 0.25
    cheese_cost = 0.75

    def __init__(self, username, total=0, ingredients=[]):
        super().__init__(username)
        self.total = total
        self.ingredients = ingredients

    def change_name(self):
        """Change user's name"""

        new_name = input("What would you like your new name to be? ")
        self.username = new_name
        print(f"User's name changed to: {self.username}")

    def known_info(self):
        """Prints user's information"""

        print(f"Username: {self.username}")
        print(f"{self.username} is ordering a burger.")

    @classmethod
    def update_ingredients_costs(cls):
        """Update class ingredient prices"""

        # Store old prices for later usage
        old_patty_cost = cls.patty_cost
        old_lettuce_cost = cls.lettuce_cost
        old_pickle_cost = cls.pickle_cost
        old_tomato_cost = cls.tomato_cost
        old_cheese_cost = cls.cheese_cost

        # New price prompt
        cls.patty_cost = float(input("Enter new patty cost: $"))
        cls.lettuce_cost = float(input("Enter new lettuce cost: $"))
        cls.pickle_cost = float(input("Enter new pickle cost: $"))
        cls.tomato_cost = float(input("Enter new tomato cost: $"))
        cls.cheese_cost = float(input("Enter new cheese cost: $"))

        # Print comparison of old to new price
        print("")
        print("Updated ingredient prices \n")
        print(f"Patty: ${old_patty_cost} --> ${cls.patty_cost}")
        print(f"Lettuce: ${old_lettuce_cost} --> ${cls.lettuce_cost}")
        print(f"Pickle: ${old_pickle_cost} --> ${cls.pickle_cost}")
        print(f"Tomato: ${old_tomato_cost} --> ${cls.tomato_cost}")
        print(f"Cheese: ${old_cheese_cost} --> ${cls.cheese_cost}")

    def update_total(self):
        """Totals the user's items"""

        for ingredient in self.ingredients:
            if ingredient == "patty":
                self.total += Burger.patty_cost
            elif ingredient == "lettuce":
                self.total += Burger.lettuce_cost
            elif ingredient == "pickle":
                self.total += Burger.pickle_cost
            elif ingredient == "tomato":
                self.total += Burger.tomato_cost
            else:
                self.total += Burger.cheese_cost

        print(f"{self.username}'s total: ${round(self.total, 2)}")
        return round(self.total, 2)

    def burger_creator(self):
        """Create a burger graphic from user inputs"""

        # Graphics pertaining to each ingredient
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
            new_ingredient = (input(
                f"\n Choose an ingredient: \n 1. Patty   ${Burger.patty_cost}\n 2. Lettuce ${Burger.lettuce_cost}\n 3. Pickle  ${Burger.pickle_cost}\n 4. Tomato  ${Burger.tomato_cost}\n 5. Cheese  ${Burger.cheese_cost}\n 6. Done \n Your Choice: ")).lower()

            # Append ingredient to list or end loop
            if new_ingredient == "1" or new_ingredient == "patty":
                self.ingredients += "patty"
                burger_ingredients.append(patty)
                print("Patty added\n")
                continue
            elif new_ingredient == "2" or new_ingredient == "lettuce":
                self.ingredients += "lettuce"
                burger_ingredients.append(lettuce)
                print("Lettuce added\n")
                continue
            elif new_ingredient == "3" or new_ingredient == "pickle":
                self.ingredients += "pickle"
                burger_ingredients.append(pickle)
                print("Pickles added\n")
                continue
            elif new_ingredient == "4" or new_ingredient == "tomato":
                self.ingredients += "tomato"
                burger_ingredients.append(tomato)
                print("Tomatoes added\n")
                continue
            elif new_ingredient == "5" or new_ingredient == "cheese":
                self.ingredients += "cheese"
                burger_ingredients.append(cheese)
                print("Cheese added\n")
                continue
            elif new_ingredient == "6" or new_ingredient == "done":
                print("Order complete.\n")
                burger_ingredients.append(bottom_bun)
                break
            else:
                print("Invalid option. Try again.\n")
                continue

        # Present the burger to the user
        if len(burger_ingredients) == 2:
            print(top_bun)
            print("")
            print(bottom_bun)
            print("You really just want buns, hun?")
        else:
            print("\n Here's your burger!\n")
            for item in burger_ingredients:
                print(item)


# Inherits username from Savory class, provides methods for ordering a pizza
class Pizza(Savory):
    """Instantiate with username"""

    # Pizza prices
    slice_price = 5.99
    ten_in_price = 14.99
    the_jeremiah_special_price = 0.99

    def __init__(self, username, total=0, item_list=[]):
        super().__init__(username)
        self.total = total
        self.item_list = item_list

    def change_name(self):
        """Change user's name"""

        new_name = input("What would you like your new name to be? ")
        self.username = new_name
        print(f"User's name changed to: {self.username}")

    def known_info(self):
        """Prints user's information"""

        print(f"Username: {self.username}")
        print(f"{self.username} is ordering pizza.")

    @classmethod
    def update_pizza_costs(cls):
        """Update class pizza prices"""

        # Store old prices for later usage
        old_slice_cost = cls.slice_price
        old_ten_in_cost = cls.ten_in_price
        old_jeremiah_special_cost = cls.the_jeremiah_special_price

        # New price prompt
        cls.slice_price = float(input("Enter new slice cost: $"))
        cls.ten_in_price = float(input("Enter new 10in pizza cost: $"))
        cls.the_jeremiah_special_price = float(
            input("Enter new Jeremiah Special cost: $"))

        # Print comparison of old to new price
        print("")
        print("Updated pizza prices \n")
        print(f"Slice: ${old_slice_cost}  -->  ${cls.slice_price}")
        print(f"10in pizza: ${old_ten_in_cost}  -->  ${cls.ten_in_price}")
        print(
            f"Jeremiah Special: ${old_jeremiah_special_cost}  -->  ${cls.the_jeremiah_special_price}")

    def update_total(self):
        """Totals the user's items"""

        for item in self.item_list:
            if item == "slice":
                self.total += Pizza.slice_price
            elif item == "10in":
                self.total += Pizza.ten_in_price
            else:
                self.total += Pizza.the_jeremiah_special_price

        print(f"{self.username}'s total: ${round(self.total, 2)}")
        return round(self.total, 2)

    def pizza_creator(self):
        """Add user-picked pizzas to the cart"""

        # Create empty list to store graphics
        graphics = []

        # Pizza graphics
        slice_graphic = """
                                     ._
                                   ,(  `-.
                                 ,': `.   `.
                               ,` *   `-.   |
                             ,'  ` :+  = `.  `.
                           ,~  (o):  .,   `.  `.
                         ,'  ; :   ,(__) x;`.  ;
                       ,'  :'  itz  ;  ; ; _,-'
                     .'O ; = _' C ; ;'_,_ ;
                   ,;  _;   ` : ;'_,-'   i'
                 ,` `;(_)  0 ; ','       :
               .';6     ; ' ,-'~
             ,' Q  ,& ;',-.'
           ,( :` ; _,-'~  ;
         ,~.`c _','
       .';^_,-' ~
     ,'_;-''
    ,,~
                    """
        ten_in_graphic = """                     ___
                    |  ~~--.
                    |%=@%%/
                    |o%%%/
                 __ |%%o/
           _,--~~ | |(_/ ._
        ,/'  m%%%%| |o/ /  `\.
       /' m%%o(_)%| |/ /o%%m `\
     /' %%@=%o%%%o|   /(_)o%%% `\
    /  %o%%%%%=@%%|  /%%o%%@=%%  \
   |  (_)%(_)%%o%%| /%%%=@(_)%%%  |
   | %%o%%%%o%%%(_|/%o%%o%%%%o%%% |
   | %%o%(_)%%%%%o%(_)%%%o%%o%o%% |
   |  (_)%%=@%(_)%o%o%%(_)%o(_)%  |
    \ ~%%o%%%%%o%o%=@%%o%%@%%o%~ /
     \. ~o%%(_)%%%o%(_)%%(_)o~ ,/
       \_ ~o%=@%(_)%o%%(_)%~ _/
         `\_~~o%%%o%%%%%~~_/'
            `--..____,,--'
                                      """
        the_jeremiah_special_graphic = """
                                                                            ░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒░░░░░░
                                                    ░░░░▒▒▒▒▒▒▒▒░░░░░░░░░░  ░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░
                                              ░░░░░░░░▒▒▒▒▒▒░░░░  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓▒▒
                                          ░░░░░░░░░░    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░▒▒▒▒
                                      ░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░▒▒░░░░▒▒░░
                                    ░░▒▒▓▓▓▓▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                                  ▒▒░░░░░░▒▒▒▒░░░░░░░░▒▒▓▓▒▒▒▒▒▒▒▒░░▒▒▒▒░░░░░░░░░░░░░░░░▒▒░░░░▒▒░░░░░░░░░░░░░░░░░░░░▒▒
                              ░░░░░░░░░░░░░░▒▒░░▒▒░░▒▒▒▒▓▓▓▓██▓▓▓▓▒▒░░░░░░░░░░░░░░░░▒▒▓▓████▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░▒▒
                            ░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓████▓▓▓▓▓▓▓▓░░░░░░░░  ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▒▒░░░░░░░░░░░░▒▒░░
                            ░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░  ░░░░░░░░░░░░░░░░░░▒▒▒▒
                          ░░░░░░  ░░░░░░▒▒░░░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▒▒▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓░░  ░░░░░░░░░░░░░░░░▒▒░░░░░░
                      ░░░░░░░░░░░░░░▒▒▓▓░░▒▒░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▒▒▓▓▓▓▓▓▒▒▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░▒▒▒▒░░░░░░░░
                      ░░░░░░░░░░░░▒▒▓▓▒▒▒▒░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓░░░░░░  ▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░▒▒░░
                    ░░░░░░░░░░░░▒▒▒▒░░▒▒▓▓██▓▓▓▓▒▒░░░░▓▓▒▒▓▓▓▓▒▒▒▒▒▒▓▓▒▒░░░░    ░░▓▓▓▓▓▓▒▒▓▓▒▒▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░▒▒▒▒░░░░▒▒░░░░░░
                  ░░░░░░░░░░░░░░▒▒░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░▓▓▓▓▓▓▒▒▓▓▓▓▒▒░░  ░░    ░░▒▒▓▓▓▓▒▒▓▓▒▒▓▓▒▒░░░░░░░░▒▒██▓▓▓▓▓▓▒▒░░░░▒▒▒▒▒▒░░░░░░
                  ▒▒░░░░░░░░▒▒░░░░▒▒▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒░░  ░░░░▓▓▒▒▓▓▒▒░░  ░░░░░░  ░░░░░░▒▒▓▓▓▓▓▓▒▒░░  ░░░░░░▓▓▓▓▒▒▓▓██▓▓▒▒░░░░▒▒▒▒░░░░░░
                ░░░░░░░░░░▒▒▒▒░░░░▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒▒░░░░    ░░░░░░  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    ░░▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░▒▒▒▒▒▒▒▒░░▒▒
                ░░░░░░░░░░░░░░░░░░██▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓░░░░░░░░░░░░░░░░▒▒▒▒▓▓██▓▓▓▓▓▓░░░░░░  ░░░░░░░░    ▒▒▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓░░░░░░▓▓░░░░░░
              ░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░  ░░░░░░░░  ░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░░░▓▓
              ░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓██████▓▓▓▓░░░░    ░░░░░░░░▒▒▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▒▒  ░░░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒░░░░▒▒░░░░▒▒▒▒
              ░░░░░░░░▒▒░░░░░░  ░░░░██▓▓▓▓██▓▓▓▓▓▓░░░░    ░░░░░░░░░░▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓░░░░░░░░░░▒▒▒▒▒▒░░▓▓
            ▒▒░░░░░░░░▒▒░░░░░░░░░░░░░░▓▓▒▒▓▓██░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓▓▓▒▒▒▒▓▓▓▓▓▓░░    ░░░░░░░░░░░░░░▓▓▓▓▒▒▓▓▒▒▓▓░░░░░░░░░░░░░░░░▒▒░░▒▒
            ██░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▒▒░░░░░░▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓░░░░  ░░░░░░░░░░░░  ░░▒▒▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░
            ▒▒░░░░░░▒▒░░░░▒▒▓▓▓▓▓▓▒▒░░░░░░░░░░░░▒▒▓▓▒▒▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▒▒▒▒▓▓▓▓▒▒░░░░░░░░░░▓▓▓▓▓▓▓▓▒▒░░  ░░▒▒░░░░  ░░░░  ░░░░░░░░░░░░▒▒░░▒▒
          ░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░▒▒▓▓▒▒▓▓▓▓▒▒▓▓▓▓░░░░░░░░▓▓▒▒▓▓▓▓▓▓▒▒░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ░░░░░░░░░░░░░░░░░░▒▒░░░░░░▒▒░░▒▒
          ░░░░░░░░▒▒░░▓▓▒▒▓▓▓▓▓▓▓▓▓▓██▒▒░░░░░░░░▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓░░░░░░░░░░▒▒▒▒▓▓░░░░░░░░░░▓▓▓▓▒▒▓▓▓▓▓▓▒▒▓▓░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░░░▒▒░░░░░░
          ▒▒░░░░░░▒▒░░▒▒▓▓▓▓▓▓▓▓▓▓██▓▓▒▒░░░░░░░░▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░  ░░░░░░▓▓▒▒▒▒▓▓▒▒▒▒▓▓▓▓▓▓    ░░░░░░░░░░░░░░░░▒▒▒▒░░░░▒▒░░░░░░
          ▒▒░░░░░░▒▒░░▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓░░░░░░░░▓▓▒▒▒▒▒▒▓▓▓▓▓▓▒▒  ░░░░░░░░░░░░      ░░░░░░▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒  ░░░░░░▓▓▓▓▒▒▓▓▓▓░░▒▒░░░░░░░░░░░░░░
          ▒▒░░░░▒▒▒▒░░▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓██░░░░  ░░░░▒▒▒▒▒▒▓▓▓▓▒▒    ░░░░▓▓░░░░▒▒▒▒░░░░░░░░░░▓▓▒▒▒▒▓▓▒▒▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▒▒▓▓▓▓░░░░░░░░░░░░░░▒▒
          ▒▒░░░░▒▒▒▒░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░▓▓▒▒░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░▓▓▓▓▒▒▓▓▓▓▓▓▒▒▓▓▓▓░░░░░░░░░░░░▒▒
          ▒▒░░░░▒▒▒▒░░░░▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░  ░░░░░░░░▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▒▒░░░░░░░░▒▒▒▒▒▒▓▓▓▓▒▒▒▒░░░░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▒▒▒▒░░▒▒
          ░░░░░░▒▒░░░░▒▒▒▒▓▓██▓▓▒▒▒▒░░░░▒▒░░░░░░▓▓▓▓▓▓░░      ░░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░  ░░░░░░▒▒▓▓▓▓▓▓░░░░░░  ░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▒▒░░▒▒
          ▒▒░░▒▒▒▒░░░░▒▒▒▒░░░░░░░░▒▒░░░░░░░░░░▓▓██▓▓▓▓▓▓░░░░  ░░▒▒██▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░  ░░░░░░░░░░░░░░░░    ░░░░▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒░░░░░░▓▓░░░░▒▒
          ░░░░░░▒▒░░░░░░▒▒░░░░░░░░░░░░░░░░▒▒▓▓██████▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓░░░░░░░░░░░░░░░░▒▒▓▓▒▒▓▓░░░░▒▒▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒░░░░░░░░░░░░▒▒
          ░░░░░░▒▒░░░░░░▒▒▓▓▓▓▓▓▓▓░░░░░░░░▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░  ░░▓▓▓▓▒▒▓▓▒▒▓▓▓▓▓▓░░░░░░░░  ░░░░░░▓▓▓▓▓▓▓▓▓▓▒▒░░░░▓▓▒▒▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░
          ▒▒░░░░▒▒▒▒▒▒▓▓██▓▓▓▓▓▓██▓▓░░░░░░██▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░▒▒░░▒▒▓▓▓▓▒▒▓▓▓▓▓▓▒▒░░░░░░▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░░░▒▒
          ▒▒░░░░▓▓▒▒▒▒████▓▓▓▓▓▓▓▓▓▓▒▒░░░░▓▓▓▓▒▒▓▓▒▒▓▓▓▓▓▓▓▓░░░░░░░░░░▒▒▓▓▓▓▒▒▒▒░░░░░░░░▒▒▒▒░░░░▓▓▓▓▓▓▒▒▓▓▒▒▓▓▓▓░░    ░░░░░░░░░░  ░░░░░░▒▒▒▒░░▓▓
          ▒▒▒▒░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓░░░░▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░▒▒▓▓▒▒░░▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒░░  ░░░░░░░░░░░░░░  ░░▒▒▒▒▒▒░░▒▒
          ▒▒▒▒░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒░░░░▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒░░░░    ░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓░░▒▒░░▒▒▓▓▒▒▒▒▒▒▒▒▓▓▒▒░░░░░░░░░░░░░░░░  ░░░░▒▒▓▓▒▒░░░░
          ░░▒▒░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░▓▓██▓▓▓▓▓▓▒▒░░░░░░░░  ░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓▒▒░░░░
          ░░▒▒░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓██▓▓░░░░░░░░░░▒▒▒▒▒▒░░▒▒░░░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░░░░░░░▓▓▓▓▓▓▓▓▒▒░░▓▓██▓▓▓▓▒▒░░░░░░░░▒▒▓▓▓▓▓▓▒▒░░░░
            ▒▒░░▒▒▒▒▒▒▓▓██▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░▓▓▒▒▒▒▒▒▒▒░░░░░░▒▒▓▓▓▓▓▓▒▒▓▓▓▓▓▓██▒▒░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓██▒▒░░░░░░░░░░▒▒▒▒▒▒░░
            ░░░░▒▒▓▓▒▒▒▒▓▓▓▓▓▓▓▓██▒▒░░░░░░░░░░░░░░▒▒░░░░▒▒▓▓▓▓▓▓▒▒▓▓▓▓░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░▓▓▓▓▒▒░░░░░░░░
              ▒▒░░▒▒▒▒▒▒░░░░░░░░░░░░░░▒▒▒▒▓▓▓▓▒▒░░░░░░▒▒▒▒▓▓▒▒▓▓▓▓▒▒▓▓▒▒░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░▓▓▒▒▓▓▒▒▓▓▓▓▓▓██▓▓░░░░▒▒▒▒▒▒░░░░▒▒
              ▒▒▒▒▒▒▓▓▒▒░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▒▒░░░░▒▒▓▓▓▓▒▒▓▓▒▒▒▒▓▓░░░░░░▓▓██▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▒▒▒▒▒▒▓▓▒▒░░░░░░
                ░░░░▒▒▒▒░░░░░░░░▒▒░░▓▓▓▓▒▒▓▓▓▓▓▓▓▓▒▒░░░░▓▓▓▓▒▒▒▒▓▓▒▒▓▓▒▒░░░░▒▒▓▓██▓▓▒▒▓▓░░▒▒▒▒░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▒▒▒▒▓▓▒▒░░░░░░
                ░░░░░░▒▒▓▓░░░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░▓▓▓▓▓▓▓▓▓▓▒▒▓▓░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░░░
                ░░░░░░░░░░▒▒▒▒░░░░▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓░░░░░░▓▓▓▓██▓▓▓▓▒▒░░░░░░▒▒▒▒░░▒▒▒▒▒▒░░░░▒▒██████▓▓▒▒░░░░░░▓▓▓▓██▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░░░
                  ▒▒░░░░░░▒▒▒▒▒▒░░▒▒▓▓▒▒▓▓▓▓▒▒▓▓▓▓██░░▒▒░░░░▒▒▓▓▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒▓▓██████▓▓▓▓██░░░░░░▒▒▓▓██████▓▓▒▒▒▒▒▒░░░░░░░░░░
                  ░░▒▒░░░░░░▒▒▒▒▒▒░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░▒▒░░  ░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░
                    ▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▒▒░░░░▒▒██▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▒▒▒▒▒▒░░░░░░░░  ░░░░
                      ▓▓▒▒░░▒▒░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓░░░░▒▒░░▒▒▒▒░░░░▒▒██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░▒▒██▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒▒░░░░▒▒░░░░░░░░░░░░  ░░░░░░
                        ▓▓▒▒░░░░░░░░░░▒▒▒▒░░░░░░░░░░░░░░▒▒▒▒▒▒░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░░░░░░░▒▒░░░░░░
                        ░░▓▓▒▒░░░░░░▒▒▒▒▒▒░░░░▒▒░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒░░░░  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░  ░░░░░░░░▒▒
                          ░░▓▓▒▒░░▒▒░░▒▒▒▒░░▒▒▒▒░░░░░░░░░░░░░░  ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░▓▓▓▓▓▓▓▓▓▓██▒▒▒▒▒▒░░░░░░░░░░░░▒▒░░▒▒
                            ░░▓▓▒▒░░░░░░░░▒▒▒▒▒▒▒▒░░░░  ░░░░░░░░░░▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▒▒░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓░░░░░░░░▓▓▓▓▓▓▒▒
                              ░░▓▓▒▒░░▒▒░░░░░░▒▒▓▓░░▒▒░░░░░░░░░░░░░░▓▓██▓▓▓▓██▓▓▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░▒▒▒▒▓▓▒▒░░░░░░░░▒▒▒▒▒▒
                                  ▒▒▓▓▓▓░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░    ░░▒▒▓▓▒▒▒▒░░▒▒▒▒░░░░▒▒▒▒▓▓▒▒▓▓░░░░░░░░░░░░░░░░░░░░░░
                                    ▒▒██▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░
                                      ░░██▓▓▒▒░░░░▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░
                                          ░░▓▓░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒░░▒▒▒▒▒▒░░░░░░▒▒░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒░░
                                              ░░▒▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░    ░░░░▒▒▒▒▒▒
                                                  ░░▓▓▒▒░░░░▒▒░░░░▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░░░
                                                        ▒▒▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░
                                                                ░░░░▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒░░░░                                                                """

        # Add pizzas to item_list and graphics to graphics list
        while True:

            # Pizza selection prompt
            pizza_size = (input(
                f"What size pizza are you feeling? \n 1. A slice  ${Pizza.slice_price}\n 2. 10in     ${Pizza.ten_in_price}\n 3. 40in     ${Pizza.the_jeremiah_special_price}\n 4. No more pizza please \n Your choice: ")).lower()

            # Append graphic and items to their corresponding lists
            if pizza_size == "1" or pizza_size == "slice" or pizza_size == "a slice":
                self.item_list.append("slice")
                graphics.append(slice_graphic)
                print("1 slice added to your card\n")
                continue

            elif pizza_size == "2" or pizza_size == "10" or pizza_size == "10in" or pizza_size == "10 in":
                self.item_list.append("10in")
                graphics.append(ten_in_graphic)
                print("10inch pizza added to your card\n")
                continue

            elif pizza_size == "3" or pizza_size == "40" or pizza_size == "40in" or pizza_size == "40 in":
                self.item_list.append("jeremiah special")
                graphics.append(the_jeremiah_special_graphic)
                print(
                    "40inch pizza added to your card\n. Family size? More like personal sized.")
                continue
            elif pizza_size == "4":
                print("No pizza ordered")
                break
            else:
                print("Invalid choice. Try again. \n")
                continue

        # Fun message depending on total item quantity
        if len(self.item_list) > 1:
            print("\nHere's your pizzas!\n")
        elif len(self.item_list) == 1:
            print("\nHere's your pizza!\n")
        else:
            print(
                "\nYou didn't order anything. How am I supposed to pay rent if you don't buy something?\n")

        # Present the user's order
        for graphic in graphics:
            print(graphic)


# Inherits username from Sweet class, provide methods for ordering pie
class Pie(Sweet):
    """Instatiate with username"""

    # Pie Prices
    pumpkin_pie_slice_price = 3.99
    cherry_pie_slice_price = 3.49
    whole_apple_pie_price = 16.99

    def __init__(self, username, total=0, item_list=[]):
        super().__init__(username)
        self.total = total
        self.item_list = item_list

    def change_name(self):
        """Change user's name"""

        new_name = input("What would you like your new name to be? ")
        self.username = new_name
        print(f"User's name changed to: {self.username}")

    def known_info(self):
        """Prints user's information"""

        print(f"Username: {self.username}")
        print(f"{self.username} is ordering pie.")

    @classmethod
    def update_pie_prices(cls):
        """Update pie prices"""

        # Store old prices for later usage
        old_pumpkin_slice_cost = cls.pumpkin_pie_slice_price
        old_cherry_slice_cost = cls.cherry_pie_slice_price
        old_apple_pie_cost = cls.whole_apple_pie_price

        # New price prompt
        cls.pumpkin_pie_slice_price = float(
            input("Enter new pumpkin pie slice cost: $"))
        cls.cherry_pie_slice_price = float(
            input("Enter new cherry pie slice cost: $"))
        cls.whole_apple_pie_price = float(
            input("Enter new whole apple pie cost: $"))

        # Print comparison of old to new price
        print("")
        print("Updated pie prices \n")
        print(
            f"Pumpkin Pie Slice: ${old_pumpkin_slice_cost}  -->  ${cls.pumpkin_pie_slice_price}")
        print(
            f"Cherry Pie Slice: ${old_cherry_slice_cost}  -->  ${cls.cherry_pie_slice_price}")
        print(
            f"Whole Apple Pie: ${old_apple_pie_cost}  -->  ${cls.whole_apple_pie_price}")

    def update_total(self):
        """Totals the user's items"""

        for item in self.item_list:
            if item == "pumpkin slice":
                self.total += Pie.pumpkin_pie_slice_price
            elif item == "cherry slice":
                self.total += Pie.cherry_pie_slice_price
            elif item == "whole apple pie":
                self.total += Pie.whole_apple_pie_price

        print(f"{self.username}'s total: ${round(self.total, 2)}")
        return round(self.total, 2)

    def pie_picker(self):
        """Picks a pie graphic(s) and updates total"""

        # Create list to store pie graphics
        graphics_list = []

        # Pie graphics
        pumpkin_pie_graphic = """                      ██████
              ████████      ██
            ██░░░░██        ██████
          ██░░░░██        ██████████
        ██░░░░░░██      ██████████████
    ████░░░░░░████      ██████████████
  ██░░░░░░░░██████      ██████████████████
  ██░░░░░░████████        ████████████████████
  ██░░░░██████████          ████████████████████████
██░░░░██████████████      ██████████████████████████████
██░░░░████████████████████████████████████████████████████
██░░░░████████████████████████████████████████████████████
  ██░░████████████████████████████████████████████████████
  ██░░░░██████░░░░██████░░░░██████░░░░██████░░░░██████░░██
  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
    ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
    ██░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░████░░░░░░░░░░░░██
    ██░░░░░░░░░░██  ████░░░░░░░░░░░░░░██  ████░░░░░░░░░░██
    ██░░░░░░░░░░████████░░░░██░░██░░░░████████░░░░░░░░░░██
      ██░░░░░░░░░░████░░░░░░░░██░░░░░░░░████░░░░░░░░░░░░██
        ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
        ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
          ████████████████████████████████████████████████"""

        cherry_pie_graphic = """                                                                      ██████
                                                        ▒▒▓▓        ▓▓      ▓▓▒▒
                                                    ████████████  ██            ██
                                                  ▒▒██▒▒▒▒██████▒▒░░            ░░
                                                  ████░░░░████████
                                                  ██░░░░██████████
                                                ████░░██████████████
                                                ████████████████████
                                              ▒▒  ████████████████    ▒▒██▒▒
                                          ████    ████████████████      ▒▒▒▒██████
                                      ██▓▓░░        ████████████░░      ▒▒▒▒▒▒▒▒▒▒██████
                                  ████░░░░░░            ████            ▒▒▒▒▒▒▒▒▒▒▒▒██████
                              ████░░░░░░░░░░░░                        ▒▒▒▒▓▓██████▓▓░░  ░░██
                          ████░░░░░░░░░░░░░░░░░░                ▒▒████████          ░░░░░░██
                      ▓▓██░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒██████████  ░░░░░░░░░░░░░░░░░░░░░░██
                  ████░░░░░░░░░░░░░░░░░░░░░░░░██████████          ░░░░░░░░░░░░░░░░░░░░░░░░██
              ▓▓██░░░░░░░░░░░░░░░░░░██████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
          ░░▓▓▒▒▒▒░░░░░░░░▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
      ████░░░░░░░░████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
  ██▓▓▒▒██▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████
██▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒████████████████
██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████████████████░░░░░░██
██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓████████▒▒▒▒▒▒▒▒▒▒░░░░░░██
██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████████████████░░░░░░░░░░░░░░░░░░░░░░░░██
██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓██████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
██░░░░░░░░░░░░░░░░░░░░░░░░████████████████████          ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
██░░░░░░░░░░░░░░░░▒▒████████████████▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
██░░░░░░██████████████████          ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
██████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
████████          ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████
██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████▓▓
██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████
██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████████
██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████████
██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████████
██░░░░░░░░░░▒▒░░░░░░░░░░░░██████████
██░░░░░░░░░░░░░░░░████████
██░░░░░░██████████
████████
"""
        whole_apple_pie_graphic = """                                                                                                ░░░░
                                                                ░░░░▒▒▒▒▒▒░░▒▒▒▒▓▓▒▒▒▒░░░░░░▒▒▒▒▒▒▓▓▒▒░░░░░░░░░░░░░░
                                                      ░░░░░░░░░░▒▒▒▒▓▓▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒░░░░░░░░░░▒▒░░░░░░
                                                    ░░▒▒▓▓▒▒░░▒▒▒▒▒▒▒▒▒▒░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒░░
                                                  ░░░░▒▒▒▒░░▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒░░    ░░░░░░▒▒▒▒▒▒░░▒▒
                                                ░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▒▒░░░░▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒
                                        ▒▒░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▒▒▓▓▓▓▓▓▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░▒▒░░░░▒▒░░▒▒░░▒▒▒▒░░░░
                              ░░▒▒▒▒▒▒░░░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▒▒░░░░░░▒▒▒▒▒▒▒▒▓▓▒▒░░▒▒▒▒▓▓████▓▓▒▒░░▒▒▓▓▒▒▒▒░░▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ░░░░░░░░░░
                            ░░▒▒▓▓▓▓░░  ░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒░░░░░░░░░░░░░░░░▒▒
                          ░░▒▒▒▒▓▓▒▒░░░░▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒░░▒▒▒▒░░░░░░░░░░░░░░░░▒▒▒▒░░▒▒▓▓▓▓░░░░▒▒▒▒░░░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒░░▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▓▓░░▒▒▒▒░░░░░░░░░░▒▒
                      ░░▒▒░░░░▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░▒▒▒▒░░░░▒▒▒▒░░▒▒▒▒▒▒▒▒░░░░▒▒▓▓▓▓▓▓▓▓▓▓▒▒░░░░▒▒▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒░░▒▒▒▒▒▒▒▒▓▓░░▒▒▓▓░░░░░░░░░░▓▓
                    ▒▒▒▒▒▒░░░░▓▓▓▓▓▓▒▒░░░░▒▒▒▒░░░░▒▒▒▒▒▒░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓░░▒▒▒▒░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▓▓▓▓▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░▒▒▒▒
                  ░░░░▒▒▒▒░░░░▓▓▓▓▒▒░░░░░░░░▒▒░░░░▒▒░░▒▒▓▓▓▓▓▓░░▒▒▒▒▒▒░░░░▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▓▓▒▒▒▒▓▓▓▓▓▓▒▒░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▒▒░░░░▒▒▒▒
                ░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▒▒░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░▒▒▒▒▒▒░░░░▒▒▒▒
              ░░▒▒▒▒▓▓▓▓▓▓▒▒▒▒░░░░  ░░░░░░░░░░░░░░░░░░▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒▓▓▓▓▒▒░░░░░░▒▒▒▒▒▒░░▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒▒▒░░░░░░▒▒▓▓
              ░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░▒▒░░▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░▒▒▒▒▒▒░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░▒▒░░
            ░░░░░░▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░▒▒▓▓▓▓▓▓▓▓▒▒▒▒░░▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░▒▒░░▒▒▒▒░░
        ░░▒▒░░░░░░▒▒▓▓▓▓▓▓▒▒░░▒▒▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓██▓▓████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▒▒▒▒░░░░▒▒▒▒██
      ░░▒▒▒▒░░░░░░▓▓▓▓▓▓▒▒░░▒▒▓▓░░▓▓▓▓▓▓▓▓░░░░░░▒▒▓▓░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒░░░░  ░░▒▒▒▒░░▒▒▒▒▒▒░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░░░▒▒▓▓██
      ░░░░▒▒░░░░░░██▒▒░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░▒▒▓▓▓▓▓▓▓▓▒▒▓▓▒▒▓▓▓▓▒▒▒▒░░░░░░░░▒▒▓▓▓▓▓▓▓▓░░░░░░▒▒▒▒▒▒░░░░░░▒▒░░██▓▓████▓▓▓▓▓▓████████▒▒░░░░▒▒▒▒▒▒▒▒▓▓████▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░▒▒▓▓▓▓
      ░░░░▒▒░░░░▒▒▒▒▒▒░░░░░░▓▓▓▓▓▓▓▓▓▓▒▒░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░▒▒▒▒▒▒▒▒▒▒░░▒▒▓▓▓▓▓▓▓▓▒▒▓▓██▓▓▓▓▓▓▒▒▓▓▒▒░░░░▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░░░▓▓
      ░░▒▒▒▒░░▒▒▒▒▓▓▒▒░░░░░░░░░░░░░░▒▒░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▒▒░░░░░░░░░░▒▒▒▒▒▒▓▓▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒░░░░░░▒▒
    ░░░░▒▒░░░░▒▒▓▓▓▓▒▒▒▒░░▒▒░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▒▒▒▒▒▒░░▒▒░░▒▒▒▒▒▒▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▓▓▒▒▒▒▓▓▓▓▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒░░░░▒▒
    ░░░░░░░░░░▒▒▓▓░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░▒▒░░░░▒▒▒▒▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓░░░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▒▒▓▓▓▓▓▓██▓▓▓▓▓▓▒▒░░░░▒▒▓▓
    ░░░░░░░░░░░░▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒░░░░▒▒░░░░▒▒▒▒▓▓████▒▒▒▒░░▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▒▒▒▒▓▓▓▓▒▒████▓▓▓▓▓▓▓▓▒▒░░▒▒▓▓▓▓░░
    ▒▒░░▒▒▒▒▒▒▓▓▓▓▒▒░░░░▒▒▒▒▒▒░░░░░░░░▒▒▒▒░░░░░░░░░░░░▒▒▓▓▓▓▒▒░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓██▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓
    ░░▒▒▒▒▒▒▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒▒▒░░░░░░▒▒░░░░░░░░▒▒▒▒░░░░▒▒▒▒▒▒░░▒▒▓▓▓▓▓▓▓▓▓▓██▒▒░░▒▒▒▒▒▒░░▒▒▒▒▒▒░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░▒▒░░
    ▒▒▒▒▒▒░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▒▒░░░░░░░░░░▒▒▒▒░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓██▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▒▒░░░░░░▒▒▓▓
  ░░░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░░░░░▒▒░░░░░░▒▒▓▓▓▓██▓▓░░░░░░▒▒▒▒▒▒▒▒░░░░░░▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒░░░░▒▒▓▓
  ░░░░░░░░░░░░▓▓▓▓░░░░▓▓▓▓▓▓▓▓░░░░▒▒▒▒░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░▒▒▒▒██▓▓▓▓██▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▓▓██████▓▓▓▓▓▓██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▓▓
  ░░░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓██░░░░░░▒▒░░░░▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░▒▒▓▓▓▓▓▓▓▓██▓▓▓▓▒▒▓▓▓▓▓▓▓▓██▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒░░▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒░░▒▒▓▓▓▓
    ▒▒░░▒▒░░░░░░▓▓▓▓▓▓▓▓▓▓▒▒▒▒░░▒▒░░▒▒▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░░░▒▒░░░░░░░░░░░░░░▒▒▒▒░░░░▒▒▒▒▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒▒▒▓▓▓▓▓▓▒▒▒▒▓▓▒▒▒▒░░▒▒▒▒▒▒░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░▒▒▓▓▓▓
      ▒▒▒▒░░░░░░▒▒░░░░░░░░▒▒▒▒░░░░▒▒▒▒▓▓░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▒▒░░░░▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒▓▓░░░░░░▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓▓████████████▓▓▒▒░░░░░░▓▓▓▓
      ▒▒░░░░░░░░░░▒▒░░░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓████▓▓████▓▓████▒▒▒▒▒▒▒▒▒▒░░░░▒▒▓▓▒▒▒▒▒▒▒▒▒▒████████████▓▓▒▒░░░░▒▒▓▓▓▓
      ▒▒░░░░░░░░░░░░▒▒░░░░░░░░░░░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓██▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓██▓▓▓▓▓▓░░░░░░▒▒▓▓▒▒
      ▒▒▒▒░░░░░░░░░░▒▒░░░░░░░░░░░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓██▓▓████░░░░▒▒▒▒▒▒▓▓▒▒▒▒░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒░░▓▓▓▓▒▒░░▒▒▒▒▒▒▒▒░░▒▒░░▒▒▒▒▓▓░░▒▒▓▓▒▒▓▓▒▒▒▒████▒▒▓▓░░░░░░▒▒▒▒▓▓░░
        ▒▒▒▒░░▒▒░░░░░░▒▒░░▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▓▓██▓▓██▓▓▓▓░░░░░░▒▒▒▒░░░░░░▒▒▒▒▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░▒▒░░░░░░▒▒▓▓▓▓▓▓██▓▓▒▒▒▒▒▒▓▓▓▓▒▒▓▓▓▓▒▒▒▒░░▒▒▒▒▒▒▓▓██
        ░░▒▒▒▒▒▒░░░░░░▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒░░░░▒▒▒▒░░░░░░▒▒░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████▓▓▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒░░▒▒▒▒░░░░░░░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░▒▒▒▒▓▓▓▓▓▓▒▒
          ▒▒▒▒░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓████▓▓▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒░░░░▒▒▓▓▒▒░░░░▒▒▒▒░░▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▒▒░░░░░░▒▒▓▓▓▓▓▓▓▓
          ░░░░░░░░░░▒▒▒▒░░░░▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▒▒░░▒▒▒▒▒▒░░░░░░░░▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░▒▒▓▓▓▓▓▓▒▒
            ▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▒▒░░░░░░░░▒▒▒▒▓▓░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒░░▒▒▒▒▒▒▒▒░░░░▒▒▒▒▓▓▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▓▓▓▓▓▓██▓▓▒▒▒▒▒▒▒▒░░▒▒▓▓▓▓▓▓▒▒
              ▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▓▓▒▒░░▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒░░▒▒▒▒▓▓▒▒▓▓▓▓▓▓██▓▓
              ▒▒████▓▓██▓▓░░░░░░░░░░▒▒▒▒▒▒▓▓▒▒░░▒▒▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓██▓▓
                ▒▒██▓▓██▓▓░░░░░░░░░░▒▒░░░░░░░░░░██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓██▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░▒▒▒▒▓▓▓▓▓▓▓▓██▓▓
                  ▒▒██░░▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████▓▓██▒▒░░▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░▒▒▒▒▓▓▓▓▓▓██▓▓
                    ▒▒▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░▒▒░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒
                      ░░▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓██░░░░▒▒▒▒▒▒▒▒▒▒░░▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓░░░░▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▓▓▓▓██▓▓░░
                          ▓▓▓▓▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒░░▒▒▓▓████▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▒▒▓▓▓▓▓▓▓▓▒▒▒▒░░░░▒▒░░░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒
                            ░░▓▓████████░░░░▒▒▒▒░░░░░░░░░░▒▒░░░░▒▒▓▓▓▓▓▓░░░░░░░░░░░░▒▒▓▓▓▓▓▓██▓▓▓▓▓▓▒▒▒▒░░░░▒▒▒▒░░░░░░░░░░▒▒░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▒▒
                                ▒▒▓▓██████░░▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒░░▒▒▒▒▒▒▒▒▒▒░░▒▒▓▓▒▒░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▓▓▒▒▓▓▒▒▓▓▓▓▓▓▓▓██▓▓▓▓▒▒
                                  ░░▒▒▓▓▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓██▓▓▓▓▓▓░░
                                      ░░▒▒▓▓▓▓▒▒▒▒▒▒▓▓████▒▒▒▒▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒░░▒▒▒▒▒▒▓▓▒▒▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▒▒▒▒
                                        ░░░░▒▒▒▒▓▓▓▓██▓▓▓▓▓▓▓▓▒▒░░▒▒▓▓▒▒▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓████████▓▓▓▓▓▓▒▒▒▒▒▒
                                            ▒▒▒▒░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓██▓▓▓▓██▒▒▓▓▓▓▓▓▓▓████████▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░
                                              ░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░
                                                  ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░
                                                        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
                                                              ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░
                                                                    ░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░
                                                                                    ░░  ░░░░░░
"""
        # Add pies to item_list and graphics to graphics_list
        while True:

            # Pie selection prompt
            pie_choice = (input(
                f"What kind of pie do you want? \n 1. Pumpkin Pie Slice ${Pie.pumpkin_pie_slice_price} \n 2. Cherry Pie Slice  ${Pie.cherry_pie_slice_price}\n 3. Whole Apple Pie   ${Pie.whole_apple_pie_price}\n 4. No Pie \n Your choice: ")).lower()

            # Append graphics and items to their corresponding lists
            if pie_choice == "1" or pie_choice == "pumpkin" or pie_choice == "pumpkin pie" or pie_choice == "pumpkin pie slice":
                self.item_list.append("pumpkin slice")
                graphics_list.append(pumpkin_pie_graphic)
                print("1 slice of pumpkin pie added to your card\n")
                continue

            elif pie_choice == "2" or pie_choice == "cherry" or pie_choice == "cherry pie" or pie_choice == "cherry pie slice":
                self.item_list.append("cherry slice")
                graphics_list.append(cherry_pie_graphic)
                print("1 slice of cherry pie added to your card\n")
                continue

            elif pie_choice == "3" or pie_choice == "apple" or pie_choice == "apple pie" or pie_choice == "whole apple pie":
                self.item_list.append("whole apple pie")
                graphics_list.append(whole_apple_pie_graphic)
                print(
                    "1 whole apple pie added to your card\n. Still cheaper than seeing a therapist amirite?")
                continue

            elif pie_choice == "4" or pie_choice == "no pie":
                print("No selection. Order completed.")
                break

            else:
                print("Invalid choice. Try again. \n")
                continue

        # Fun message depending on total item quantity
        if len(self.item_list) > 1:
            print("\nHere's your pies!\n")
        elif len(self.item_list) == 1:
            print("\nHere's your pie!\n")
        else:
            print(
                "\nYou didn't order anything. How am I supposed to pay rent if you don't buy something?\n")

        # Present the user's order
        for graphic in graphics_list:
            print(graphic)


# Inherits username from Sweet clas, provides methods for ordering cake
class Cake(Sweet):
    """Instantiates with username"""

    # Cake Prices
    white_cake_price = 4.99
    crepe_cake_price = 5.49
    birthday_cake_price = 18.01

    def __init__(self, username, total=0, item_list=[]):
        super().__init__(username)
        self.total = total
        self.item_list = item_list

    def change_name(self):
        """Change user's name"""

        new_name = input("What would you like your new name to be? ")
        self.username = new_name
        print(f"User's name changed to: {self.username}")

    def known_info(self):
        """Prints user's information"""

        print(f"Username: {self.username}")
        print(f"{self.username} is ordering cake.")

    @classmethod
    def update_cake_prices(cls):
        """Update cake prices"""

        # Store old prices for later usage
        old_white_cake_cost = cls.white_cake_price
        old_crepe_cake_price = cls.crepe_cake_price
        old_birthday_cake_price = cls.birthday_cake_price

        # New price prompt
        cls.white_cake_price = float(input("Enter new white cake price: $"))
        cls.crepe_cake_price = float(input("Enter new crepe cake price: $"))
        cls.birthday_cake_price = float(
            input("Enter new birthday cake price: $"))

        # Print comparison of old to new price
        print("")
        print("Updated cake prices \n")
        print(
            f"White cake: ${old_white_cake_cost}  -->  ${cls.white_cake_price}")
        print(
            f"Crepe cake: ${old_crepe_cake_price}  -->  ${cls.crepe_cake_price}")
        print(
            f"Birthday cake: ${old_birthday_cake_price}  -->  ${cls.birthday_cake_price}")

    def update_total(self):
        """Totals the user's items"""

        for item in self.item_list:
            if item == "white cake":
                self.total += Cake.white_cake_price
            elif item == "crepe cake":
                self.total += Cake.crepe_cake_price
            elif item == "birthday cake":
                self.total += Cake.birthday_cake_price

        print(f"{self.username}'s total: ${round(self.total, 2)}")
        return round(self.total, 2)

    def cake_picker(self):
        """Picks a cake graphic and updates total"""

        # Create list to store cake graphics
        graphics_list = []

        # Cake graphics
        white_cake_graphic = """                                            ██            ▒▒▒▒▒▒  ▒▒▒▒▒▒
                                      ██████  ████      ▒▒░░░░░░▒▒░░▒▒░░▒▒
                                  ████    ██      ████  ▒▒░░░░░░░░░░▒▒░░▒▒▒▒▒▒
                                ██        ██      ░░░░▒▒░░▒▒░░░░░░░░░░░░░░░░░░▒▒
                              ██      ████        ░░▒▒░░░░░░▒▒▒▒░░░░░░░░▒▒░░░░▒▒
                              ██                ░░░░▒▒  ░░▒▒░░░░░░▒▒░░░░░░▒▒▒▒
                            ██                  ░░▒▒  ░░░░▒▒░░░░░░▒▒░░░░░░▒▒▒▒▒▒
                            ██                  ░░▒▒  ░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒
                          ██░░                ░░░░▒▒  ░░░░░░▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒
                      ████    ░░░░        ░░░░░░░░▒▒░░░░░░░░▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒
                    ▓▓            ░░░░░░░░░░░░░░░░▒▒░░░░░░░░▒▒░░▒▒░░░░▒▒░░▒▒▒▒▒▒
                  ██                  ░░░░░░░░░░  ░░▒▒▒▒▒▒▒▒░░▒▒░░░░░░▒▒▒▒▒▒▒▒
                  ██░░░░                          ░░▒▒▒▒▒▒░░▒▒░░▒▒▒▒░░▒▒▒▒▒▒▒▒
                  ██░░░░░░░░                        ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░██
                  ██░░░░░░░░░░░░░░░░░░░░░░            ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░    ██
                  ██░░░░  ░░░░░░░░░░░░░░░░░░░░░░░░░░    ░░░░▒▒▒▒▒▒▒▒▒▒░░░░        ▓▓
                  ██░░░░                  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░              ██
                  ██░░░░░░      ▒▒        ░░░░  ░░░░░░░░░░░░░░░░░░░░░░░░              ▓▓
                  ██░░░░░░        ░░                          ░░░░░░░░░░░░░░░░░░        ██
                  ██░░░░░░        ░░                          ░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
                  ██░░░░░░                                  ▒▒          ░░      ░░░░░░░░  ██
                  ██░░░░░░░░░░░░░░            ▒▒              ░░                          ██
                  ██░░░░░░░░░░░░░░░░░░░░░░░░    ░░                                        ██
                  ██▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░                      ▒▒            ██
                  ██░░░░░░▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░              ░░          ██
                  ██░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                ██
                  ██░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░        ██
              ██▓▓██░░░░▒▒░░░░░░░░          ░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░  ░░░░░░██
          ████▒▒▒▒░░░░░░░░░░░░░░░░░░                  ░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░▒▒██████
      ▓▓▓▓▒▒▒▒    ░░░░░░░░░░░░░░░░░░                            ░░░░░░░░░░▒▒▒▒▒▒▒▒░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓
    ██▒▒▒▒        ░░░░░░░░░░░░░░░░░░░░░░            ▒▒                    ░░░░░░░░▒▒▒▒▒▒▒▒▒▒      ▒▒▒▒████
  ██▒▒            ░░░░░░░░░░░░░░░░░░▒▒░░░░░░          ░░                    ░░    ░░░░░░░░░░          ▒▒▒▒██
  ██▒▒    ░░░░▒▒  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                      ▒▒            ░░    ░░░░░░░░░░▒▒
██▒▒    ▓▓      ░░░░      ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░              ░░          ░░░░░░          ░░
██▒▒    ▓▓░░░░░░░░  ░░░░░░░░      ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░      ░░░░░░░░░░░░
  ██▒▒    ▒▒▒▒░░░░░░        ░░░░            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░      ░░░░░░░░░░░░░░░░░░
  ██▒▒▒▒      ▒▒▒▒▒▒░░░░░░░░    ░░░░                  ░░░░░░░░░░░░░░░░░░░░  ░░      ░░░░░░░░░░░░░░░░░░░░░░░░
    ██▒▒░░░░░░      ▒▒▒▒▓▓░░░░░░    ▒▒░░░░░░░░░░░░░░░░░░░░░░░░            ░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓
        ▒▒▓▓▓▓░░░░░░      ░░░░░░░░░░                          ░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░░░░░▒▒▒▒▓▓
      ▒▒      ▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░  ▒▒▒▒▓▓▓▓
      ▒▒░░░░░░      ▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░            ▒▒▒▒▒▒████
        ▒▒▓▓░░▒▒░░░░      ░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░                ▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓  ░░
            ▒▒▒▒░░░░░░░░░░░░░░▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓
                ▒▒▒▒▒▒▒▒▒▒▒▒▓▓    ░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░
"""
        crepe_cake_graphic = """                                                          ▒▒▒▒▒▒▒▒░░
                                                        ██████████████████
                                                      ▒▒██████████████████▓▓▓▓▓▓
                                                    ▒▒████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒░░
                                                  ██████▒▒░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
                                                ██████▒▒░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░▒▒▓▓▓▓▓▓▓▓██░░
                                              ██████▓▓▓▓▓▓▓▓▒▒░░▒▒▓▓▓▓▓▓░░░░░░░░▒▒▒▒▓▓▓▓██████████
                                            ▓▓██████▒▒░░▒▒▓▓░░▒▒▒▒▓▓▓▓▓▓░░░░░░▒▒▒▒▒▒██████████████▒▒
                                          ██████▓▓▒▒░░▒▒▒▒▒▒▓▓▒▒▒▒▓▓▓▓░░░░░░▒▒▒▒▒▒▒▒██████████████████
                                        ▓▓████▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓░░░░▒▒▒▒▒▒▒▒██████████████████████
                                      ▒▒████▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓░░▒▒▒▒▒▒▒▒▓▓██████████████████████▒▒
                                    ████▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒██████████████████████░░░░████▓▓
                                  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████████████████████▓▓▓▓██▓▓▓▓
                                ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓████████████████████████████████░░░░████▓▓▓▓▒▒▓▓
                              ▓▓██░░░░░░░░░░░░▒▒▒▒▒▒▒▒██████████████████████████████████████████▓▓▓▓▓▓▓▓▓▓
                          ░░▓▓████░░░░░░░░░░░░░░░░░░▓▓██████████████████████░░░░██████████████▓▓▓▓▓▓▓▓▒▒▓▓
                        ████████▓▓▓▓░░░░░░░░░░░░██████████████████████░░░░██████░░████████████▓▓▓▓▒▒▒▒  ▓▓
                      ▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████████████▓▓▓▓██▓▓▓▓▓▓░░████████▒▒▒▒▒▒░░░░  ▓▓
                    ██████▓▓▓▓▓▓▓▓▓▓██████████████████████░░██████████████▒▒▒▒▒▒▒▒██░░██████          ▒▒▓▓
                  ▓▓████▓▓▓▓▓▓▓▓████████████████████░░██████░░██████████▓▓▓▓▓▓▓▓▒▒▒▒██░░██        ▒▒▒▒▓▓▓▓
                ██████▓▓▓▓████████████████████░░████▓▓██████▒▒░░████████▓▓▒▒▒▒▒▒    ██░░██  ░░░░░░▒▒▒▒▓▓▓▓
              ████▓▓▓▓██████████████████░░░░██████▓▓▓▓▓▓▒▒▒▒████░░██████▒▒          ██░░██▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓
            ▓▓██▓▓████████████████░░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░████░░░░      ▒▒░░██▓▓██▒▒▓▓▓▓▓▓▒▒▒▒░░▓▓
          ████▓▓████████░░░░░░░░██████▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒████░░██    ▒▒▒▒▒▒▓▓▓▓▒▒████▒▒▒▒▒▒▒▒      ▓▓
        ████▓▓████░░░░░░████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒        ██░░██▒▒▒▒▓▓▒▒▒▒▓▓▓▓▓▓████▒▒          ▒▒▓▓
    ▓▓▓▓██▓▓░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░      ░░██░░██▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒████        ░░░░▒▒▓▓
  ██░░░░░░░░██████▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒            ▒▒▒▒▒▒▓▓██░░██▓▓▓▓▒▒▒▒▒▒      ████  ▒▒▒▒▒▒▓▓▓▓▓▓▓▓
  ▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░      ▒▒▒▒░░▒▒▒▒▒▒▒▒██░░██▒▒▒▒░░░░░░      ████░░▒▒▒▒▒▒▓▓▓▓▒▒▓▓
  ▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒░░            ▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒██░░██          ▒▒▒▒▒▒████▓▓▓▓▓▓▓▓▒▒▒▒  ▓▓
  ▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒              ▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒  ██░░██    ▒▒▒▒▒▒▓▓▒▒▒▒████▒▒▒▒▒▒▒▒      ▓▓
  ▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░        ░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░  ██▓▓██▒▒░░▒▒▒▒▒▒▓▓▓▓▓▓████▒▒░░░░░░    ░░▓▓
  ▓▓▒▒▒▒▒▒░░            ▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒            ▒▒▒▒██▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒████        ▒▒▒▒▓▓▓▓
  ▓▓░░░░░░░░      ▒▒▒▒░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░      ▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░██░░██▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓
  ▓▓      ░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒            ▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒          ██░░████▓▓▓▓▓▓▓▓▓▓██
  ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒            ▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒            ▒▒▒▒██░░██████▓▓▓▓▓▓▓▓
  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒              ▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒            ▒▒▒▒▒▒▓▓██░░██████████▓▓
  ▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒              ▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒            ▒▒▒▒▒▒▓▓▓▓▓▓▓▓██░░██████████
  ▓▓▒▒▒▒▒▒▒▒░░░░░░      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░      ▒▒▒▒░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓██▒▒░░░░████
  ▓▓              ▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒            ▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓██    ████████
  ▓▓        ▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒            ▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▓▓▓▓▓▓
  ▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░            ▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒              ▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
  ▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░          ▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓
  ▓▓▒▒▒▒▒▒░░            ▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
  ▓▓              ▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓
  ▓▓      ░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
  ▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓░░
  ▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓
  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
    ██▓▓▓▓▓▓
"""
        birthday_cake_graphic = """░░                ▒▒░░▒▒        ░░        ▒▒░░▒▒
░░░░░░              ▒▒        ██████        ▒▒    ░░░░  ░░░░  ░░
                  ██████      ██▒▒██      ██████
░░░░              ██▒▒██      ██▒▒██      ██▒▒██    ░░
                  ██▒▒██      ██▒▒██      ██▒▒██
░░        ░░  ░░  ██▒▒██      ██▒▒██      ██▒▒██
░░░░      ░░      ██▒▒████▒▒▒▒██▒▒████▒▒▒▒██▒▒██
░░░░    ░░    ▓▓▓▓██▒▒██▓▓░░▒▒██▒▒██▓▓░░▒▒██▒▒██▓▓▓▓
░░░░      ████▒▒  ██▒▒██  ▒▒  ██▒▒██  ▒▒  ██▒▒██  ▒▒████
░░      ██  ▒▒  ▒▒██▒▒██▒▒  ▒▒██▒▒██▒▒  ▒▒██▒▒██▒▒  ▒▒  ██
░░░░░░  ██░░░░░░░░██▒▒██░░░░░░▓▓████░░░░░░▓▓████░░░░░░░░██
░░░░    ██▒▒▒▒  ▒▒  ████▒▒  ▒▒  ▒▒  ▒▒  ▒▒  ▒▒  ▒▒  ▒▒▒▒██
░░░░    ██▒▒▒▒▒▒  ▒▒  ▒▒  ▒▒  ▒▒  ▒▒  ▒▒  ▒▒  ▒▒  ▒▒▒▒▒▒██
░░      ██    ▒▒▒▒▒▒▒▒  ▒▒  ▒▒  ▒▒  ▒▒  ▒▒  ▒▒▒▒▒▒▒▒    ██
░░░░    ██    ░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░    ██░░
░░░░░░  ██                                              ██░░  ░░
░░░░    ██    ░░              ░░              ░░        ██
░░░░  ██        ▒▒              ▒▒              ▒▒        ██░░
      ██▒▒▒▒          ▒▒▒▒▒▒          ▒▒▒▒▒▒          ▒▒▒▒██
░░    ██░░░░▒▒      ▒▒░░░░░░▒▒      ▒▒░░░░░░▒▒      ▒▒░░░░██
      ██▒▒░░░░▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒░░▒▒░░██
░░░░  ██░░▒▒░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░▒▒██
░░  ██▒▒██░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░██▒▒██
▒▒██░░▒▒▒▒████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████▒▒▒▒░░██
▒▒██░░░░▒▒▒▒▒▒██████░░░░░░░░░░░░░░░░░░░░░░░░░░██████▒▒▒▒▒▒░░░░██
░░░░██░░▒▒▒▒▒▒▒▒▒▒▒▒██████████████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░░░░  ████░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░████
░░        ████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████
"""

        # Add cakes to item_list and graphics to graphics_list
        while True:

            # Cake selection prompt
            cake_choice = (input(
                f"What cake do you want? \n 1. White cake  ${Cake.white_cake_price} \n 2. Crêpe Cake  ${Cake.crepe_cake_price} \n 3. Whole birthday cake (with candles!) ${Cake.birthday_cake_price} \n 4. No cake \n Your choice: ")).lower()

            # Append graphics and items to their corresponding lists
            if cake_choice == "1" or cake_choice == "white cake" or cake_choice == "white":
                self.item_list.append("white cake")
                graphics_list.append(white_cake_graphic)
                print("1 slice of white cake added to your card\n")
                continue

            elif cake_choice == "2" or cake_choice == "crepe cake" or cake_choice == "crepe":
                self.item_list.append("crepe cake")
                graphics_list.append(crepe_cake_graphic)
                print("1 slice of crêpe cake added to your card\n")
                continue

            elif cake_choice == "3" or cake_choice == "birthday cake" or cake_choice == "birthday":
                self.item_list.append("birthday cake")
                graphics_list.append(birthday_cake_graphic)
                print("1 whole birthday cake added to your card\n")

            elif cake_choice == "4" or cake_choice == "no cake":
                print("No selection. Order completed.")
                break

            else:
                print("Invalid choice. Try again.\n")
                continue

        # Fun message depending on total iteam quantity
        if len(self.item_list) > 1:
            print("\nHere's your cakes!\n")
        elif len(self.item_list) == 1:
            print("\nHere's your cake!\n")
        else:
            print(
                "\nYou didn't order anything. I'm not running a charity. Get the hell outta my store.")

        # Present the user's order
        for graphic in graphics_list:
            print(graphic)


# ____________________ FUNCTIONS _____________________

def create_user():
    """Instantiates Welcome object"""

    username = input("Input your name: ")

    # Prompts user for hunger status, kill program if response is False
    while True:
        hunger_status = (input("Are you hungry? (Y/N): ")).lower()

        if hunger_status == "y" or hunger_status == "yes":
            hunger_status = True
            break
        elif hunger_status == "n" or hunger_status == "no":
            hunger_status = False
            print("Cancelling program")
            exit()
        else:
            print("Invalid input. Try again.\n")
            continue

    print("")

    # Create the Welcome object
    global created_user
    created_user = Welcome(username, hunger_status)

    # Call welcome_options
    welcome_options(created_user)


def welcome_options(user):
    """Menu of user options"""

    print(f"\nWelcome {user.username}")
    while True:

        selected_option = (input(
            "Select an option\n 1. Change name\n 2. Change hunger status\n 3. View user info\n 4. Order Food\n 5. Quit\n Your choice: ")).lower()

        if selected_option == "1" or selected_option == "change name" or selected_option == "name":
            user.change_name()
            welcome_options(user)
            break
        elif selected_option == "2" or selected_option == "change hunger status" or selected_option == "hunger":
            user.is_hungry()

            if user.hunger == False:
              print("Cancelling program")
              exit()

            welcome_options(user)
            break
        elif selected_option == "3" or selected_option == "view info" or selected_option == "view user info" or selected_option == "info":
            print("")
            user.known_info()
            print("")
            welcome_options(user)
            break
        elif selected_option == "4" or selected_option == "order food" or selected_option == "food":
            created_user.savory_or_sweet()
            break
        elif selected_option == "5" or selected_option == "exit" or selected_option == "quit":
            print("Exiting program")
            exit()
        else:
            print("Invalid input. Try again.\n")
            continue


def change_name(user):
    """Change user's name"""

    user.username = input("What would you like your new name to be? ")
    print(f"User's name changed to: {user.username}")
    welcome_options(user)


# ------------------- Function Call -------------------
create_user()
