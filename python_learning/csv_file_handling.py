import csv

with open("students.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Roll", "English", "Math"])
    writer.writerow(["Tejas", 24, 80, 40])


with open("students.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)