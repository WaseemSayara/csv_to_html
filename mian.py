import csv
import myModule as mm

arrOfEmp = []
heads =[]
# with open('Employee.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         tmp = list(','.join(row).split(","))
#         if tmp[0] == "ID":
#             continue
#         tmp2 = Employee(tmp[0], tmp[1], tmp[2], tmp[3], tmp[4], tmp[5], tmp[6])
#         arrOfEmp.append(tmp2)

with open('Employee.csv', newline='') as csvfile:
    spamreader = csv.DictReader(csvfile)
    for row in spamreader:
        heads=list(row.keys())
        tmp2 = mm.Employee(int(row['ID']), row['Name'], int(row['Salary']), row['Address'], row['Department'], row['Email'], row['Phone'])
        arrOfEmp.append(tmp2)


for i in arrOfEmp:
    i.printInfo()
print()

print(heads)

f1 = open("template.html", "r")
temp=f1.read()

table="<table class='table'> \n <tr>\n"
for i in heads:
    table+= "<th>"+ i + "</th>\n"
table+="</tr> \n"
for i in arrOfEmp:
    table +="<tr> \n"
    table += "<th> " + str(i.id_) + "</th> \n"
    table += "<th> " + i.name + "</th> \n"
    table += "<th> " + str(i.salary) + "</th> \n"
    table += "<th> " + i.address + "</th> \n"
    table += "<th> " + i.department + "</th> \n"
    table += "<th> " + i.email + "</th> \n"
    table += "<th> " + i.phone + "</th> \n"
    table += "</tr> \n"

print(table)
print("===============")
print(temp)

temp = temp.format(table)
f2 = open("template2.html" , "w")
f2.write(temp)