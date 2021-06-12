# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# ------------------------------------------#
# Title: Booking_Quote_System.py
# Desc: Assignment Booking Quote System - Create the Booking Quote application
# Change Log: (Who, When, What)
# AHernandez, 2021-June-08, Created File for Booking Quote application and skeletal structure 
# AHernandez, 2021-June-11, Created menu structure and IO class 
# ------------------------------------------#
import time
from datetime import datetime 
strChoice = '' 
lstTbl = []
dictRow = {}
menuOptions = '\nWelcome to the Booking System.  Please choose from one of the following:\n\t[P] Show Current Rates\n\t[N] Create a New Order\n\t[X] Quit'
strMenuOption = 'n','p','x'
 

# -- INPUT/OUTPUT -- #
class Order:
    def __init__(self, orderId, customerName, packageDescription, hazardousFlag, weight, volume, deliveryDate):
        self.__orderId = orderId
        self.__customerName = customerName
        self.__packageDescription = packageDescription
        self.__hazardousFlag = hazardousFlag
        self.__weight = weight
        self.__volume = volume
        self.__deliveryDate = deliveryDate

    
class IO:
    def choice(menuOptions):
        choice = input("Please select an Option: ").lower().strip()
        try:
            if choice.lower() in (menuOptions):
                return choice
            else:
                raise
        except RuntimeError:
            print("Ivalid option selected. Please try again\n")  
            
    def add_new_order(orderId):
         
        orderId = len(dictRow) + 1
        customerName = input("Please enter the customers Name: ")
        packageDescription = input("Please enter the package description: ")
        hazFlag = False
        hazardousFlag = input("Does the package contain any hazardous material? ").strip().lower()
        if hazardousFlag == 'yes':
            hazFlag = True
        else:
            hazFlag
        while True:
            try:
                weight = float(input("Enter weight of package: "))
                if weight <= 10.0:
                    break
                else:
                    print("packages must be under 10Kg")
            except ValueError:
                print("Weight must be a float value")
                
        while True:
            try:    
                height = float(input("Enter package height (in meters): "))
                break
            except ValueError:
                print("height must be a float value")
                
        while True:
            try:            
                length = float(input("Enter package length (in meters): "))
                break
            except ValueError:
                print("height must be a float value")
                
        while True:
            try:                 
                width = float(input("Enter package width (in meters): "))
                break
            except ValueError:
                print("width must be a float value")
                
        volume = height * length * width
        while True:
            deliveryDate = input('Enter a delivery date(YYYY-MM-DD): ').strip() 
            try:
                datetime.strptime(deliveryDate, '%Y-%m-%d')
                break
            except ValueError:
                print("Incorrect Start Date format, It should be YYYY-MM-DD") 
        lstTbl = customerName, packageDescription, hazFlag, weight, volume, deliveryDate
        dictRow[orderId] = list(lstTbl)
        print (dictRow)
        return orderId, customerName, packageDescription, hazFlag, weight, volume, deliveryDate       

                
class Main:    
    def main():
        global intOrderId
        intOrderId = 1
        try:
            while True:
                print(menuOptions)
                strChoice = IO.choice(strMenuOption)
                if strChoice == 'x':
                    break
                elif strChoice == 'p':
                    pass
                elif strChoice == 'n':
                    intOrderId, strName, strDescription,hazardousFlag,fltWeight, fltVolume, dtDelivery = IO.add_new_order(intOrderId)
                
        except KeyboardInterrupt:
            print('\nThe user has caused a keyboard interruption\nThe program will now close!')
            time.sleep(2)

           
if __name__ == '__main__':
    Main.main()