# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# ------------------------------------------#
# Title: Test_Booking_Quote_System.py
# Desc: Assignment Booking Quote System - Create the tests harness for the Booking Quote application
# Change Log: (Who, When, What)
# AHernandez, 2021-June-08, Created File
# AHernandez, 2021-June-14, Added more test cases to Test Harness
# ------------------------------------------#
import Booking_Quote_System
from io import StringIO


def test_process_new_order():
    dictRow = {5: ['Andrew', False, 'Test', False, 3.0, 6.0, '2021-09-19']}
    expected = dictRow
    actual = Booking_Quote_System.DataProcessor.process_new_order(5,False,'Andrew', 'Test', False, 3.0, 6.0, '2021-09-19')
    assert actual == expected

def test_process_new_order2():
    dictRow = {5: ['John', True, 'Test', False, 3.0, 6.0, '2021-09-29']}
    expected = dictRow
    actual = Booking_Quote_System.DataProcessor.process_new_order(5,True,'John', 'Test', False, 3.0, 6.0, '2021-09-29')
    assert actual == expected
    
def test_process_new_order3():
    dictRow = {5: ['Andrew', False, 'Test', False, 3.0, 6.0, '2021-09-19']}
    expected = dictRow
    actual = Booking_Quote_System.DataProcessor.process_new_order(5,True,'Andrew', 'Test', False, 3.0, 6.0, '2021-09-19')
    assert actual != expected

def test_order_cost():
    dictRow = {5: ['John', True, 'Test', False, 3.0, 6.0, '2021-09-29']}
    newDictRow = {5: ['John', True, 'Test', False, 3.0, 6.0, '2021-09-29','N/A',25,30]}
    expected = newDictRow
    actual = Booking_Quote_System.DataProcessor.order_cost(dictRow, 5, True, False)
    assert actual == expected
    
def test_order_cost2():
    dictRow = {6: ['John', False, 'Test', False, 3.0, 6.0, '2021-09-29']}
    newDictRow = {6: ['John', False, 'Test', False, 3.0, 6.0, '2021-09-29',120,25,30]}
    expected = newDictRow
    actual = Booking_Quote_System.DataProcessor.order_cost(dictRow, 6, False, False)
    assert actual == expected
    
def test_order_cost3():
    dictRow = {5: ['John', False, 'Test', False, 3.0, 6.0, '2021-09-29']}
    newDictRow = {6: ['John', False, 'Test', False, 3.0, 6.0, '2021-09-29',120,25,30]}
    expected = newDictRow
    actual = Booking_Quote_System.DataProcessor.order_cost(dictRow, 5, True, False)
    assert actual != expected

def test_export_to_text1(monkeypatch):
    file_status = StringIO('YES')
    monkeypatch.setattr('sys.stdin',file_status)
    assert Booking_Quote_System.IO.export_to_text() == 'yes' 
    
def test_export_to_text2(monkeypatch):
    file_status = StringIO('NO')
    monkeypatch.setattr('sys.stdin',file_status)
    assert Booking_Quote_System.IO.export_to_text() == 'no'  
    
def test_export_to_text3(monkeypatch):
    file_status = StringIO('NO')
    monkeypatch.setattr('sys.stdin',file_status)
    assert Booking_Quote_System.IO.export_to_text() != 'yes' 
    
def test_get_bools():
    dictRow = {5: ['John', False, 'Test', False, 3.0, 6.0, '2021-09-29']}
    bools = (False, False)
    expected = bools
    assert Booking_Quote_System.DataProcessor.get_bools(dictRow, 5) == expected
    
def test_get_bools2():
    dictRow = {5: ['John', True, 'Test', False, 3.0, 6.0, '2021-09-29']}
    bools = (False, True)
    expected = bools
    assert Booking_Quote_System.DataProcessor.get_bools(dictRow, 5) == expected    
    
def test_get_bools3():
    dictRow = {5: ['John', True, 'Test', True, 3.0, 6.0, '2021-09-29']}
    bools = (False, False)
    expected = bools
    assert Booking_Quote_System.DataProcessor.get_bools(dictRow, 5) != expected       