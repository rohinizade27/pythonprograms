"""
purpose   : To create Clinique Management Program

@Author   : Rohini Zade
@version  : 1.0
@since    : 11-12-2018

"""

from com.bridgelabz.utility.Oops_Utility import CliniqueManagement

if __name__ == '__main__':

    cliniqueManagement_obj = CliniqueManagement()
    patient_file=cliniqueManagement_obj.readJsonfileofPatient()
    appointment_file=cliniqueManagement_obj.readJsonfileofAppoinment()
    cliniqueManagement_obj.getUserInput()




