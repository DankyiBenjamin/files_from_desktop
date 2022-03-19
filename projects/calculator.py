first_number = int(input("please type your first  number: "))
second_number = int(input("please type your second  number: "))
operators = input("please what operator are you using(+,-,*,/): ")


def solve():
    if operators == "addition" or  operators == "+":
        print(first_number + second_number)
    if operators == "subraction" or operators == "-":
        print(first_number - second_number)
    if operators == "divide by" or operators == "/":
        try: print(first_number // second_number)
        except ZeroDivisionError:
            print("you cannot divide with zero")
    if operators == "multiplication" or operators == "*":
        print(first_number * second_number)

solve()
