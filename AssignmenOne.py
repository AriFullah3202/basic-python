# 1. Print your name
print("Arifullah")

# 2. Input your batch number using input() function
batch_number = int(input("Enter your batch number: "))
print("Your batch number is:", batch_number)

# 3. Create 5 different valid variables and print
variableNumber = 10
VariableString = "Hello"
variable3_boolean = True
_variableList = [1, 2, 3]
variable_dictionary = {'name': 'John', 'age': 25}

print(variableNumber)
print(VariableString)
print(variable3_boolean)
print(_variableList)
print(variable_dictionary)

# 4. Create Pascal Case Variable
PascalCaseVariable = "This is a Pascal Case variable."
print(PascalCaseVariable)

# 5. Assign a single value to multiple variables with memory location
a = b = c = 10

print(a, b, c)
print(id(a), id(b), id(c))

# 6. Input float value using input()
float_value = float(input("Enter a float value: "))
print("You entered:", float_value ,".")

# 7. Convert 'a' to uppercase
a = 'Welcome to Django for web and Ai'
uppercase = a.upper()
print(uppercase)

# 8. Remove whitespace from 'b'
b = '    Python'
b_without_whitespace = b.strip()
print(b_without_whitespace)

# 9. Convert 'c' and 'd' from int to float
c = 60
d = 22

c_float = float(c)
d_float = float(d)

print(c_float, type(c_float))
print(d_float, type(d_float))

# 10. Create a dictionary and print your info
info = {
    'name': 'Arif ullah',
    'age': 25,
    'occupation': 'Software Developer'
}

print(info)
