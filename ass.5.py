n = int(input("Enter number of students: "))
total = 0

for i in range(n):
    sum = 0
    print("Student", i + 1)

    for j in range(5):
        marks = float(input("Enter marks: "))
        sum += marks

    avg = sum / 5
    total += sum
    print("Average =", avg)

print("Class average =", total / (n * 5))