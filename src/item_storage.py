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

    # new inventory selection from inventory_app
    def new_inventory(self):
        # ensure that user can save current inventory before opening a new one.
        # because a new inventory list is created on running app, there will always be a current inventory
        user_input = input("Save current inventory? (y/n): ")[0]
        match user_input.lower():
            case 'y':
                self.save_inventory()
                self._create_new_inventory_list()
            case 'n':
                self._create_new_inventory_list()
            case _:
                self._create_new_inventory_list()
    
    #create inventory list dictionary
    def _create_new_inventory_list(self):
        if __debug__:
            print('Creating New Inventory...')
        self.inventory = {}
        self.inventory['type'] = 'An Inventory'
        self.inventory['date'] = 'A long time ago, in a galaxy far, far away...'
        self.inventory['actual_date'] = date.today().isoformat()
        #create list to hold inventory items
        self.inventory['items'] = []
        if __debug__:
            print('New Inventory created.')
    
    def save_inventory(self):
        # output item storage list to file
        if __debug__:
            print('attempting to save inventory...')
        """ensures there is an inventory loaded. 
        Not sure this is necessary - there shouldn't be a point in the running of the program where no inventory exists."""
        if self.inventory != None:
            file_path = self._retrieve_file_path()
            # calls parameters file_path, write-priveledges, UTF-8
            with open(file_path, 'w', encoding='UTF-8') as f:
                # writes inventory to json file in json-formatted str
                f.write(json.dumps(self.inventory))

    def load_inventory(self):
        # load inventory from file
        if __debug__:
            print('attempting to load inventory...')
        # include try/except to allow for errors in entering file path
        try:
            file_path = self._retrieve_file_path()
            # calls paramenters file_path, read-priveledges, UTF-8 encoding
            with open(file_path, 'r', encoding='UTF-8') as f:
                self.inventory = json.loads(f.read())
        except OSError:
            print('File path or file does not exist. Try again.')

    def add_inventory_items(self, item_name, item_count):
        if __debug__:
            print('Adding items to inventory')
        self.inventory['items'].append({'item' : item_name, 'count' : int(item_count)})

    def _retrieve_file_path(self):
        # where to store/retrieve inventory
        save_where = input("Please enter the path and filename: ")
        return save_where
    
    # print list
    def list_inventory(self):
        if __debug__:
            print('printing loaded inventory to screen')
        # runs through inventory dictionary. prints type, date, etc., then the items in the inventory
        for k, v in self.inventory.items():
            if k == 'items':
                print('what\'s in the house:')
                for item in v:
                    # create f strings so string return can read from list
                    print(f'\t {item["item"]:15} \t {item["count"]}')
            elif k == 'actual date':
                print(f'{k}: \t {v}')
            else:
                print(f'{k}: \t\t {v}')
    
    # show total count
    def full_count(self):
        total_count = 0
        for item in self.inventory['items']:
            total_count += item['count']
        print(f'the total number of items in the house is: \t {total_count}')

    def search_storage(self):
        where_is = input('What are you looking for: ')
        for item in self.inventory['items']:
            if item['item'] == where_is:
                print(f'There are {item["count"]} of those.')
            else:
                continue