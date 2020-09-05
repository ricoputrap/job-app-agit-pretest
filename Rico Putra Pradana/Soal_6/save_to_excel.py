import xlsxwriter

class Excel:
    def __init__(self, filename='soal_6.xlsx'):
        self.workbook = xlsxwriter.Workbook(filename + '.xlsx')
        self.worksheet = self.workbook.add_worksheet()
        self.row_number = 1
    
    def fill_header(self):
        self.worksheet.write('A1', 'nama')
        self.worksheet.write('B1', 'email')
        self.worksheet.write('C1', 'usia')
    
    def add_data(self, nama, email, usia):
        self.row_number += 1
        self.worksheet.write('A' + str(self.row_number), nama)
        self.worksheet.write('B' + str(self.row_number), email)
        self.worksheet.write('C' + str(self.row_number), usia)
    
    def close_workbook(self):
        self.workbook.close()