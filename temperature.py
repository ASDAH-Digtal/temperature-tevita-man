# Student Name: Tevita Manu
# Date: 17/03/2022

# 1. Write a print statement that says "Welcome to the Temperature Conversion program"
print("Welcome to the Temperature Conversion program by me")

# 2. Ask the user if they want to convert from Farenheit to Celsius or vice versa (provide 2 options)
choice = input("To Celsius or to Farenheit?")

# 3. Ask the user for a number to convert
temp = int(input("What is the number you wouold like to convert?"))

# 4. Convert the number to its respective temperature
farenheit = ["farenheit", "f" , "to farenheit"]
celsius = ["celsius", "c" , "to celsius"]
result = 0

if choice in farenheit:
    result = (temp * 9) / 5 + 32
elif choice in celsius:
    result = (temp - 32) * (5/9) 
else:
    print("Please choose \'farenheit\' or \'celsius\'")


# 5. Print the results
print(result)