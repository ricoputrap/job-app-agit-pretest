import xlsxwriter

# prepare inputs
inputs = ['rico', 'rico.putra@outlook.co.id', '22 Tahun']

# create a new excel file & worksheet
workbook = xlsxwriter.Workbook('rico_putra_pradana.xlsx')
worksheet = workbook.add_worksheet()

# fill the header
worksheet.write('A1', 'nama')
worksheet.write('B1', 'email')
worksheet.write('C1', 'usia')

# fill the body
worksheet.write('A2', inputs[0])
worksheet.write('B2', inputs[1])
worksheet.write('C2', inputs[2])

# fit column width to contents
for i in range(3):
    char_len = len(inputs[i])
    if char_len > 5: worksheet.set_column(i, i, char_len + 1)

# close the excel file
workbook.close()