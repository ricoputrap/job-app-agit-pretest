from os.path import dirname, abspath
import sys
import xlsxwriter

# get the parent dir name of current dir
pretest_dir = dirname(dirname(abspath(__file__)))

# add path to folder Soal_1
sys.path.insert(0, pretest_dir + '\Soal_1')

from soal_nama_2 import SoalNama

soal = SoalNama()
soal.get_user_input()
soal.calculate_age()

# prepare inputs
inputs = [soal.nama, soal.email, soal.age_to_string()]

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