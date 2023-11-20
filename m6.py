#AMILIA AGATA
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