# creating a program that takes an equation and find the roots of it 



print("Quadratic calculator, takes the form ax^2+bx+c = 0")
a = int(input("please type in the value for a "))
b= int(input("please input the value for b "))
c = int(input("please type the value for c "))
M = b*b

real_root = M-(4*(a*c))


# print(real_root,y)
# function checking for real root
def check_for_real_root():
    if real_root > 0:
        print("this equation has a real root {real_root} ")
        answer1 = (-b + (real_root**0.5))/2*a
        answer2 = (-b - (real_root**0.5))/2*a
        print(f"({answer1}, {answer2})")
    else:
        print(f"there is no real root {real_root} ")
        answer3 = (-b + (real_root**0.5))/2*a
        comp_answer3 = complex(round(answer3.real),round(answer3.imag))
        answer4 = (-b - (real_root**0.5))/2*a
        comp_answer4 = complex(round(answer4.real),round(answer4.imag))
        print(f"({comp_answer3}, {comp_answer4})")


check_for_real_root()


# # function for calculating the quadratic equation
# def calculate_quadratic():
#   pass
  
# # calculating complex root
# def complex_round():
#    pass 




