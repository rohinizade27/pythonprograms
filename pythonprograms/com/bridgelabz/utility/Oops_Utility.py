
import json

class InventoryManagement:

    inventory_details_dict = {
        "inventory_details": [{"Item_Name": "wheat", "weight_in_kgs": 50, "weight_per_kg": 35},
                              {"Item_Name": "rice", "weight_in_kgs": 40, "weight_per_kg": 45},
                              {"Item_Name": "Beans", "weight_in_kgs": 25, "weight_per_kg": 30},
                              {"Item_Name": "Lentils", "weight_in_kgs": 60, "weight_per_kg": 52},
                              {"Item_Name": "groundnut", "weight_in_kgs": 45, "weight_per_kg": 62}
                              ]}

    s = json.dumps(inventory_details_dict)
    with open('Inventory.json', 'w') as f:
        f.write(s)

    def __init__(self):

        with open('Inventory.json', 'r') as file:
            json_str = file.read()
            json_value = json.loads(json_str)

        #   print(json_value)
        self.existing_material_list = json_value["inventory_details"]
        print(self.existing_material_list)

    def display_items(self):
        print("Available items are:")
        print("********* ******** **************")
        print("Item_Name  Weight  weight_per_kg")
        print("********* ******** **************")
        for i in range(len(self.existing_material_list)):
            items = self.existing_material_list [i]["Item_Name"]
            items_weight = self.existing_material_list[i]["weight_in_kgs"]
            items_weight_per_kg = self.existing_material_list[i]["weight_per_kg"]

            print(items,"     ",items_weight,"      " ,items_weight_per_kg)






    def getUserInput(self):
        print("1.Buy Items \n 2.View items \n 3 exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            self.inventoryManagementLogic()

        elif choice==2:
            self.display_items()



    def inventoryManagementLogic(self):
        self.display_items()
        user_item =input("please Enter the item you want to buy:")

        for i in range(len(self.existing_material_list)):
            if user_item == self.existing_material_list [i]["Item_Name"]:
                user_item_in_kgs=input("How many kgs",user_item,"you want??")
                user_item_per_kg=self.existing_material_list [i]["weight_per_kg"]













