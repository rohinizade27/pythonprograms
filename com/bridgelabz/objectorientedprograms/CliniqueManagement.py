from com.bridgelabz.utility.Oops_Utility import CliniqueManagement

if __name__ == '__main__':

    cliniqueManagement_obj = CliniqueManagement()


    patient_file=cliniqueManagement_obj.readJsonfileofPatient()
    #print(patient_file)
    appointment_file=cliniqueManagement_obj.readJsonfileofAppoinment()
    #print(appointment_file)

    cliniqueManagement_obj.getUserInput()




