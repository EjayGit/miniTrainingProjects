from openpyxl import Workbook, load_workbook
from random import random
import numpy as np
import names


redText = Font(color="00FF0000", size=12, bold=True)
centerAlign = Alignment(horizontal='center')
mu, sigma = 0.6, 0.1
nameNum = int(input("How many names would you like to have in your list? "))
newWorkbook = Workbook()
sheet = newWorkbook.active
sheet["A1"].font = redText 
sheet["A1"].alignment = centerAlign
sheet["A1"] = 'Name'
sheet["B1"].font = redText
sheet["A1"].alignment = centerAlign
sheet['B1'] = 'Score'
borderSide = Side(border_style='double')
squareBorder = Border(top=borderSide, left=borderSide, right=borderSide, bottom=borderSide)
header = NamedStyle(name="header")
header.font = Font(bold=True, size=13)
header.border=Border(bottom=Side(border,style="double"))
header.alignment=Alignment(horizontal="center", vertical="center")
firstRow = sheets[1]
print(firstRow)
for cell in firstRow:
    cell.style = header
for row in range(2,nameNum):
    m_f = random()
    scoreNum = np.random.normal(mu, sigma)
    if scoreNum > 1:
        scoreNum = 1
    if scoreNum < 0:
        scoreNum = 0
    if m_f%2 == 0:
        sheet["A"+str(row)] = names.get_full_name(gender='female')
        sheet["B"+str(row)] = scoreNum*100
        sheet["C"+str(row)] = f'=ROUND(B{str(row)})'
        sheet["C"+str(row)].border = squareBorder
    else:
        sheet["A"+str(row)] = names.get_full_name(gender='male')
        sheet["B"+str(row)] = scoreNum*100
        sheet["C"+str(row)] = f'=ROUND(B{str(row)})'
        sheet["C"+str(row)].border = squareBorder
newWorkbook.save("name.xlsx")
