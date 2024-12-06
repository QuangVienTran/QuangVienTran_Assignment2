"""
File Name: hotel_management.py
Student's name: Quang Vien Tran
Description: A simple hotel management system
Date: 2024-12-06
"""

#Task 1

#Part A Application Menu

import os
from datetime import datetime

#List to store rooms and their status
rooms= []
allocated_rooms= []

#Define the name of the room allocation file and backupfile with timestamp
roomfile="LHMS_764708339.txt"
backupfile="LHMS_764708339_backup{}.txt". format(datetime.now().strftime("%Y%m%d_%H%M%S"))

"""
Function display menu options to show users to know the functions of Hotel Management app including Add room, Delete room, Display room detail, room booking, display room booking detail, etc...
"""

#Function to display menu options
def display_menu():
    while True:
        print("--- WELCOME TO HOTEL MANAGEMENT SYSTEM ---")
        print("Please choose one of all the following option")
        print("1. Add Room")
        print("2. Delete Room")
        print("3. Display Rooms Details")
        print("4. Allocate Rooms")
        print("5. Display Room Allocation Details")
        print("6. Billing & De-Allocation")
        print("7. Save Room Allocation to a File")
        print("8. Show Room Allocation from a File")
        print("9. Backup Room Allocation File")
        print("0. Exit Application")
        print("-----------#####---------------")
        choice = input("HELLO! What can I help you? Please enter your choice: ")
        if choice == "1":
            add_room()
        elif choice == "2":
            delete_room()
        elif choice == "3":
            display_room_details()
        elif choice == "4":
            allocate_room()
        elif choice == "5":
            display_room_allocation()
        elif choice == "6":
            billing_and_deallocation()
        elif choice == "7":
            save_room_allocation()
        elif choice == "8":
            show_room_allocation()
        elif choice == "9":
            backup_file()
        elif choice == "0":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")
#Function to add rooms to the list
def add_room():
    room_type = input(" Please enter room type: ")
    room_number = input("Please nter room number: ")
    room_price = input("Please enter room price: ")
    rooms.append({"room_type": room_type, "room_number": room_number, "room_price": room_price})
    print(f"Room {room_number} of type {room_type} added successfully with price {room_price}.")

# Function to delete rooms from the list
def delete_room():
    room_number = input("Enter room number to delete: ")
    room_found = False
    for room in rooms:
        if room["room_number"] == room_number:
            rooms.remove(room)
            print(f"Room {room_number} deleted successfully.")
            room_found = True
            break
    if not room_found:
        print(f"Room {room_number} not found.")

# Function to display room details
def display_room_details():
    if rooms:
        print("\nRoom Details:")
        for room in rooms:
            print(f"Room Number: {room['room_number']}, Type: {room['room_type']}, Price: {room['room_price']}")
    else:
        print("No rooms available.")

# Function to allocate a room to a customer
def allocate_room():
    room_number = input("Please nter room number to allocate: ")
    for room in rooms:
        if room["room_number"] == room_number:
            allocated_rooms.append(room)
            rooms.remove(room)
            print(f"Room {room_number} allocated successfully. Thank yo")
            return
    print(f"Room {room_number} not available.")

# Function to display room allocation details
def display_room_allocation():
    if allocated_rooms:
        print("\nAllocated Rooms:")
        for room in allocated_rooms:
            print(f"Room Number: {room['room_number']}, Type: {room['room_type']}, Price: {room['room_price']}")
    else:
        print("No rooms allocated.")

# Function to handle billing and de-allocation
def billing_and_deallocation():
    room_number = input("Enter room number for billing and deallocation: ")
    for room in allocated_rooms:
        if room["room_number"] == room_number:
            print(f"Room {room_number} billed successfully. Price: {room['room_price']}")
            allocated_rooms.remove(room)
            rooms.append(room)
            print(f"Room {room_number} de-allocated successfully.")
            return
    print(f"Room {room_number} not allocated.")

# Function to save room allocation to a file
def save_room_allocation():
    try:
        with open("LHMS_764708339.txt", "a") as file:
            for room in allocated_rooms:
                file.write(f"Room Number: {room['room_number']}, Type: {room['room_type']}, Price: {room['room_price']}\n")
        print("Room allocation saved to file.")
    except IOError:
        print("Error writing to file.")

# Function to show room allocation from file
def show_room_allocation():
    try:
        with open("LHMS_764708339.txt", "r") as file:
            content = file.read()
            print("\nRoom Allocations from File:")
            print(content)
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error reading from file.")

# Function to backup the file
def backup_file():
    try:
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = f"LHMS_764708339_Backup_{current_time}.txt"
        with open("LHMS_764708339.txt", "r") as source_file:
            content = source_file.read()
        with open(backup_filename, "w") as backup_file:
            backup_file.write(content)
        with open("LHMS_764708339.txt", "w") as file:
            file.truncate(0)
        print(f"Backup saved to {backup_filename} and original file cleared.")
    except IOError:
        print("Error handling the backup file.")
#Function to exit the application
def exit_the_app():
    print("Exit the app!")
    exit()
display_menu()
