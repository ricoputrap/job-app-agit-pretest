from person import Person
from save_to_excel import Excel

print('Selamat datang di Program Terakhir')

def print_main_menu():
    print('Menu:')
    print('1: Menambahkan Data Diri')
    print('2: Tampilkan Data')
    print('3: Konversi Gambar')

def print_save_menu():
    print('Tujuan penyimpanan:')
    print('1: simpan sebagai file excel')
    print('2: simpan ke database')
    print('3: tidak perlu disimpan, cukup dicetak saja')

def print_user_data(new_person):
    print('Nama Anda : {}'.format(new_person.nama))
    print('Email Anda : {}'.format(new_person.email))
    print('Usia Anda : {}'.format(new_person.age_to_string()))

def print_break():
    print('=================================================')

def print_success_msg(menu):
    print(menu + ' sukses!')

print_main_menu()
main_menu = input('Masukkan 1, 2, atau 3: ')
print_break()

# add new person
if main_menu == '1':
    print_save_menu()
    save_menu = input('Masukkan 1, 2, atau 3: ')
    print_break()

    # instatiate new person
    new_person = Person()
    new_person.get_user_input()
    new_person.calculate_age()

    # save to excel
    if save_menu == '1':
        filename = input('Masukkan nama file : ')
        new_excel = Excel(filename)
        new_excel.fill_header()
        new_excel.add_data(new_person.nama, new_person.email, new_person.age_to_string())
        new_excel.close_workbook()
        print_success_msg('Menyimpan data ke excel')

    # save to db
    elif save_menu == '2':
        pass

    # print out
    elif save_menu == '3':
        print_break()
        print_user_data(new_person)
    else:
        pass # kembali take save_menu

# show all data
elif main_menu == '2':
    pass 

# open cv
elif main_menu == '3':
    pass

else:
    pass # kembali take main_menu

# from save_to_excel import Excel

# nama = input('Masukan Nama : ')
# email = input('Masukan Email : ')
# tgl_lahir = input('Masukan tanggal lahir (DD-MM-YYYY) : ')

# excel_1 = Excel()
# excel_1.fill_header()
# excel_1.add_data(nama, email, tgl_lahir)
# excel_1.close_workbook()

# excel_2 = Excel('coba')
# excel_2.fill_header()
# excel_2.add_data('rico', 'ricoputra', '21-01-1998')
# excel_2.close_workbook()