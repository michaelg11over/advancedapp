# Program Name: Assignment1.py
# Course: IT3883/Section  1
# Student Name:Sidney Michael Glover
# Assignment Number: Lab1
# Due Date: 01/24/2026
# Purpose: This program implements a text-based menu system that allows
#          users to append data to a buffer, clear the buffer, display
#          current buffer contents, or exit the program.
# List Specific resources used to complete the assignment:



def print_menu():

    #Displays the menu and prints out all available choices that are given in the program

    print("\n" + "="*50)
    print("Menu")
    print("="*50)
    print("Option 1: Append data to input")
    print("Option 2: Clear input")
    print("Option 3: Display input")
    print("Option 4: Quit")
    print("="*50)

def data(buffer):

    #asks user data to input into the existing buffer

    user_input = input("Enter data to append: ")

    if buffer:
        buffer += " " + user_input
    else:
        buffer = user_input
    print (f"Success!")
    return buffer

def clear():
 
    #Clears all the data that is from the input buffer
    
    print("Cleared")
    return ""

def display(buffer):


    print("\n" + "="*50)
    print("Current: ")
    print("-"*50)
    if buffer:
        print(buffer)
    else:
        print("(Empty)")
    print("-"*50)

def main():

    input_data = ""

    while True:
            
            print_menu()

            choice = input("Enter choice 1-4: ")

            if choice == "1":

                input_data = data(input_data)

            elif choice == "2":

                input_data = clear()

            elif choice == "3":

                display(input_data)

            elif choice == "4":

                print ("\n Thank you. Goodbye!")
                break

if __name__ == "__main__":
    main()
    
