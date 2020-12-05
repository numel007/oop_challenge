# Inherits username from Sweet clas, provides methods for ordering cake
class Cake():
    """Instantiates with username"""

    # Cake Prices
    white_cake_price = 4.99
    crepe_cake_price = 5.49
    birthday_cake_price = 18.01

    def __init__(self, username, total = 0, item_list = []):
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
        cls.birthday_cake_price = float(input("Enter new birthday cake price: $"))

        # Print comparison of old to new price
        print("")
        print("Updated cake prices \n")
        print(f"White cake: ${old_white_cake_cost}  -->  ${cls.white_cake_price}")
        print(f"Crepe cake: ${old_crepe_cake_price}  -->  ${cls.crepe_cake_price}")
        print(f"Birthday cake: ${old_birthday_cake_price}  -->  ${cls.birthday_cake_price}")


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
            cake_choice = (input(f"What cake do you want? \n 1. White cake  ${Cake.white_cake_price} \n 2. Crêpe Cake  ${Cake.crepe_cake_price} \n 3. Whole birthday cake (with candles!) ${Cake.birthday_cake_price} \n 4. No cake \n Your choice: ")).lower()

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
            print("\nYou didn't order anything. I'm not running a charity. Get the hell outta my store.")

        # Present the user's order
        for graphic in graphics_list:
            print(graphic)