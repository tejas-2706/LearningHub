import csv

data = [
    ['name', 'eng', 'math', 'science'],
    ['Alice', 95, 35, 45],
    ['Bob', 88, 56, 67],
    ['Charlie', 76, 45, 90],
]


# with open("students_data.csv", "w", newline='') as f:
#     writer = csv.writer(f)
#     writer.writerows(data)

def calculate_avg_marks():
    with open("students_data.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            name = row[0]
            eng = float(row[1])
            math = float(row[2])
            science = float(row[3])
            avg = (eng + math + science) / 3
            print(f"Name = {name} | avg. marks = {avg}")


calculate_avg_marks()