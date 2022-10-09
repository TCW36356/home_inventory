"""Represents application user interface"""

import os #imports os to allow for clearing the python screen

class InventoryApp:

    def __init__(self):
        pass

    def display_menu(self):
        pass

    def process_menu_choice(self):
        pass

    def new_inventory(self):
        if __debug__:
            print('new_inventory() method called...')
        
    
    def clear_screen(self): #clears screen. requires importing os module:
        os.system('clear') #apparently works on windows as long as file is called from build.sh file
        return()

