# from person import Person

# print('Selamat datang di Program Terakhir')

# def print_main_menu():
#     print('Menu:')
#     print('1: Menambahkan Data Diri')
#     print('2: Konversi Gambar')

# def print_user_data(new_person):
#     print('=================================================')
#     print('Nama Anda : {}'.format(new_person.nama))
#     print('Email Anda : {}'.format(new_person.email))
#     print('Usia Anda : {}'.format(new_person.age_to_string()))

# print_main_menu()
# main_menu = input('Masukkan 1 atau 2: ')

# if main_menu == '1':
#     new_person = Person()
#     new_person.get_user_input()
#     new_person.calculate_age()

#     print('Tujuan penyimpanan:')
#     print('1: simpan sebagai file excel')
#     print('2: simpan ke database')
#     print('3: tidak jadi disimpan, cukup dicetak saja')

#     save_menu = input('Masukkan 1, 2, atau 3: ')
#     if save_menu == '1':
#         pass # save to excel
#     elif save_menu == '2':
#         pass # save to db
#     elif save_menu == '3':
#         print_user_data(new_person)
#     else:
#         pass # kembali take save_menu
# elif main_menu == '2':
#     pass # open cv

# else:
#     pass # kembali take main_menu

from save_to_excel import Excel

nama = input('Masukan Nama : ')
email = input('Masukan Email : ')
tgl_lahir = input('Masukan tanggal lahir (DD-MM-YYYY) : ')

excel_1 = Excel()
excel_1.fill_header()
excel_1.add_data(nama, email, tgl_lahir)
excel_1.close_workbook()

excel_2 = Excel('coba')
excel_2.fill_header()
excel_2.add_data('rico', 'ricoputra', '21-01-1998')
excel_2.close_workbook()