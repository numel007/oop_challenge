from Welcome import Welcome

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

    print("")
    global created_user
    created_user = Welcome(username, hunger_status)


def welcome_options(user):

    while True:

        selected_option = (input("Select an option\n 1. Change name\n 2. Change hunger status\n 3. View user info\n 4. Quit\n Your choice: ")).lower()

        if selected_option == "1" or selected_option == "change name" or selected_option == "name":
            user.change_name()
            break
        elif selected_option == "2" or selected_option == "change hunger status" or selected_option == "hunger":
            user.is_hungry()
            break
        elif selected_option == "3" or selected_option == "view info" or selected_option == "view user info" or selected_option == "info":
            user.known_info()
            break
        elif selected_option == "4" or selected_option == "exit" or selected_option == "quit":
            print("Exiting program")
            exit()
        else:
            print("Invalid input. Try again.\n")
            continue

def change_name():
    """Change user's name"""

    new_name = input("What would you like your new name to be? ")
    print(f"User's name changed to: {new_name}")
    return new_name
# ------------ Test Object Creation ------------
create_user()
created_user.savory_or_sweet()