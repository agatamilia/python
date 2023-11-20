import numpy as np

followers = []
x=int(input('Masukan banyak mahasiswa kelas A:'))

for i in range (x):
    y= int(input('Masukan jumlah followers mahasiswa kelas A:'))
    followers.append(y)
print(f'Median jumlah followers mahasiswa kelas A adalah {np.median(followers)}')
print(f'Rata-rata jumlah followers mahasiswa kelas A adalah {np.mean(followers)}')
print(f'Akun dengan jumlah followers terkecil adalah sebanyak {np.min(followers)}')
print(f'Akun dengan jumlah followers terbanyak adalah sebanyak {np.max(followers)}')
