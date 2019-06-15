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

# this works, which is awesome. let's now work on some logic to "prettyprint"
# the table so it looks more like a times table:

# for every number in columns, print that number.
# go to the next line.
# for every number there was above, print an underscore. This will be the beginning of the table.

# (3) then, for each row, print the FIRST row item, then a bar line, then the next row item, then a bar line.
#          (must check elements in row_list because we don't want a number at the end NOT contained by a line. )
# return to (3) until the entire chart is complete.

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

# if it's the beginning of a new row, write the value of the row itself (leftmost hand side)
# ELSE, for i in table values, write each table value followed by the bar line delimiter.
# must check to see if we're at the end of the row, then START THE LOOP OVER until all rows are complete.

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
