import openpyxl as xl
from openpyxl import BarChart, Reference

def process_workbook(filename):
    wb = xl.load_workbook(filename)
    sheet = wb["Sheet1"]
    '''cell = sheet["a1"] #how to access to cell
    print(cell.value)'''
    '''print(sheet.max_row)''' #this shows how many row we have in excel sheet
    for row in range(3, sheet.max_row + 1):
        cell = sheet.cell(row, 3)

        corrected_price = cell.value * 0.9
        print(corrected_price)
        corrected_price_cell = sheet.cell(row, 4)
        corrected_price_cell.value = corrected_price

    values = Reference (sheet, min_row=2,
               max_row = sheet.max_row,
               min_col = 4,
               max_col = 4)
    chart = BarChart()
    chart.add_data(values)
    sheet.add_chart(chart,"e2")
    wb.save(filename)
