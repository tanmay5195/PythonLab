def weight(mass, gravity):
    return mass * gravity

EARTH = 9.8
MOON = 1.62

mass = float(input("Enter mass in kg: "))

print("Earth weight:", weight(mass, EARTH))
print("Moon weight:", weight(mass, MOON))