from person import Person
from save_to_excel import Excel
from convert_img import ImageConverter

def print_main_menu():
    print('Silahkan pilih menu di bawah ini:')
    print('1: Menambahkan Data Diri')
    print('2: Tampilkan Data')
    print('3: Konversi Gambar')
    print('4: Keluar')

def print_save_menu():
    print('Tujuan penyimpanan:')
    print('1: Simpan sebagai file excel')
    print('2: Tidak perlu disimpan, cukup dicetak saja')

def print_user_data(new_person):
    print('Nama Anda : {}'.format(new_person.nama))
    print('Email Anda : {}'.format(new_person.email))
    print('Usia Anda : {}'.format(new_person.age_to_string()))

def print_convert_type():
    print('Pilih jenis konversi gambar:')
    print('1: Hitam Putih')
    print('2: Rotasi')

def print_rotation_type():
    print('Pilih jenis rotasi:')
    print('1: Rotasi ke kanan')
    print('2: Rotasi ke kiri')
    print('3: Pantulkan secara vertikal')

def print_img_selection():
    print('Silahkan pilih gambar memes berikut ini:')
    print('1: Bu Tejo')
    print('2: Yao Ming')
    print('3: Dua jam gak ngapa-ngapain')

def print_break():
    print('=================================================')

def print_success_msg(menu):
    print(menu + ' sukses!')

def print_closing_msg():
    print('Terima kasih telah menggunakan program ini!')

def add_new_person():
    print_save_menu()
    save_menu = input('Masukkan 1, 2, atau 3: ')
    print_break()

    # instatiate new person
    new_person = Person()
    new_person.get_user_input()
    new_person.calculate_age()
    print_break()

    # save to excel
    if save_menu == '1':
        filename = input('Masukkan nama file : ')
        new_excel = Excel(filename)
        new_excel.fill_header()
        new_excel.add_data(new_person.nama, new_person.email, new_person.age_to_string())
        new_excel.close_workbook()
        print_success_msg('Menyimpan data ke excel')

    # print new person data
    elif save_menu == '2':
        print_user_data(new_person)
        print_success_msg('Mencetak data diri')
        print_break()
        print_closing_msg()

    # back to save menu
    else:
        print('Mohon maaf Anda memasukkan pilihan yang kurang tepat.')
        print_break()
        add_new_person()

def open_main_menu():
    print_main_menu()
    main_menu = input('Masukkan 1, 2, atau 3: ')
    print_break()

    # add new person
    if main_menu == '1':
        add_new_person()
        
    # show all data
    elif main_menu == '2':
        pass 

    # convert image
    elif main_menu == '3':
        print_convert_type()
        convert_type = input('Masukkan 1 atau 2: ')
        print_break()
        
        print_rotation_type()
        rotation_type = int(input('Masukkan 1, 2, atau 3: '))
        print_break()

        print_img_selection()
        selected_img = int(input('Masukkan 1, 2, atau 3: '))
        
        img_converter = ImageConverter(selected_img)
        converted_img = img_converter.convert_to_gray() if convert_type == '1' else img_converter.rotate_img(rotation_type)
        img_converter.save_image(converted_img)
        img_converter.show_img(converted_img)
        print_success_msg('Mengonversi gambar')

    elif main_menu == '4':
        print('Terima kasih telah menggunakan program ini!')

    # back to main menu
    else:
        print('Mohon maaf Anda memasukkan pilihan yang kurang tepat.')
        print_break()
        open_main_menu()

print('Selamat datang di Program Terakhir')
open_main_menu()