# Calculator

# def add(a,b):
#     return a+b
# def subtract(a,b):
#     return a-b
# def multiply(a,b):
#     return a*b
# def divide(a,b):
#     return a/b


# num1 = int(input("Enter num 1 = "))
# num2 = int(input("Enter num 2 = "))
# operator = input("Enter operator symbol only = ")

# match operator:
#     case "+":
#         print(add(num1,num2))
#     case "-":
#         print(subtract(num1,num2))
#     case "*":
#         print(multiply(num1,num2))
#     case "/":
#         print(divide(num1,num2))
#     case default:
#         print("Wrong Operator/ Use only +,-,*,/")



# Max Finder 

# def MaxFinder(myList):
#     return sorted(myList).pop(len(myList) - 1)


# list_of_num = [3,5,450,6,73,90,34]

# print(MaxFinder(list_of_num))



# Greeting Machine

# def greetings(name = "Ani"):
#     print(f"Hello, How are You {name}")

# greetings("tejas")




# Temperature Converter

# def temp_converter(num, conversion_unit):
#     if conversion_unit == 'F':
#         return (num * 9/5) + (32)
#     elif conversion_unit == 'C':
#         return (num - 32) * (5/9)
#     else :
#         return None


# conversion_unit = input("Enter the conversion Unit to F / C = ").upper()
# num  = float(input("Enter a num = ").upper())

# print(temp_converter(num, conversion_unit))