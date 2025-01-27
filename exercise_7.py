# Question_1. Find BMI with range of under weight & overweight.

height=float(input('Enter your height in meter:'))
weight=int(input('Enter your weight in kg:'))
b_m_i=int(weight/(height*height))
if b_m_i<18.5:
    print(f'Your BMI  is{b_m_i} and your are under weight.')
elif b_m_i<25:
    print(f'Your BMI is  {b_m_i} and you have a normal weight.')
elif b_m_i<30:
    print(f'Your BMI is {b_m_i} and you are over weight.')
elif b_m_i<35:
    print(f'Your BMI is {b_m_i} and you are obese.')
else:
    print(f'your BMI is {b_m_i} and you are clinically obese.')