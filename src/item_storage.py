"""Creates and stores list of items, allows for adding items, outputs json file/imports json file, lists items"""

#import json, so that requirement can be met
import json
#import date, so that can be displayed
from datetime import date

# create class, so multiple lists can be created
class item_storage:

    #create dictionary
    def _create_new_inventory_list(self):
        if __debug__:
            print('Creating New Inventory...')
        self.inventory = {}
        self.inventory['type'] = 'An Inventory'
        self.inventory['date'] = 'A long time ago, in a galaxy far, far away...'
        self.inventory['actual date'] = date.today().isoformat()
        #create list to hold inventory items
        self.inventory['items'] = []
        if __debug__:
            print('New Inventory created.')

