#Convert hourst to days
from ast import Return
from cgi import print_arguments

#test_commentsaaaaaasssss
calculation_of_units = 24
num_of_unit = "hours"

def days_to_units(num_of_days):
        return f"{num_of_days} days are {num_of_days * calculation_of_units} {num_of_unit}"

def validate_and_execute():
    try: 
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you enetered a 0, enter positive number")
        else:
            print("you entered negative number, please enter positive number")
            
    except ValueError :
        print("your input in not valid input")
    
user_input = input("Enter number of days to convert it to hours\n")
validate_and_execute()

