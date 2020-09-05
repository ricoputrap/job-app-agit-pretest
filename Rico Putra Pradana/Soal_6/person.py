from datetime import date
import sys

class Person:
    def __init__(self):
        self.nama = ''
        self.email = ''
        self.tgl_lahir = ''
        self.month_age = 0
        self.year_age = 0
    
    def get_user_input(self):
        self.nama = input('Masukan Nama : ')
        self.email = input('Masukan Email : ')
        self.tgl_lahir = input('Masukan tanggal lahir (DD-MM-YYYY) : ')

    def calculate_age(self):
        # extract birth date elements to int
        try:
            dates = self.tgl_lahir.split('-')
            day_birth, month_birth, year_birth = int(dates[0]), int(dates[1]), int(dates[2])
        except:
            print('Salah memasukkan tanggal!')
            sys.exit('Terima kasih telah menggunakan program ini!')

        # prepare some age elements
        today = date.today()
        day_age = today.day - day_birth
        self.month_age = today.month - month_birth
        self.year_age = today.year - year_birth

        # finalize age
        if self.month_age < 0:
            self.year_age -= 1
            self.month_age = 12 - month_birth + today.month

        if day_age < 0:
            self.month_age -= 1
    
    # get age in formatted string
    def age_to_string(self):
        if (self.month_age > 0):
            return('{} Tahun {} Bulan'.format(self.year_age, self.month_age))
        return('{} Tahun'.format(self.year_age))