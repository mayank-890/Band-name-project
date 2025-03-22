height = 1.65 #kg
weight = 84 #metre



bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif 19 <= bmi < 24.9:
    category = "Normalweight"
elif 25 <= bmi <29.9:
    category = "Overweight"
else:
    category = "Obesity"
    
print(bmi)
print(category)