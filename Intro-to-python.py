

#Create a function that takes a list of numbers as an argument, squares each number, and returns a new list with the squared values.
list_of_numbers = [3, 99, 12, 1, 7]
def square_numbers(numbers):
    squared_numbers = []
    for number in numbers:
        squared_numbers.append(number ** 2)
    return squared_numbers

print (square_numbers(list_of_numbers))


userx = input("Enter a number: ")
usery = input("Enter another number: ")

userx = int(userx)
usery = int(usery)

def divide_numbers(x, y):
    try:
        result = x / y
        return result
    except ValueError:
        return "Error: Please enter valid numbers."
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    
print(divide_numbers(userx, usery))




account_balance = 1000

def withdraw(amount):
    try:
        amount = int(amount)
    except ValueError:
        return "Error: Please enter a valid number for the withdrawal amount." 
    global account_balance
    if amount <= account_balance:
        account_balance -= amount
        return f"Withdrawal successful! New balance: {account_balance}"
    else:
        return "Error: Insufficient funds."
    
print(withdraw(1500))
print(withdraw(600))  # This should trigger an error due to insufficient funds
