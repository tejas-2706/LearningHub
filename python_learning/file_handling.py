# w - write and a - append mode

with open("example.txt", "w") as file:
    file.write("Hello , How are You ? \n")
    file.write("Hello , I am Good !! \n")


with open("example.txt", "r") as file:
    content = file.read()
    print(content)


with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())