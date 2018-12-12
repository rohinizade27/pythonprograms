import json
from com.bridgelabz.utility.Datastructure_utility import QueeByLinklist


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
        # print(type(self.existing_material_list))
        print("Available items are:")
        print("********* ******** **************")
        print("Item_Name  Weight   weight_per_kg")
        print("********* ******** **************")
        for i in range(len(self.existing_material_list)):
            items = self.existing_material_list[i]["Item_Name"]
            items_weight = self.existing_material_list[i]["weight_in_kgs"]
            items_weight_per_kg = self.existing_material_list[i]["weight_per_kg"]

            print(items, "     ", items_weight, "      ", items_weight_per_kg)

    def getUserInput(self):
        ch = input("do you want to continue:y/n:")
        while ch == 'y':
            print(" \n 1.Buy Items \n 2.View items \n 3.Exit")
            choice = int(input("Enter your choice:"))
            if choice == 1:
                self.inventoryManagementLogic()

            elif choice == 2:
                self.display_items()
            # self.display_updated_file()

            else:
                print("!!!..Invalid choice..!!!")

    def update_iteams(self, user_item_in_kgs, user_item):
        for i in range(len(self.existing_material_list)):
            if user_item == self.existing_material_list[i]["Item_Name"]:
                total_weight = self.existing_material_list[i]["weight_in_kgs"]
                total_weight = total_weight - user_item_in_kgs
                self.existing_material_list[i]["weight_in_kgs"] = total_weight

    def inventoryManagementLogic(self):

        print("Available items are:")
        for i in range(len(self.existing_material_list)):
            items = self.existing_material_list[i]["Item_Name"]
            print(items)

        print("\n")
        user_item = input("please Enter the item you want to buy:")

        for i in range(len(self.existing_material_list)):
            if user_item in self.existing_material_list[i]["Item_Name"]:
                # if user_item == self.existing_material_list [i]["Item_Name"]:
                user_item_in_kgs = int(input("How many kgs you want??"))
                user_item_per_kg = self.existing_material_list[i]["weight_per_kg"]
                total_price = user_item_in_kgs * user_item_per_kg
                print("total price:", total_price)
                self.update_iteams(user_item_in_kgs, user_item)
                self.display_items()
                break
            else:
                pass

        if user_item not in self.existing_material_list[i]["Item_Name"]:
            print("Enter item is not available please make it available:")
            weight = int(input("Enter the weight of new item:"))
            weight_per_kg = int(input("Enter the weight of new item per kg:"))

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

    def display_updated_file(self, updated_list):
        print("Available items are:")
        print("********* ******** **************")
        print("Item_Name  Weight   weight_per_kg")
        print("********* ******** **************")
        for i in range(len(updated_list)):
            items = updated_list[i]["Item_Name"]
            items_weight = updated_list[i]["weight_in_kgs"]
            items_weight_per_kg = updated_list[i]["weight_per_kg"]

            print(items, "     ", items_weight, "      ", items_weight_per_kg)


######################################################################################
import datetime
import re


class RegularExpression:
    def __init__(self):
        self.string = "Hello <<name>>, We have your full name as <<full name>> " \
                      "in our system. your contact number is 91-xxxxxxxxxx. " \
                      "Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2016."

    def validateUserInputs(self):
        name = input("Enter your name:")
        fullname = input("Please Enter your full name: ")
        mobile_number = (input("Enter your mobile number:"))
        current_date = str(datetime.date.today())

        regex_name = re.compile("[<]{2}[a-z]{4}[>]{2}")
        replace_name = regex_name.sub(name, self.string)
        print("\n")
        print(replace_name)

        regex_full_name = re.compile("[<]{2}[a-z]{4}\s[a-z]{4}[>]{2}")
        replace_full_name = regex_full_name.sub(fullname, self.string)
        print(replace_full_name)

        regex_mob_no = re.compile(r"91-x*")
        replace_mob_no = regex_mob_no.sub(mobile_number, self.string)
        print(replace_mob_no)

        regex_curr_date = re.compile(r"\d{2}/\d{2}/\d{4}")
        replace_curr_date = regex_curr_date.sub(current_date, self.string)
        print(replace_curr_date)
        print("\n")

        substitutions = {"<<name>>": name, "<<full name>>": fullname,
                         "91-xxxxxxxxxx": mobile_number, "01/01/2016": current_date}

        return substitutions

    def RegularExpressionLogic(self, substitutions):
        template = sorted(substitutions, key=len, reverse=True)
        regex = re.compile('|'.join(map(re.escape, template)))
        return regex.sub(lambda match: substitutions[match.group(0)], self.string)


###################################################################################################
import random
import itertools


class DeckOfCards:
    def __init__(self):
        self.cards_categoeies = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.rank = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        # self.cards_of_each_player=cards_of_each_player

    def deckOfCardsLogic(self):
        print("Cards after shuffling:")
        print("*********************")
        for i in itertools.product(self.cards_categoeies, self.rank):
            self.cards_categoeies.append(i)
        random.shuffle(self.cards_categoeies)
        card_list = self.cards_categoeies
        print(card_list)
        return card_list

    def sortedDeckOfCardsLogic(self):

        print("sorted Cards are:")
        print("******************")
        cards = []
        cards_array = []
        for i in range(len(self.cards_categoeies)):
            for j in range(len(self.rank)):
                cards.append(self.cards_categoeies[i])
                cards.append(self.rank[j])
            cards_array.append(cards)
        # print(cards)
        row = 52
        column = 2
        card_matrix = [[0 for j in range(column)] for i in range(row)]

        k = 0
        r = 1
        for i in range(row):

            for j in range(column):

                if k < len(cards):
                    if k <= r:
                        card_matrix[i][j] = cards[k]
                        k = k + 1
            r = r + 2
        random.shuffle(card_matrix)
        return card_matrix

    def print2DdeckofCards(self, card_list):
        row = 10
        column = 10
        matrix = [[0 for j in range(column)] for i in range(row)]

        k = 0
        r = 9
        for i in range(row):

            for j in range(column):

                if k < len(card_list):
                    if i == 0 and j == 0:
                        matrix[i][j] = "player-1: "
                    elif i == 1 and j == 0:
                        matrix[i][j] = "player-2: "
                    elif i == 2 and j == 0:
                        matrix[i][j] = "player-3: "
                    elif i == 3 and j == 0:
                        matrix[i][j] = "player-4: "
                    elif k <= r and k <= 35:
                        matrix[i][j] = card_list[k]
                        k = k + 1
            r = r + 10
        # print(matrix)
        print("\n")
        print("Two D matrix of shuffled cards:")
        print("*******************************")
        for row in matrix:
            for element in row:
                if element != 0:
                    if element != 'Clubs':
                        if element != "Diamonds":
                            if element != "Hearts":
                                if element != "Spades":
                                    print(element, end=" ")

            print()


##########################################################################################

class SortedDeckOfCards:

    def __init__(self, cards_of_each_player):
        self.cards_of_each_player = cards_of_each_player
        # print(self.cards_of_each_player)

    def rankCards(self):
        players_card = self.cards_of_each_player
        for i in range(len(players_card)):
            q_linklist_obj.insertElementAtRear(players_card[i])

        c_list = []
        for j in range(len(players_card) + 1):
            deleted_item = q_linklist_obj.removeElementFromFront()
            if deleted_item != None:
                c_list.append(deleted_item)

        for c in range(0, len(c_list)):
            for k in range(0, len(c_list) - c - 1):
                if c_list[k][1] > c_list[k + 1][1]:
                    temp = c_list[k]
                    c_list[k] = c_list[k + 1]
                    c_list[k + 1] = temp

        return c_list


q_linklist_obj = QueeByLinklist()

##########################################################################################
import json


class CliniqueManagement:

    def __init__(self):
        pass

    def getUserInput(self):

        print("welcome to Clinique Management System..!!:")
        ch = input("do you want to continue:y/n:")
        while ch == 'y':
            print(" \n 1.Options for Doctor \n 2.Options for patients  \n 3.Exit")
            choice = int(input("Enter your choice:"))
            if choice == 1:
                print("\n 1.Add Doctor \n 2.view Doctors \n 3.Exit")
                ch1 = int(input("Enter your choice:"))
                if ch1 == 1:
                    self.addDoctors()
                elif ch1 == 2:
                    self.viewDoctors()
                elif ch1 == 3:
                    break
                else:
                    print("!!..Invalid choice..!!")
                    break
            elif choice == 2:
                print("\n 1.Add Appointment \n 2.Search Doctor \n 3.Exit")
                ch2 = int(input("Enter your choice:"))
                if ch2 == 1:
                    self.addAppointment()
                elif ch2 == 2:
                    print("\n 1.Search Doctor by Name \n 2.Search Doctor Id \n 3.Search Doctor Specialization \n 4.Exit")
                    ch3=int(input("Enter your choice:"))
                    if ch3 == 1:
                        self.searchDoctorbyName()
                    elif ch3 == 2:
                        self.searchDoctorbyId()
                    elif ch3 == 3:
                        self.searchDoctorbySpecialization()


                elif ch2 == 3:
                    break
                else:
                    print("!!..Invalid choice..!!")
                    break
            elif choice == 3:
                break
            else:
                print("!!!..Invalid choice..!!!")
                break

    def readJsonfileofDoctor(self):

        doctors_information = {
                    "doctor": [{
                                    "Name": "Dr.Arman Singh",
                                    "Id": 101,
                                    "specialization": "Cardiologist",
                                    "Availability": "AM"
                                },
                                {
                                    "Name": "Dr.Shital Patil",
                                    "Id": 102,
                                    "specialization":"Neurologist",
                                    "Availability": "PM"
                                },
                                {
                                    "Name": "Dr.Varun Shaha",
                                    "Id": 103,
                                    "specialization": "Addiction psychiatrist",
                                    "Availability": "AM"

                                }]
                               }
        # s = json.dumps(doctors_information)
        # with open('Doctors_info.json', 'w') as file_obj:
        #     file_obj.write(s)
        #     file_obj.close()

        with open('Doctors_info.json', 'r') as file_obj:
            json_str = file_obj.read()
            json_value = json.loads(json_str)

            file_obj.close()

        return json_value

    def readJsonfileofPatient(self):

        patient_information = {
            "patient":[{
                    "Name": "sahil sharma",
                    "Id": 12,
                    "Age": 24,
                    "mobile number": "7865232419"
                     },
                    {
                    "Name": "pratik Patil",
                    "Id": 12,
                    "Age": 34,
                    "mobile number": "8956345213"
                     },
                    {
                    "Name": "sampada dagwar",
                    "Id": 14,
                    "Age": 21,
                    "mobile number": "9420036520"

                    },

                   {
                    "Name": "nidhi kamath",
                    "Id": 15,
                    "Age": 22,
                    "mobile number": "8976348562"

                   }]
         }
        s = json.dumps(patient_information)
        with open('Patient_info.json', 'w') as file_obj:
            file_obj.write(s)

        with open('Patient_info.json', 'r') as file_obj:
            json_str = file_obj.read()
            json_value = json.loads(json_str)

        file_obj.close()

        return json_value



    def readJsonfileofAppoinment(self):

        appoinment_information = {
            "Dr.Arman Singh":[{"patient Name": "sahil sharma","Id": 12,"Age": 24,"mobile number": "7865232419", "time":"AM"},
                              {"patient Name": "pratik Patil","Id": 12,"Age": 34,"mobile number": "8956345213", "time":"AM"}],
            "Dr.Shital Patil":[{"patient Name": "sampada dagwar","Id": 14,"Age": 21,"mobile number": "9420036520", "time":"PM"}],
            "Dr.Varun Shaha":[{"patient Name": "nidhi kamath", "Id": 15,"Age": 22,"mobile number": "8976348562" ,"time":"AM"}],
            "Dr. Amit Joshi": [{"patient Name": "pratik Patil","Id": 12,"Age": 34,"mobile number": "8956345213", "time":"AM"}]}


        s = json.dumps(appoinment_information)
        with open('appoinment_info.json', 'w') as file_obj:
            file_obj.write(s)

        with open('appoinment_info.json', 'r') as file_obj:
            json_str = file_obj.read()
            json_value = json.loads(json_str)

        file_obj.close()

        return json_value


    def addDoctors(self):
        doctor_name=input("Enter Name:")
        doctor_id=int(input("Enter Id:"))
        specilization=input("Enter Specialization:")
        availability=input("Enter Availability(AM/PM/Both):")

        with open('Doctors_info.json', 'r') as file_obj:

            json_str = file_obj.read()
            new_json_value = json.loads(json_str)
            file_obj.close()

        new_dict={"Name": doctor_name , "Id": doctor_id, "specialization": specilization, "Availability": availability}

        with open('Doctors_info.json', 'w') as file_obj:
            new_json_value["doctor"].append(new_dict)
            file_obj.write(json.dumps(new_json_value))
            file_obj.close()


    def viewDoctors(self):
        doctor_dict=self.readJsonfileofDoctor()
        doctor_list=doctor_dict["doctor"]

        print(type(doctor_list))
        print("Available Doctors are:")
        print("----------------------------------------")
        print("Name                    specialization ")
        print("----------------------------------------")

        for i in range(len(doctor_list)):
            name = doctor_list[i]["Name"]
            specialization = doctor_list[i]["specialization"]

            print(name, "          ",specialization)

    def addAppointment(self):
        print("Name of doctors")
        print("---------------")
        doctor_dict = self.readJsonfileofDoctor()
        doctor_list = doctor_dict["doctor"]




        for i in range(len(doctor_list)):
            name = doctor_list[i]["Name"]

            print(name)


        doctor_name=input("Which doctor's appointment you want..??")
        time=input("please Enter appointment time..(AM/PM/Both)=>")

        appointment_dict = self.readJsonfileofAppoinment()
        appointment_list = appointment_dict[doctor_name]
        #print(len(appointment_list))


        if len(appointment_list) <5:
            for i in range(len(doctor_list)):
                if doctor_name == doctor_list[i]["Name"]:
                    if time == doctor_list[i]["Availability"]:
                        print("Doctor is available..!! please Enter the patient details:")
                        name = input("Enter patient name:")
                        id = int(input("Enter patient Id:"))
                        age = int(input("Enter patient age:"))
                        mob_no = input("Enter patient's mobile number:")

                        #self.addpatient(name,id,age,mob_no)
                        with open('appoinment_info.json', 'r') as file_obj:
                            json_str = file_obj.read()
                            new_json_value = json.loads(json_str)
                            file_obj.close()

                        new_dict = {"patient Name": name ,"Id": id,"Age": age,"mobile number": mob_no, "time":time}

                        with open('appoinment_info.json', 'w') as file_obj:
                            new_json_value[doctor_name].append(new_dict)
                            file_obj.write(json.dumps(new_json_value))
                            file_obj.close()

                        print("your appointment is fixed..")

                    else:
                         print("sorry..Doctor is not available..!! ")
                # else:
                #     print("sorry.. you have entered wrong name..!!")



    def searchDoctorbyName(self):
        doctor_dict = self.readJsonfileofDoctor()
        doctor_list = doctor_dict["doctor"]
        name=input("Enter doctor name you want to search:")
        for i in range(len(doctor_list)):
            if name == doctor_list[i]["Name"]:
                print(name, "Doctor is available..!!")
                break
            else:
                print(name, "Doctor is not available..!!")
                break


    def searchDoctorbyId(self):
        pass


    def searchDoctorbySpecialization(self):
        pass




    # def addpatient(self, name, id, age, mob_no):
    #     # patient_dict = self.readJsonfileofPatient()
    #     # patient_list = patient_dict["patient"]
    #
    #     with open("patient Name", 'r') as file_obj:
    #         json_str = file_obj.read()
    #         new_json_value = json.loads(json_str)
    #         file_obj.close()
    #
    #     new_dict = {"Name":name,"Id": id,"Age": age,"mobile number": mob_no}
    #
    #     with open("patient Name", 'w') as file_obj:
    #         new_json_value["patient"].append(new_dict)
    #         file_obj.write(json.dumps(new_json_value))
    #         file_obj.close()



CliniqueManagement_obj = CliniqueManagement()
CliniqueManagement_obj.readJsonfileofDoctor()