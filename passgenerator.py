import random
letters = ["a", "s", "d", "f", "g", "h", "j", "k", "l", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "z", "x", "c", "v", "b", "n", "m"]
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "=", "_", "+", "-", ",", ".", "?"]
print ("Welcome to password generator!")
amount_letters = int (input ("How many letters would you like? "))
amount_numbers = int (input ("How many numbers would you like? "))
amount_symbols = int (input ("How many symbols would you like? "))
password = []
for num in range (0, amount_letters):
    password += random.choice (letters)
for num in range (0, amount_numbers):
    password += random.choice (numbers)
for num in range (0, amount_symbols):
    password += random.choice (symbols)
final_password = ""
random.shuffle (password)
for i in password:
    final_password += i
print (final_password)