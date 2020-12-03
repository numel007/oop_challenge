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
    """Requires username, initial total, ingredient list"""
    patty_cost = 1.49
    lettuce_cost = 0.05
    pickle_cost = 0.15
    tomato_cost = 0.25
    cheese_cost = 0.75

    def __init__(self, username, total, ingredients):
        super().__init__(username)
        self.total = 0
        self.ingredients = []

    def change_name(self):
        """Change user's name"""

        new_name = input("What would you like your new name to be? ")
        self.username = new_name
        print(f"User's name changed to: {self.username}")


    def known_info(self):
        """Prints user's information"""

        print(f"Username: {self.username}")
        print(f"{self.username} is ordering a burger.")


    def update_ingredients_costs(self):
        """Update class ingredient prices"""

        old_patty_cost = Burger.patty_cost
        old_lettuce_cost = Burger.lettuce_cost
        old_pickle_cost = Burger.pickle_cost
        old_tomato_cost = Burger.tomato_cost
        old_cheese_cost = Burger.cheese_cost

        Burger.patty_cost = float(input("Enter new patty cost: $"))
        Burger.lettuce_cost = float(input("Enter new lettuce cost: $"))
        Burger.pickle_cost = float(input("Enter new pickle cost: $"))
        Burger.tomato_cost = float(input("Enter new tomato cost: $"))
        Burger.cheese_cost = float(input("Enter new cheese cost: $"))
        
        print("")
        print("Updated ingredient prices \n")
        print(f"Patty: ${old_patty_cost} --> ${Burger.patty_cost}")
        print(f"Lettuce: ${old_lettuce_cost} --> ${Burger.lettuce_cost}")
        print(f"Pickle: ${old_pickle_cost} --> ${Burger.pickle_cost}")
        print(f"Tomato: ${old_tomato_cost} --> ${Burger.tomato_cost}")
        print(f"Cheese: ${old_cheese_cost} --> ${Burger.cheese_cost}")

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
            new_ingredient = (input(f"\n Choose an ingredient: \n 1. Patty   ${Burger.patty_cost}\n 2. Lettuce ${Burger.lettuce_cost}\n 3. Pickle  ${Burger.pickle_cost}\n 4. Tomato  ${Burger.tomato_cost}\n 5. Cheese  ${Burger.cheese_cost}\n 6. Done \n Your Choice: ")).lower()

            # Append ingredient to list or end loop
            if new_ingredient == "1" or new_ingredient == "patty":
                self.ingredients += "patty"
                burger_ingredients.append(patty)
                print("Patty added")
                continue
            elif new_ingredient == "2" or new_ingredient == "lettuce":
                self.ingredients += "lettuce"
                burger_ingredients.append(lettuce)
                print("Lettuce added")
                continue
            elif new_ingredient == "3" or new_ingredient == "pickle":
                self.ingredients += "pickle"
                burger_ingredients.append(pickle)
                print("Pickles added")
                continue
            elif new_ingredient == "4" or new_ingredient == "tomato":
                self.ingredients += "tomato"
                burger_ingredients.append(tomato)
                print("Tomatoes added")
                continue
            elif new_ingredient == "5" or new_ingredient == "cheese":
                self.ingredients += "cheese"
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
            print("\n Here's your burger!\n")
            for item in burger_ingredients:
                print(item)


class Pizza(Savory):
    """Requires username, initial total, and starting item list"""
    slice_price = 5.99
    ten_in_price = 14.99
    the_jeremiah_special_price = 0.99

    def __init__(self, username, total, item_list):
        super().__init__(username)
        self.total = 0
        self.item_list = []


    def change_name(self):
        """Change user's name"""

        new_name = input("What would you like your new name to be? ")
        self.username = new_name
        print(f"User's name changed to: {self.username}")


    def known_info(self):
        """Prints user's information"""

        print(f"Username: {self.username}")
        print(f"{self.username} is ordering a pizza.")


    def update_pizza_costs(self):
        """Update class pizza prices"""

        old_slice_cost = Pizza.slice_price
        old_ten_in_cost = Pizza.ten_in_price
        old_jeremiah_special_cost = Pizza.the_jeremiah_special_price

        Pizza.slice_price = float(input("Enter new slice cost: $"))
        Pizza.ten_in_price = float(input("Enter new 10in pizza cost: $"))
        Pizza.the_jeremiah_special_price = float(input("Enter new Jeremiah Special cost: $"))
        
        print("")
        print("Updated pizza prices \n")
        print(f"Slice: ${old_slice_cost} --> ${Pizza.slice_price}")
        print(f"10in Pizza: ${old_ten_in_cost} --> ${Pizza.ten_in_price}")
        print(f"Jeremiah Special: ${old_jeremiah_special_cost} --> ${Pizza.the_jeremiah_special_price}")


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
        
        # Create empty list to store graphics in
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
            pizza_size = (input(f"What size pizza are you feeling? \n 1. A slice  ${Pizza.slice_price}\n 2. 10in     ${Pizza.ten_in_price}\n 3. 40in     ${Pizza.the_jeremiah_special_price}\n 4. No more pizza please \n Your choice: ")).lower()

            if pizza_size == "1" or pizza_size == "slice" or pizza_size == "a slice":
                self.item_list.append("slice")
                graphics.append(slice_graphic)
                continue

            elif pizza_size == "2" or pizza_size == "10" or pizza_size == "10in" or pizza_size == "10 in":
                self.item_list.append("10in")
                graphics.append(ten_in_graphic)
                continue
                          
            elif pizza_size == "3" or pizza_size == "40" or pizza_size == "40in" or pizza_size == "40 in":
                self.item_list.append("jeremiah special")
                graphics.append(the_jeremiah_special_graphic)
                continue
            elif pizza_size == "4":
                print("No pizza ordered")
                break
            else:
                print("Invalid choice. Try again. \n")
                continue
        
        if len(self.item_list) > 1:
            print("\nHere's your pizzas!\n")
        elif len(self.item_list) == 1:
            print("\nHere's your pizza!\n")
        else:
            print("\nYou didn't order anything. How am I supposed to pay rent if you don't buy something?\n")

        # Present the user's order
        for item in graphics:
            print(item)


#------------------- Object Creation -------------------

test_user = Pizza("testuser", 10, ["test"])
test_user.pizza_creator()