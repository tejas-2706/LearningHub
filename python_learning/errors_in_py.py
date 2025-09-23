# Handling Errors with try / except

# try : 
#     num = int(input("Enter a num = "))
#     print(10/num)
# except ValueError :
#     print("❌ Please enter a valid integer.")
# except ZeroDivisionError:
#     print("❌ Cannot divide by zero.")
# except Exception as e:
#     print(e)
# finally :
#     print("Done")



def square_root(x):
    if x < 0:
        raise ValueError("X is Negative no.")
    return x ** 0.5

print(square_root(-2))
