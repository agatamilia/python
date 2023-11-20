

username = "alpro"
password = "telyu123"
jawaban = (username,password)
jumlah_tebakan = 0
kesempatan =3
while jumlah_tebakan < kesempatan:
  user= input("username: ")
  pas= input("password: ")
  hasil= (user,pas)
  jumlah_tebakan += 1
  if hasil != jawaban :
    print("Login gagal. Sisa percobaan login sebanyak ", kesempatan)
  elif hasil == jawaban :
    print("Selamat, anda berhasil login!")
    break
else:
  print("maaf percobaan login sudah habis, silahkan mulai dari awal kembali.")
'''
####
maks = int(input("Masukkan maks jumlah kolom/baris : "));
for bintang in range (0,maks):
    for pola in range (0, maks):
        print(" ",end=" ")
    maks-=1
    print("",'*')



total=0
barang=[]
harga=[]
ulang= True
print("""
    ==== SELAMAT DATANG DI PROGRAM BUTIK====
    1. KAOS  : 5000
    2. KEMEJA: 1000
    3. JAS   : 3000
    4. SELESAI
    """)
while ulang==True:
    pesan= int(input("masukan barang: "))
    if pesan == 1:
      barang.append('kaos')
      harga.append(5000)
      total += 5000
    elif pesan == 2:
      barang.append('kemeja')
      harga.append(1000)
      total += 1000
    elif pesan == 3:
      barang.append('jas')
      harga.append(3000)
      total += 3000
    elif pesan == 4:
      print("total barang", total)
      ulang= False
      break
else:
    print('not found')
    '''