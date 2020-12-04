from Welcome import Welcome
from Savory import Savory
from Sweet import Sweet
from Burger import Burger
from Pizza import Pizza
from Cake import Cake
from Pie import Pie

def create_user():
    username = input("Input your name: ")

    while True:
        hunger_status = (input("Are you hungry? (Y/N): ")).lower()

        if hunger_status == "y" or hunger_status == "yes":
            hunger_status = True
            break
        elif hunger_status == "n" or hunger_status == "no":
            hunger_status = False
            break
        else:
            print("Invalid input. Try again.\n")
            continue

    global created_user
    created_user = Welcome(username, hunger_status)


# ------------ Test Object Creation ------------
create_user()