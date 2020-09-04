from datetime import date

# get user input
nama = input('Masukan Nama : ')
email = input('Masukan Email : ')
tgl = input('Masukan tanggal lahir (DD-MM-YYYY) : ')

# extract dates element in int
dates = tgl.split('-')
day_birth, month_birth, year_birth = int(dates[0]), int(dates[1]), int(dates[2])

# prepare some age elements
today = date.today()
year_age = today.year - year_birth
month_age = today.month - month_birth
day_age = today.day - day_birth

# calculate month
if month_age < 0:
    year_age -= 1
    month_age = 12 - month_birth + today.month

if day_age < 0:
    month_age -= 1

# get age in formatted string
def age_to_string():
    if (month_age > 0):
        return('{} Tahun {} Bulan'.format(year_age, month_age))
    return('{} Tahun'.format(year_age))

print('=================================================')
print('Nama Anda : {}'.format(nama))
print('Email Anda : {}'.format(email))
print('Usia Anda : {}'.format(age_to_string()))