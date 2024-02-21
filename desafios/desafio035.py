r1 = int(input("Enter the first side: "))
r2 = int(input("Enter the second side: "))
r3 = int(input("Enter the third side: "))

condition1 = (r2 - r3) < r1 < r2 + r3
condition2 = (r3 - r1) < r2 < r3 + r1
condition3 = (r1 - r2) < r3 < r1 + r2

if condition1 and condition2 and condition3:
    print(f"{r1}, {r2} and {r3} can make a triangle.")
else:
    print(f"{r1}, {r2} and {r3} cannot make a triangle.")
