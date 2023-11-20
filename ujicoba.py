
"""
#terus = True
#while terus:
a = int(input('masukkan tahun:'))
if (a % 4 == 0 and a % 100 !=0 or a % 400 == 0):
    print ("Tahun Kabisat")
else:
    #terus = True
    print ("Bukan Tahun Kabisat")
"""
tanggal= int(input("masukan tanggal"))
bulan= int(input("masukan bln"))
tahun= int(input("masukan thn"))
angkasaya= (tanggal*1)+(bulan*10)+(tahun)
if( (angkasaya %4==0 and angkasaya %100!=0) or (angkasaya % 400 == 0)):
    print("kabisat")
else:
    print("bukan kabisat")