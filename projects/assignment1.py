body_weight = float(input("please type in your body weight(kg): "))
height = float(input("please type in your height(m): "))


body_mass_index = round((body_weight / height**2))

 


if body_mass_index >= 35:
    print(f"Your BMI is {body_mass_index}kg/m2,you are clinically obese")
elif body_mass_index > 30  < 35 :
    print(f"Your BMI is {body_mass_index}kg/m2,you are obese")
elif body_mass_index > 25 < 30 :
    print(f"Your BMI is {body_mass_index}kg/m2,you are slightly obese")
elif body_mass_index > 18.5 < 25 :
      print(f"Your BMI is {body_mass_index}kg/m2,you are normal weight")
else :
      print(f"Your BMI is {body_mass_index}kg/m2,you are underweight")