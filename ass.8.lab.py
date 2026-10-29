
def calculate_area(shape, *args):
    if shape == "circle":
        radius = args[0]
        c_area=3.14 * radius ** 2
        print(f"Area of the circle is: {c_area}")
    elif shape == "rectangle":
        length, width = args
        r_area = length * width
        print(f"Area of the rectangle is: {r_area}")
    elif shape == "triangle":
        base, height = args
        t_area = 0.5 * base * height
        print(f"Area of the triangle is: {t_area}")
    else:
        raise ValueError("Unsupported shape type")



print("Choose a shape:")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = input("Enter your choice (1-3): ")

if choice == "1":
    radius = float(input("Enter the circle's radius: "))
    calculate_area("circle", radius)
elif choice == "2":
    length = float(input("Enter the rectangle's length: "))
    width = float(input("Enter the rectangle's width: "))
    calculate_area("rectangle", length, width)
elif choice == "3":
    base = float(input("Enter the triangle's base: "))
    height = float(input("Enter the triangle's height: "))
    calculate_area("triangle", base, height)
else:
    print("Invalid choice. Please run the program again and choose 1, 2, or 3.")
