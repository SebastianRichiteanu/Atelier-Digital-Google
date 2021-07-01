# print("Files")
#
# with open("hello.txt", "w") as file:
#     file.write("hello world!")

import csv
with open("cars.csv", "r") as csv_file:
    rows = csv.reader(csv_file, delimiter=",")
    for row in rows:
        print(row)
