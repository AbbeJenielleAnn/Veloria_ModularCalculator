# Function to add two numbers
def add(num1, num2):
    return num1 + num2
    
# Function to subtract numbers
def subtract(num1, num2):
    return num1 - num2
    
# Function to multiply numbers
def multiply(num1, num2):
    return num1*num2
    
# Function to divide two numbers
def divide(num1, num2):
    if num2 == 0:
        return "Cannot be divided by zero."
    else:
        return num1 / num2
        
# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
choice = input("Enter choice (Add, Subtract, Multiply, Divide): ")

# Call function and print result
if choice == "Add":
    print("Result:", add(num1, num2))
elif choice == "Subtract":
    print("Result:", subtract(num1, num2))
elif choice == "Multiply":
    print("Result:", multiply(num1, num2))
elif choice == "Divide":
    print("Result:", divide(num1, num2))
    