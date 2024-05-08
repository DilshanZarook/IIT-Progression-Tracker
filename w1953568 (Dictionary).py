# I declare that my work contains no examples of misconduct, such as plagiarism, or
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20220088
# uow ID : w1953568 
# Date: 12/12/2022

# variable declarations

print("             ------Entire programme with dictionary------\n")

number_credit_pass = ''
number_defer = ''
number_fail = ''
total_credits = ''
progress = 0
progress_list = []
trailer = 0
trailer_list = []
retriever = 0
retriever_list = []
excluded = 0
excluded_list = []
outcome = 0
input_validated = True
staff_input_validated = True
student_id_validated = True
this_dictionary = {}
student_id_list = []


def check_out_of_range(input_value):
    '''function to check the input is out of range'''
    if input_value in range(0, 121, 20):
        return True
    else:
        print("Out of range.\n ")
        return False


def preview_choice():
    ''' function to preview the choice'''

    print("|--------------------------------------------------------|")
    print("|             Enter the number according to              |")
    print("|                    your preference                     |")
    print("|--------------------------------------------------------|")
    print("| 1 - Horizontal histogram                               |")
    print("| 2 - Preview the input data with the progression outcome|")
    print("| 3 - print all in Dictionary                            |")
    print("| 4 - Exit from the program                              |")
    print("|--------------------------------------------------------|")


def histogram_horizontal(progress, trailer, retriever, excluded):
    '''function to create the horizontol histogram'''

    symbol = "*"
    outcome = progress + trailer + retriever + excluded
    print("\nProgress                ", progress, ":", progress * symbol, end='')
    print("\nProgress(Module Trailer)", trailer, ":", trailer * symbol, end='')
    print("\nModule Retriever        ", retriever, ":", retriever * symbol, end='')
    print("\nExcluded                ", excluded, ":", excluded * symbol, end='')
    print("\n")
    print(outcome, "outcomes in total.\n")

def print_dictionary():
    for key in this_dictionary:
        print(key, " : ", *this_dictionary[key], sep='')
        print()

def print_list_outcome(progress_list, trailer_list, retriever_list, excluded_list):
    '''print lists outcome'''

    if len(progress_list) >= 1:
        print("Progress                 -", progress_list)
    if len(trailer_list) >= 1:
        print("Progress(module trailer) -", trailer_list)
    if len(retriever_list) >= 1:
        print("Module retriever         -", retriever_list)
    if len(excluded_list) >= 1:
        print("Excluded                 -", excluded_list)


while input_validated:

    input_version = input("Are you a Student or Staff? ")
    input_version.lower()

    # run the programme if user is a student

    if input_version == "student" or input_version == "s":

        print("..........STUDENT VERSION..........")

        is_validated = True
        while True:
            try:
                number_credit_pass = int(input("Please enter your credits at pass: "))
                is_validated = check_out_of_range(number_credit_pass)
                if not is_validated:
                    continue

                number_defer = int(input("Please enter your credit at defer: "))
                is_validated = check_out_of_range(number_defer)
                if not is_validated:
                    continue

                number_fail = int(input("Please enter your credit at fail: "))
                is_validated = check_out_of_range(number_fail)
                if not is_validated:
                    continue

                total_credits = number_credit_pass + number_defer + number_fail

                if total_credits != 120:
                    print("Incorrect Total \n")

                elif number_credit_pass == 120:
                    print("Progress \n")

                    break
                elif number_credit_pass == 100:
                    print("Progress (module trailer) \n")
                    break

                elif number_fail <= 60:
                    print("Do not progress- module retriever \n")
                    break

                elif number_fail >= 80:
                    print("Exclude \n")
                    break

            except ValueError:
                print("Integer required\n")

        print("Good Bye\nThank you for using this!")
        input_validated = False

    # run the programme if user is a staff member

    elif input_version == "staff" or input_version == "staf":

        print("..........STAFF VERSION..........")

        is_validated = True
        is_continue = True

        while is_continue:

            while student_id_validated:
                
                student_id = input("Enter student ID :").lower()
                
                if len(student_id) == 8 and student_id[0] == "w":
                    if student_id not in student_id_list:
                        student_id_list.append(student_id)
                    else:
                        print("This student ID has already given")
                        break
                else:
                    print("invalid student ID")
                    break
                
                while True:

                    staff_user_input_list = []

                    try:
                        number_credit_pass = int(input("Please enter your credits at pass: "))
                        staff_user_input_list.append(number_credit_pass)
                        is_validated = check_out_of_range(number_credit_pass)
                        if not is_validated:
                            continue

                        number_defer = int(input("Please enter your credit at defer: "))
                        staff_user_input_list.append(number_defer)
                        is_validated = check_out_of_range(number_defer)
                        if not is_validated:
                            continue

                        number_fail = int(input("Please enter your credit at fail: "))
                        staff_user_input_list.append(number_fail)
                        is_validated = check_out_of_range(number_fail)
                        if not is_validated:
                            continue

                        total_credits = number_credit_pass + number_defer + number_fail

                        if total_credits != 120:
                            print("Incorrect Total \n")

                        elif number_credit_pass == 120:
                            print("Progress \n")
                            progress_list.append(staff_user_input_list)
                            this_dictionary[student_id] = "progress-", ', '.join(str(item) for item in staff_user_input_list)
                            progress += 1

                            break
                        elif number_credit_pass == 100:
                            print("Progress (module trailer) \n")
                            trailer_list.append(staff_user_input_list)
                            this_dictionary[student_id] = "Progress (module trailer)-", ', '.join(str(item) for item in staff_user_input_list)
                            trailer += 1

                            break
                        elif number_fail <= 60:
                            print("Do not progress - module retriever \n")
                            retriever_list.append(staff_user_input_list)
                            this_dictionary[student_id] = "Do not progress - (module retriever)-", ', '.join(
                                str(item) for item in staff_user_input_list)

                            retriever += 1
                            break
                        elif number_fail >= 80:
                            print("Exclude \n")
                            excluded_list.append(staff_user_input_list)
                            this_dictionary[student_id] = "Exclude-", ', '.join(str(item) for item in staff_user_input_list)

                            excluded += 1
                            break

                    except ValueError:
                        print("Integer required\n")
                        # break
                while staff_input_validated:
                    try:
                        user_input = input(
                            "Would you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view "
                            "results:")
                        user_input = user_input.lower()

                        if user_input == "y" or user_input == "yes" or user_input == "yeah":
                            is_continue = True
                            break

                        elif user_input == "q" or user_input == "quit" or user_input == "end":
                            is_continue = False
                            # continue

                            preview_choice()
                            print()
                            preview = int(input("Enter the number according to your preference: "))
                            if preview == 4:
                                print("Good Bye\nThank you for using this!")
                                staff_input_validated = False
                                input_validated = False
                                student_id_validated = False
                                
                            
                            elif preview == 1:
                                histogram_horizontal(progress, trailer, retriever, excluded)
                            elif preview == 2:
                                print_list_outcome(progress_list, trailer_list, retriever_list, excluded_list)
                            elif preview == 3:
                                print_dictionary()

                        else:
                            print("user input is wrong\n")

                    except ValueError:
                        print("wrong input")

    else:
        print("wrong input")
        input_validated = True

#REFERENCES :
#https://www.w3schools.com/python/python_dictionaries.asp
#https://www.geeksforgeeks.org/python-string-join-method/
#https://blog.finxter.com/how-to-convert-an-integer-list-to-a-string-list-in-python/


