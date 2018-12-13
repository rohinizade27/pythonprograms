"""
purpose   : Create a JSON file having Inventory Details for Rice, Pulses and Wheats
            with properties name, weight, price per kg.Calculate the value for every
            Inventory and output the JSON String

@Author   : Rohini Zade
@version  : 1.0
@since    : 4-12-2018

"""
from com.bridgelabz.utility.Oops_Utility import InventoryManagement

if __name__ == '__main__':
    inventory_management_obj = InventoryManagement()
    inventory_management_obj.getUserInput()
   



