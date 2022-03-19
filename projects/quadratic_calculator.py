# creating a program that takes an equation and find the roots of it 



print("Quadratic calculator, takes the form ax^2+bx+c = 0")
A = int(input("please type in the value for a "))
B = int(input("please input the value for b "))
C = int(input("please type the value for c "))
m = B*B

real_root = m-(4*(A*C))


# print(real_root,y)
# function checking for real root
def check_for_real_root():
    if real_root > 0:
        print("this equation has a real root {real_root} ")
        answer1 = (-B + (real_root**0.5))/2*A
        answer2 = (-B - (real_root**0.5))/2*A
        print(answer1 , answer2)
    else:
        print(f"there is no real root {real_root} ")
        answer3 = (-B + (real_root**0.5))/2*A
        comp_answer3 = complex(round(answer3.real),round(answer3.imag))
        answer4 = (-B - (real_root**0.5))/2*A
        comp_answer4 = complex(round(answer4.real),round(answer4.imag))
        print(comp_answer3, comp_answer4)


check_for_real_root()


# # function for calculating the quadratic equation
# def calculate_quadratic():
#   pass
  
# # calculating complex root
# def complex_round():
#    pass 




