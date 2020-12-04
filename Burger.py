from Savory import Savory

# Inherits username from Savory class, provides methods for ordering a burger
class Burger(Savory):
    """Instantiate with username"""

    # Burger ingredient costs
    patty_cost = 1.49
    lettuce_cost = 0.05
    pickle_cost = 0.15
    tomato_cost = 0.25
    cheese_cost = 0.75

    def __init__(self, username, total = 0, ingredients = []):
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
            new_ingredient = (input(f"\n Choose an ingredient: \n 1. Patty   ${Burger.patty_cost}\n 2. Lettuce ${Burger.lettuce_cost}\n 3. Pickle  ${Burger.pickle_cost}\n 4. Tomato  ${Burger.tomato_cost}\n 5. Cheese  ${Burger.cheese_cost}\n 6. Done \n Your Choice: ")).lower()

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