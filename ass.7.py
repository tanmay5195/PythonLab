def calculate_calories(c, f, p):
    return c*4 + f*9 + p*4

c = int(input("Carbs: "))
f = int(input("Fats: "))
p = int(input("Proteins: "))

print("Calories:", calculate_calories(c, f, p))