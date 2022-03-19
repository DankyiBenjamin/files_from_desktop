first_number = int(input("pleasetype your first number "))
second_number = int(input("please type your seond number "))

RESULT = first_number* second_number



def logic_calculation():
    if RESULT % 5 == 0:
        print("ben")
    else:
        print("not him")


logic_calculation()