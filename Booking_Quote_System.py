# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# ------------------------------------------#
# Title: Booking_Quote_System.py
# Desc: Assignment Booking Quote System - Create the Booking Quote application
# Change Log: (Who, When, What)
# AHernandez, 2021-June-08, Created File for Booking Quote application and skeletal structure 
# AHernandez, 2021-June-10, Created menu structure and IO class 
# AHernandez, 2021-June-11, Added Exception handling to new order
# AHernandez, 2021-June-12, Worked on logic for adding new package, built Order class
# ------------------------------------------#
import time
from datetime import datetime, timedelta 
strChoice = '' 
lstTbl = []
dictRow = {}
menuOptions = '\nWelcome to the Booking System.  Please choose from one of the following:\n\t[P] Show Current Rates\n\t[N] Create a New Order\n\t[X] Quit'
strMenuOption = 'n','p','x'

# -- DataProcessor -- # 
class DataProcessor:
    def process_new_order(intOrderId, deliveryStatus, strName, strDescription,hazardousFlag,fltWeight, fltVolume, dtDelivery):
        new_order = Order(intOrderId, deliveryStatus, strName, strDescription,hazardousFlag,fltWeight, fltVolume, dtDelivery)
        lstTbl = new_order.customerName,new_order.status , new_order.packageDescription, new_order.hazardousFlag, new_order.weight, new_order.volume, new_order.deliveryDate
        dictRow[new_order.orderId] = list(lstTbl)
        print(dictRow)
        return dictRow
    
    def process_shipping_options(dictRow, intOrderId):
        pass
 
class Order:
    def __init__(self, orderId, status, customerName, packageDescription, hazardousFlag, weight, volume, deliveryDate):
        self.orderId = orderId
        self.status = status
        self.customerName = customerName
        self.packageDescription = packageDescription
        self.hazardousFlag = hazardousFlag
        self.weight = weight
        self.volume = volume
        self.deliveryDate = deliveryDate

    
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
        while True:
            try:
                urgent = input("Do you need urgent delivery (Dilivered in less than 3 Business days): ").strip().lower()
                if urgent.isalpha():
                    if urgent in ("yes", "no"):
                        if urgent == 'yes':
                            deliveryStatus = True
                        else:
                            deliveryStatus = False
                        break
                    else:
                        print("You must enter Yes or No")
                else:
                    raise
            except:
                print("Please enter only Alpha characters")
                
        customerName = input("Please enter the customers Name: ")
        packageDescription = input("Please enter the package description: ")
        hazFlag = False
        hazardousFlag = input("Does the package contain any hazardous material? ").strip().lower()
        if hazardousFlag == 'yes':
            hazFlag = True
            cont = input("Warining hazardous material is not permitted for Air Delivery! Would you like to continue: ").strip().lower()
            if cont == 'yes':
                hazFlag = True
            else:
                hazFlag = False
                print("hazardous material has been removed from the package!")
                
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
            if volume <= 125.0:
                break
            else:
                print("Volume of package must be less than 125m³")
                
        while True:
            if deliveryStatus:
                deliveryDate = (datetime.now() + timedelta(days = 3)).strftime('%Y-%m-%d')
                break
            else:
                deliveryDate = input('Enter a delivery date(YYYY-MM-DD): ').strip()
                if datetime.strptime(deliveryDate, '%Y-%m-%d') >= datetime.now():
                    try:
                        datetime.strptime(deliveryDate, '%Y-%m-%d')
                        break
                    except ValueError:
                        print("Incorrect Start Date format, It should be YYYY-MM-DD") 
                else:
                    print("Delivery Date cannot be in the past")
        
                
        return orderId, deliveryStatus, customerName, packageDescription, hazFlag, weight, volume, deliveryDate       

                
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
                    intOrderId, deliveryStatus, strName, strDescription,hazardousFlag,fltWeight, fltVolume, dtDelivery = IO.add_new_order(intOrderId)
                    dictRow = DataProcessor.process_new_order(intOrderId, deliveryStatus, strName, strDescription,hazardousFlag,fltWeight, fltVolume, dtDelivery)
                    DataProcessor.process_shipping_options(dictRow, intOrderId)
        except KeyboardInterrupt:
            print('\nThe user has caused a keyboard interruption\nThe program will now close!')
            time.sleep(2)

           
if __name__ == '__main__':
    Main.main()