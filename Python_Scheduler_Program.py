import datetime
import sys

# create a list for the appointments to be stored in 
appointments_list = []


def welcome ():
    print ('Welcome to your scheduling Python program.')

def menu ():
    print ('''Here are your options:
    1) Enter Appointment
    2) Modify Schedule
    3) View Scedule
    4) Exit Program''')

def user_choice():
    # Display the welcome message
    while True:
        # Display the menu options
        menu()
        # Get the user's choice
        choice = input("Enter your choice (1-4): ")
        # Handle the user's choice
        if choice == "1":
            enter_appointment()
        elif choice == "2":
            modify_schedule()
        elif choice == "3":
            view_schedule(appointments_list)
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

# This function validates the user input. It takes a user input as a parameter and ensures that it meets the required format and constraints 
def valid_input(input_str):
    try:
        datetime.datetime.strptime(input_str.split(' - ')[0], '%Y/%m/%d %H:%M')
#        datetime.datetime.strptime(input_str.split(' - ')[1], '%Y/%m/%d %H:%M')
        return True
    except ValueError:
        return False

def enter_appointment():
    while True:
        # prompt the user to enter appointment details
        name = input("Please enter the name of the appointment: ")
        appointment_input = input("Please enter the appointment details in the following format: YYYY/MM/DD HH:MM - YYYY/MM/DD HH:MM")

        # validate the user input
        if not valid_input(appointment_input):
            print("Invalid input. Please try again.")
            continue
        else:
            # parse the input string into datetime objects
            start_str, end_str = appointment_input.split(' - ')
            start_time = datetime.datetime.strptime(start_str, '%Y/%m/%d %H:%M')
            end_time = datetime.datetime.strptime(end_str, '%Y/%m/%d %H:%M')

            # check if the start time is before the end time
            if start_time >= end_time:
                print("End time must be after start time. Please try again.")
                continue
            else:
                # add the appointment to the schedule
                appointments_list.append({'name': name, "start_time": start_time, "end_time": end_time})
                print(f'Appointment: {name} is scheduled for: {start_time} - {end_time}')
                break
    
def modify_schedule ():
    # display options for modifying appointment 
    print('You chose to modify your schedule.')
    # ask the user what appointment they want to modify 
    name = input("Please enter the name of the appointment you want to modify: ")
        
    # search for the appointment in the list of appointments
    found = False
    for appointment in appointments_list:
        if appointment['name'] == name:
            found = True
            break
    # handle case where appointment not found
    if not found:
        print("Appointment not found.")
        return
        
    # ask how they want to modify the appointment
    print('''How would you like to modify your scedule?
        1. Delete the appointment
        2. Change the appointment time''')
    choice = input("Enter your choice (1-2): ")

    if choice == '1':
        # delete appointment
        appointments_list.remove(name)
        print(f"{name} appointment has been deleted from your schedule.")
            
    elif choice == '2':
        # ask user if they want to change both start and end time or just one
        time_change = input("Do you want to change both start and end time (b) or just one (o)? ")
        if time_change.lower() == 'b':
            # ask user what they would like to change their start time to
            new_start_time = input("What time would you like your appointment to start? (formatted YYYY/MM/DD HH:MM) ")
            # validate the user input and update the preferences dictionary
            if  not valid_input(new_start_time):
                print("Invalid input. Start time not updated.")
                return
            new_start_time = datetime.datetime.strptime(new_start_time, '%Y/%m/%d %H:%M')
            appointments_list[name]['start_time'] = new_start_time
            # ask user what they would like to change their end time to
            new_end_time = input("What time would you like your appointment to end? (formatted YYYY/MM/DD HH:MM) ")
            # validate the user input and update the preferences dictionary
            if not valid_input(new_end_time):
                print("Invalid input. End time not updated.")
                return
            new_end_time = datetime.datetime.strptime(new_end_time, '%Y/%m/%d %H:%M')
            appointments_list[name]['end_time'] = new_end_time
            print (f"Your new start time for {name} is {new_start_time} and your new end time is {new_end_time}.")
        if time_change.lower() == 'o':
            # ask user which time they want to change
            time_change = input("Do you want to change your start time (s) or end time (e)? ")
            if time_change.lower() == 's':
                # ask user what they would like to change their start time to
                new_start_time = input("What time would you like your appointment to start? (formatted YYYY/MM/DD HH:MM) ")
                # validate the user input and update the preferences dictionary
                if not valid_input(new_start_time):
                    print("Invalid input. Start time not updated.")
                    return
                new_start_time = datetime.datetime.strptime(new_start_time, '%Y/%m/%d %H:%M')
                appointments_list[name]['start_time'] = new_start_time
                print (f"Your new start time for {name} is {new_start_time}.")

            elif time_change.lower() == 'e':
                 # ask user what they would like to change their end time to
                new_end_time = input("What time would you like your appoitnment to end? (e.g. 5:00 PM) ")
                # validate the user input and update the preferences dictionary
                if not valid_input(new_end_time):
                    print("Invalid input. End time not updated.")
                    return
                new_end_time = datetime.datetime.strptime(new_end_time, '%Y/%m/%d %H:%M')
                appointments_list[name]['end_time'] = new_end_time
                print (f"Your new end time for {name} is {new_end_time}.")

def view_schedule (appointments):
    print("Your Appointments\tStart Time\tEnd Time")
    print("-------------------------------------------------")
    for appointment in appointments:
        print(f"{appointment['name']}\t\t{appointment['start_time']}\t\t{appointment['end_time']}")

# Define a function to save the schedule to a file
def save_file(filename, data):
    f = open(filename, 'w')
    f.write('Daily Schedule')
    f.write("-------------------------------------------------")
    for item in data:
        f.write(f"{item}\n")
    print(f"Your appointment data has been saved to {filename}")

# 
def load_file(filename):
    data = []
    try:
        file = open(filename, 'r')
        for line in file:
            data.append(line.strip())
        print(f"Data loaded from {filename}")
        return data
    except FileNotFoundError:
        print(f"File {filename} not found.")

def main ():
    file_name = 'schedule.txt'
    load_file (file_name)
    welcome()
    user_choice()
    save_file (file_name, appointments_list)
    

main ()