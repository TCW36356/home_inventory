"""Explicit main execution module."""

from inventory_app import InventoryApp


def main():
	# start app
	home_inventory_app = InventoryApp()
	home_inventory_app.turn_ignition()



# Call main() if this is the main execution module
if __name__ == '__main__':
	main()