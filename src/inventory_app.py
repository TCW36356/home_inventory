"""Represents application user interface"""

import os #imports os to allow for clearing the python screen
from item_storage import itemStorage
import time

# create class so that stateful environment is created
class InventoryApp:

    def __init__(self):
        # methods referenced by menu
        self.NEW_INVENTORY='1'
        self.LOAD_INVENTORY='2'
        self.SHOW_ITEMS='3'
        self.ADD_ITEMS='4'
        self.SAVE_INVENTORY='5'
        self.PLAY_VIDEO='6'
        self.EXIT='7'
        
        self.its_working = True
        self.item_storage = itemStorage()

    def display_menu(self):
        # show the menu
        print('\t\t\t(Irreverent) Household Inventory\n')
        print('\t\t1. New Inventory')
        print('\t\t2. Load Inventory')
        print('\t\t3. Show Items in House')
        print('\t\t4. Add Items')
        print('\t\t5. Save Inventory')
        print('\t\t6. Play Video')
        print('\t\t7. Exit\n')
        

    def process_menu_choice(self):
        # Accept user input of menu choice, execute method.
        self.menu_choice = input('Choose menu item number: ')[0] # this should only take the first char entered.
        if __debug__:
            print(f'You entered: {self.menu_choice}')
        match self.menu_choice:
            case self.NEW_INVENTORY:
                self.new_inventory()
            case self.LOAD_INVENTORY:
                self.load_inventory()
            case self.SHOW_ITEMS:
                self.show_inventory()
            case self.ADD_ITEMS:
                self.add_to_inventory()
            case self.SAVE_INVENTORY():
                self.save_inventory()
            case self.PLAY_VIDEO:
                self.joke_page()
            case self.EXIT:
                if __debug__:
                    print('This message will self-destruct. Have a nice day!')
                self.its_working = False
                self.clear_screen()
            case _:
                print('Try again, following instructions this time!')


    def new_inventory(self):
        if __debug__:
            print('new_inventory() method called...')

    def load_inventory(self):
        pass    

    def save_inventory(self):
        pass

    def add_to_inventory(self):
        pass

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

    def joke_page(self):
        self.clear_screen()
        print('\tI just started learning Python last month.\n\n')
        time.sleep(5) # adds 5 second pause
        print('\t Did you really think there was going to be a video here?')
        time.sleep(5) # another 5 second pause
        self.clear_screen()
    
    def turn_ignition(self):
        # starts program, begin with clearing screen.
        self.clear_screen()
        while self.its_working:
            self.display_menu()
            self.process_menu_choice()
        
