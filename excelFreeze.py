from openpyxl import Workbook

workbook = loadWorkbook("AmazonReviews.xlsx")
sheet = workbook.active
sheet.freeze_panes("C3")
wookbook.save("AmazonReviews2.xlsx")
sheet.auto_filter.ref = "A1:J1896"
workbook.save("AmazonReviews3.xlsx")