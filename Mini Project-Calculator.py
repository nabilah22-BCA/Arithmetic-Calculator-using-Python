# Function for addition
def add(x, y):
    return x + y


# Function for subtraction
def subtract(x, y):
    return x - y


# Function for multiplication
def multiply(x, y):
    return x * y


# Function for division
def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed!"
    return x / y


# Function to get user input and validate it
def get_number_input(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Main calculator function
def calculator():
    print("Welcome to the Command-line Calculator!")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        # User selects the operation
        choice = input("\nEnter operation (1/2/3/4) or 'q' to quit: ")

        if choice == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            # Get user input for two numbers
            num1 = get_number_input("Enter the first number: ")
            num2 = get_number_input("Enter the second number: ")

            # Perform the selected operation
            if choice == '1':
                print("Result:",num1,"+",num2 ,"=", {add(num1, num2)})
            elif choice == '2':
                print("Result:",num1,"-", num2, "=", {subtract(num1, num2)})
            elif choice == '3':
                print("Result:",num1,"*",num2,"=",{multiply(num1, num2)})
            elif choice == '4':
                result = divide(num1, num2)
                print("Result:",num1,"/",num2, "=", result)
        else:
            print("Invalid choice! Please select a valid operation (1/2/3/4) or 'q' to quit.")


if __name__ == "__main__":
    calculator()
