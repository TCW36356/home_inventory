"""Represents application user interface"""

import os #imports os to allow for clearing the python screen
from item_storage import itemStorage

# create class so that stateful environment is created
class InventoryApp:

    def __init__(self):
        self.item_storage = itemStorage()

    def display_menu(self):
        pass

    def process_menu_choice(self):
        pass

    def new_inventory(self):
        if __debug__:
            print('new_inventory() method called...')
        
    
    def clear_screen(self): #clears screen. requires importing os module
        os.system('clear') #apparently works on windows as long as file is called from build.sh file

    def show_inventory(self):
        if __debug__:
            print('showing the inventory')
        # this should clear the screen, show the inventory, show the full count, then, after the user presses a key, clear again.
        self.clear_screen()
        self.item_storage.list_inventory()
        self.item_storage.full_count()
        input('Press any key to continue: ')
        self.clear_screen()


