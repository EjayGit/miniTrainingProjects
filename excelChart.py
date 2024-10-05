from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference


spreadsheet = Workbook()
sheet = spreadsheet.active
rows = [
    ["Book Name", "Paperback", "Ebook"],
    ["DSA Swift", 35, 30],
    ["DSA Java", 45, 35],
    ["DSA Python", 40, 30],
    ["Python for kids", 20, 15],
    ["Scratch", 30, 25],
]

for row in rows:
    sheet.append(row)

chart = BarChart()
data = Reference(worksheet=sheet, min_row=1, max_row=6, min_col=1, max_col=3)
chart.add_data(data, titles_from_data=True)
sheet.add_chart(chart, "D2")
cats = Reference(worksheet=sheet,
                min_row=2,
                max_row=6,
                min_col=1,
                max_col=1)
chart.set_categories(cats)

spreadsheet.save("chart.xlsx")