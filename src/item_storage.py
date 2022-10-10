"""Creates and stores list of items, allows for adding items, outputs json file/imports json file, lists items"""

#import json, so that requirement can be met
import json
#import date, so that can be displayed
from datetime import date

# create class, so multiple lists can be created
class itemStorage:

    # create init to define class-specific variables (may not be the right term)
    def __init__(self):
        # needs to create a new inventory list when called
        self._create_new_inventory_list()

    #create inventory list dictionary
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
    
    def add_inventory_items(self, item_name, item_count):
        if __debug__:
            print('Adding items to inventory')
        self.inventory['items'].append({'item' : item_name, 'count' : int(item_count)})

    def _retrieve_file_path(self):
        # where to store/retrieve inventory
        save_where = input("Please enter the path and filename:")
        return save_where
    
    # print list
    def list_inventory(self):
        if __debug__:
            print('printing loaded inventory to screen')
        #runs through inventory dictionary. prints type, date, etc., then the items in the inventory
        for k, v in self.inventory.items():
            if k == 'items':
                print('what\'s in the house:')
                for item in v:
                    # create f strings so string return can read from list
                    print(f'\t {item["item"]:15} \t {item["count"]}')
            else:
                print(f'{k}: \t {v}')
    
    # show total count
    def full_count(self):
        total_count = 0
        for item in self.inventory['items']:
            total_count += item['count']
        print(f'the total number of items in the house is: \t {total_count}')

