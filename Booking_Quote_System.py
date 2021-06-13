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
# AHernandez, 2021-June-12, Worked on print functionality, Cost logic and Cost class
# ------------------------------------------#
import time
from datetime import datetime, timedelta 
import pandas as pd
import pathlib
import csv
from prettytable import PrettyTable

strChoice = '' 
lstTbl = []
 

menuOptions = '\nWelcome to the Booking System.  Please choose from one of the following:\n\t[P] Show Current Rates\n\t[N] Create a New Order\n\t[S] Show Order History\n\t[X] Quit'
strMenuOption = 'n','p','x','s'
orderHistoryFile = 'OrderHistory.csv'
quoteFile = 'OrderQuotes.csv'
fieldnames = ['OrderId','CustomerName', 'UrgentDelivery', 'Description', 'Hazardous', 'WT', 'Vol.', 'DeliveryDate', 'Air Cost($)', 'Truck Cost($)', 'Sea Costs($)']

# -- DataProcessor -- # 
class DataProcessor:
    def process_new_order(intOrderId, deliveryStatus, strName, strDescription,hazardousFlag,fltWeight, fltVolume, dtDelivery):
        new_order = Order(intOrderId, deliveryStatus, strName, strDescription,hazardousFlag,fltWeight, fltVolume, dtDelivery) 
        lstTbl = new_order.customerName,new_order.status , new_order.packageDescription, new_order.hazardousFlag, new_order.weight, new_order.volume, new_order.deliveryDate
        dictRow[new_order.orderId] = list(lstTbl)
        return dictRow
    
    def order_cost(dictRow, OrderId, hazardous, urgent):
        airVals = dictRow.get(OrderId)
        weightCost = airVals[4] * 10
        volumeCost = airVals[5] * 20
        deliveryCosts = DeliveryCost()
        deliveryCosts.airCost
        deliveryCosts.truckCost
        deliveryCosts.oceanCost
        if weightCost > volumeCost:
            deliveryCosts.airCost = weightCost
        else:
            deliveryCosts.airCost = volumeCost
            
        if hazardous == True:
            deliveryCosts.airCost = 'N/A'

        else:
            deliveryCosts.airCost
            
        if urgent == True:
            deliveryCosts.truckCost = 45
        else:
            deliveryCosts.truckCost = 25
        deliveryCosts.oceanCost = 30    
        dictRow[intOrderId].extend([deliveryCosts.airCost, deliveryCosts.truckCost, deliveryCosts.oceanCost])
        return dictRow
    
    def order_history(dictRow):
        try:
            for key, val in dictRow.items():
                table = PrettyTable(fieldnames)
                for key, val in dictRow.items():
                    table.add_row([key, *val])
            return table 
        except UnboundLocalError:
            print('The table is empty.  There is nothing to print.') 
            
    def get_bools(dictRow, OrderId):
        orderVals = dictRow.get(OrderId)
        isHazardous = orderVals[3]
        isUrgent = orderVals[1]
        return isHazardous, isUrgent 

    def find_current_order(dictRow, orderId):    
        for key, val in dictRow.items():
            table = PrettyTable(fieldnames)
        for key, val in dictRow.items():
            if key == intOrderId:
                table.add_row([key, *val])
        return table    
# -- Order -- #  
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
        
# -- Cost -- #  
class DeliveryCost:
    def __init__(self, airCost='', truckCost='', oceanCost=''):
        self.airCost = airCost
        self.truckCost = truckCost
        self.oceanCost = oceanCost

        
# -- FILE PROCESSING -- #         
class FileProcessor:
    def read_file(file_name, dictRow,lstTbl):
            dictRow.clear()
            try:
                with open(file_name, mode='r') as file:
                    next(file)
                    for line in csv.reader(file):
                        tup = line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10]
                        lstTbl = list(tup)
                        dictRow[line[0]] = lstTbl
                print(f'Loading {file_name}: \n')
            except (FileNotFoundError,OSError):
                print(f'There is no file named {file_name}.')
            return dictRow

    def write_file(file_name, dictRow):         
        try:
            (pd.DataFrame.from_dict(data=dictRow, orient='index')
             .to_csv(file_name, mode='w'))
            
        except ValueError:
            print('There are no Orders data')
        except PermissionError:
            print('The file is open, Please close and try again.')
        return None   
    
    def export_order_history(tblex, table):
        if tblex == 'yes':
            with open('OrderHistoryTable.txt', 'w') as table_export:
                table_export.write(str(table))
                
    def export_current_order(tblex, table, dictRow, orderId):
        for key, value in dictRow.items():
            if key == orderId:
                name = value[0]
        if tblex == 'yes':
            with open(f'{name}_Order.txt', 'w') as table_export:
                table_export.write(str(table))
# -- I/O -- #    
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
   
    def export_to_text():
        tblExport = input('Would you like to print this table? (Yes/No) ').strip().lower()
        return tblExport     
# -- PRESENTATION -- #

class Presentation:
    def file_state(strFileName):
        print('The File {} does not exists!'.format(strFileName))
        print('\n') 
        
    def show_order_history(table):
        if table != None:
            print (table)     
             
class Main:    
    def main():
        global intOrderId
        intOrderId = 1
        file =  pathlib.Path(orderHistoryFile)
        global dictRow  
        dictRow = {}
        try:
            while True:
                if file.exists():
                    dictRow = FileProcessor.read_file(orderHistoryFile, dictRow, lstTbl)
                else:
                    Presentation.file_state(orderHistoryFile)
                print(menuOptions)
                strChoice = IO.choice(strMenuOption)
                if strChoice == 'x':
                    break
                elif strChoice == 'p':
                    pass
                elif strChoice == 'n':
                    intOrderId, deliveryStatus, strName, strDescription,hazardousFlag,fltWeight, fltVolume, dtDelivery = IO.add_new_order(intOrderId)
                    dictRow = DataProcessor.process_new_order(intOrderId, deliveryStatus, strName, strDescription,hazardousFlag,fltWeight, fltVolume, dtDelivery)
                    hazardous, urgent = DataProcessor.get_bools(dictRow, intOrderId)
                    DataProcessor.order_cost(dictRow, intOrderId, hazardous, urgent) 
                    ptable = DataProcessor.find_current_order(dictRow, intOrderId)
                    FileProcessor.write_file(orderHistoryFile, dictRow)
                    Presentation.show_order_history(ptable)
                    if ptable != None:
                        tblExport = IO.export_to_text()
                        FileProcessor.export_current_order(tblExport,ptable, dictRow, intOrderId)
                        
                elif strChoice == 's':
                    ptable = DataProcessor.order_history(dictRow)
                    Presentation.show_order_history(ptable)
                    if ptable != None:
                        tblExport = IO.export_to_text()
                        FileProcessor.export_order_history(tblExport,ptable)
        except KeyboardInterrupt:
            print('\nThe user has caused a keyboard interruption\nThe program will now close!')
            time.sleep(2)

           
if __name__ == '__main__':
    Main.main()