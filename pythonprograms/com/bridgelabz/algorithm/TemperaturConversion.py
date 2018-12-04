from com.bridgelabz.utility.Utility  import Utility

utility_obj=Utility()
print("Enter the temprature in fahrenheit:")
fahrenheit_Temprature=utility_obj.inputIntiger()
utility_obj.convertTempToCelcius(fahrenheit_Temprature)
print("Enter the temprature in celcius:")
celcius_temprature=utility_obj.inputIntiger()
utility_obj.convertTempTofahrenheit(celcius_temprature)


