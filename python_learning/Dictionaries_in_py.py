# Dictionaries – Key–Value Pairs

# Think of it as a mini database.

person = {
    "name" : "tejas",
    "age" : "22",
    "gender" : "male",
    "city" : "aurangabad"
}

print(person["age"])

person["age"] = 23

person["country"] = "India"

print(person)


for key,value in person.items():
    print(key, "=>", value)


print(len(person))
print(sorted(person))
print(dict(person))
print(set(person))
print(list(person))

