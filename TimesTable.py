# given a size value, this program
# generates a multiplication table of that size.

print("Welcome to the multiplication table generator. Please enter your desired number of \
rows and columns to view the table.\n")

rows = int(input("Rows: "))
columns = int(input("Columns: "))

row_list = list(range(rows))
column_list = list(range(columns))

for i in row_list:
    row_list[i] += 1

for j in column_list:
    column_list[j] += 1

tableValues = [] # the master list

for i in row_list:
    for j in column_list:
        tableValues.append(i * j)


length = 0
marker = 0
while length < len(column_list):
    length += 1
    marker += 1

    if length == len(column_list):
        print("\n")
        length = 0

    if marker == len(tableValues):
        break
        

for i in column_list:
    if i == 1:
        print("  " + str(i), end= " ")
    else:
        print(" " + str(i), end= " ")

print("")

for i in column_list:
    if i == 1:
        print("  --", end= " ")
    else:
        print("--", end= " ")

print("")

p = 0
row_string = ""
for i in row_list:          # nested for loop
    row_string = ""
    if not row_string:
        print(str(i) + "|", end=" ")

    for j in column_list:

        print(str(tableValues[p]) + "|", end= " ")

        row_string += "." # symbolizes that we already have a row going.

        p += 1

    print("")
