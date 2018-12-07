
import json

class InventoryManagement:

    inventory_details_dict = {
        "inventory_details": [{"Item_Name": "wheat", "weight_in_kgs": 50, "weight_per_kg": 35},
                              {"Item_Name": "rice", "weight_in_kgs": 40, "weight_per_kg": 45},
                              {"Item_Name": "beans", "weight_in_kgs": 25, "weight_per_kg": 30},
                              {"Item_Name": "lentils", "weight_in_kgs": 60, "weight_per_kg": 52},
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

        # print(self.existing_material_list)



    def display_items(self):
        #print(type(self.existing_material_list))
        print("Available items are:")
        print("********* ******** **************")
        print("Item_Name  Weight   weight_per_kg")
        print("********* ******** **************")
        for i in range(len(self.existing_material_list)):
            items = self.existing_material_list [i]["Item_Name"]
            items_weight = self.existing_material_list[i]["weight_in_kgs"]
            items_weight_per_kg = self.existing_material_list[i]["weight_per_kg"]

            print(items,"     ",items_weight,"      " ,items_weight_per_kg)




    def getUserInput(self):
        ch=input("do you want to continue:y/n:")
        while ch=='y':
            print(" \n 1.Buy Items \n 2.View items \n 3.Exit")
            choice = int(input("Enter your choice:"))
            if choice == 1:
                self.inventoryManagementLogic()

            elif choice == 2:
                self.display_items()

            else:
                print("!!!..Invalid choice..!!!")


    def update_iteams(self,user_item_in_kgs,user_item):
        for i in range(len(self.existing_material_list)):
            if user_item == self.existing_material_list[i]["Item_Name"]:
                total_weight=self.existing_material_list[i]["weight_in_kgs"]
                total_weight=total_weight-user_item_in_kgs
                self.existing_material_list[i]["weight_in_kgs"]=total_weight



    def inventoryManagementLogic(self):

        print("Available items are:")
        for i in range(len(self.existing_material_list)):
            items = self.existing_material_list[i]["Item_Name"]
            print(items)

        print("\n")
        user_item = input("please Enter the item you want to buy:")

        for i in range(len(self.existing_material_list)):
            if user_item in self.existing_material_list[i]["Item_Name"]:
            #if user_item == self.existing_material_list [i]["Item_Name"]:
                user_item_in_kgs=int(input("How many kgs you want??"))
                user_item_per_kg=self.existing_material_list [i]["weight_per_kg"]
                total_price=user_item_in_kgs*user_item_per_kg
                print("total price:",total_price)
                self.update_iteams(user_item_in_kgs,user_item)
                self.display_items()
                break
            else:
                pass

        if user_item not in self.existing_material_list[i]["Item_Name"]:
            print("Enter item is not available please make it available:")
            weight = int(input("Enter the weight of new item:"))
            weight_per_kg = int(input("Enter the weight of new item per kg"))

            new_dict = {}
            new_dict.update({"Item_Name": user_item, "weight_in_kgs": weight, "weight_per_kg": weight_per_kg})

            with open('Inventory.json', 'r') as file:
                json_str = file.read()
                new_json_value = json.loads(json_str)
                print(type(new_json_value))
                updated_list = new_json_value["inventory_details"]
                updated_list.append({"Item_Name": user_item, "weight_in_kgs": weight, "weight_per_kg": weight_per_kg})
                print(updated_list)
                self.display_updated_file(updated_list)
                s = json.dumps(updated_list)
                with open('Inventory.json', 'w') as f:
                    f.write(s)

    def display_updated_file(self,updated_list):
        print("Available items are:")
        print("********* ******** **************")
        print("Item_Name  Weight   weight_per_kg")
        print("********* ******** **************")
        for i in range(len(updated_list)):
            items = updated_list[i]["Item_Name"]
            items_weight = updated_list[i]["weight_in_kgs"]
            items_weight_per_kg = updated_list[i]["weight_per_kg"]

            print(items, "     ", items_weight, "      ", items_weight_per_kg)

































