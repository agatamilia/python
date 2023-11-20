a= lambda s:s*s*s
angka= int(input('Masukkan sisi: '))
print(f"volume kubus dengan sisi{angka} adalah{a(angka)}")



'''



print(f'Median jumlah followers mahasiswa kelas A adalah {np.median(followers)}')
print(f'Rata-rata jumlah followers mahasiswa kelas A adalah {np.mean(followers)}')
n= int(input('masukan pendapatan:'))
if n < 2000000:
    print('A')
elif n > 2000000 and n <= 4000000:
    print('B')
elif n > 4100000 and n <= 5000000:
    print('C')
elif n > 5100000 and n < 7000000:
    print('D')
else:
    print('tidak mendapatkan bantuan')
''' 
'''
player1 = str(input("Masukan peran player 1: "))
player2 = str(input("Masukan peran player 2: "))

if player1 == player2:
    print("Game Seri")
elif player1 == "anjing":
    if player2 == "kucing":
       print("player2 menang")
    else:
       print("player1 menang")
elif player1 == "kucing":
    if player2 == "tikus":
       print("player2 menang")
    else:
       print("player1 menang")
elif player1 == "tikus":
    if player2 == "anjing":
       print("player2 menang")
    else:
       print("player1 menang")
else:
        print("Pilihan yang kamu masukan salah...")

print("========Menu======")
print("""1.pintu dan jendela
2.CCTV
3.alarm
""")
pilihan1 = (input("Masukkan pilihan 1 (pintu dan jendela/CCTV/alarm): "))
print("""1.nyalakan
2.matikan
""")
pilihan2 = (input("Masukkan pilihan (nyalakan/matikan): "))
match pilihan1:
    case'1':
        print ("Pintu dan Jendela")
    case'2':
        print("CCTV")
    case'3':
        print("Alarm")
    case _ :
        print("Tidak terdeteksi")

match pilihan2:
    case'1':
        print("dinyalakan")
    case'2':
        ket = "dimatikan"
    case _ :
        ket = "tidak terdeteksi"

i = 0

while i < 5:

    print(i,end = " ")

    i += 1

    if i == 3: 

        break

else:

        print(0)

baju=50000
celana=100000
def jumlah():
    total= (nbaju*baju) + (ncelana *celana)
    print(f"jumlah belanjaan anda {total}")
nbaju=int(input("Masukkan Jumlah baju:"))
ncelana=int(input("Masukkan jumlah celana: "))
jumlah()
'''
def tambah(angka_satu, angka_dua):
    jumlah=angka_satu+angka_dua
    print(jumlah)