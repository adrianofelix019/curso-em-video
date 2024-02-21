salary = float(input("Enter your salary: "))
increase = 0

if salary > 1250:
    increase = salary * 0.1
else:
    increase = salary * 0.15

print(f"The salary increase is U${increase} and the new salary is U${salary+increase}")
