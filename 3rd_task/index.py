# Task 1: Calculate your age based on the current year and your birth year
def CalculateAge():
    current_year = 2024
    try:
        birth_year = int(input("Enter your birth year: "))
        if birth_year > current_year:
            print("Birth year cannot be in the future.")
        elif birth_year < 1900:
            print("Birth year seems too far in the past. Please enter a valid year.")
        else:
            age = current_year - birth_year
            print(f"You are {age} years old.")
    except ValueError:
        print("Please enter a valid year (numeric value).")


# Task 2: Write a program that calculates the area of a rectangle using length and width variables.
def CalculateAreaOfRectangle():
    try:
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))

        if length <= 0 or width <= 0:
            print("Length and width must be positive numbers.")
        else:
            area_of_rectangle = length * width
            print(f"The area of the rectangle is {area_of_rectangle} square units.")
    except ValueError:
        print("Please enter valid numeric values for length and width.")


print("Task 1: Calculate age")
CalculateAge()

print("\nTask 2: Calculate the area of a rectangle")
CalculateAreaOfRectangle()

# # Q3: Write a program that calculates the area of a circle.
# try:
#     pie = 3.14
#     radius = float(
#         input("\nTask3: Area of the circle.\nEnter the radius of the circle: ")
#     )
#     if radius < 0:
#         print("Radius cannot be negative.")
#     else:
#         area_of_circle = pie * (radius**2)
#         print(f"Pie = {pie}, Radius = {radius}\nArea of Circle = {area_of_circle:.2f}")
# except ValueError:
#     print("Please enter a valid number for the radius.")

# # Q4: Write a program that calculates the area of the cube
# try:
#     s = float(input("\nTask4: Area of the cube.\nEnter the side length of the cube: "))
#     if s < 0:
#         print("Side length cannot be negative.")
#     else:
#         area_of_cube = 6 * (s**2)
#         print(f"S = {s}\nArea of Cube = 6 x {s}^2 = {area_of_cube:.2f}")
# except ValueError:
#     print("Please enter a valid number for the side length.")

# # Q5: Create a program that converts a temperature from Fahrenheit to Celsius and vice versa using a variable.
# try:
#     temperature_in_fahrenheit = float(
#         input(
#             "\nTask5: Temperature from Fahrenheit to Celsius and Vice versa\nEnter the temperature in Fahrenheit: "
#         )
#     )
#     temperature_in_celsius = (temperature_in_fahrenheit - 32) * 5 / 9
#     print(
#         f"{temperature_in_fahrenheit} degrees Fahrenheit is equal to {temperature_in_celsius:.2f} degrees Celsius."
#     )
#     print(
#         f"{temperature_in_celsius:.2f} degrees Celsius is equal to {(temperature_in_celsius * 9 / 5 + 32):.2f} degrees Fahrenheit."
#     )
# except ValueError:
#     print("Please enter a valid number for the temperature.")

# # Q6: Convert a given number of seconds into minutes and seconds using variables.
# try:
#     seconds = int(
#         input("\nTask6: Converting Sec into Min/Sec\nEnter the number of seconds: ")
#     )
#     if seconds < 0:
#         print("Seconds cannot be negative.")
#     else:
#         minutes = seconds // 60
#         remaining_seconds = seconds % 60
#         print(
#             f"{seconds} Seconds, Equal to {minutes} Minutes, and {remaining_seconds} Seconds."
#         )
# except ValueError:
#     print("Please enter a valid integer for the seconds.")

# # Q7: Write a program that calculates the percentage.
# try:
#     total_marks = float(
#         input("\nTask7: Calculating the percentage\nEnter the total marks: ")
#     )
#     obtained_marks = float(input("Enter the obtained marks: "))
#     if total_marks <= 0:
#         print("Total marks must be greater than zero.")
#     elif obtained_marks < 0 or obtained_marks > total_marks:
#         print("Obtained marks must be between 0 and the total marks.")
#     else:
#         percentage = (obtained_marks / total_marks) * 100
#         print(
#             f"Obtained Marks = {obtained_marks}, Total Marks = {total_marks}\nPercentage = {percentage:.2f}%"
#         )
# except ValueError:
#     print("Please enter valid numbers for the marks.")
