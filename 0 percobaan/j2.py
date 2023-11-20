
#pengelompokan status berdasarkan usia.
umur = int(input("Masukan Umur: "));

if umur > 60:
  print("Lansia")
elif 18 <= umur <= 59:
  print("Dewasa")
elif 13 <= umur <= 17:
  print("Remaja")
elif 6<= umur <= 13:
  print("anak-anak")
else:
  print("Inputan Salah")

pemain = input("Gunting, Batu, Kertas ? : ")
komputer = input("Gunting, Batu, Kertas ? : ")
if pemain == komputer:
    print("Seri!")
elif pemain == "Batu":
    if komputer == "Kertas":
       print("Kamu Kalah!", komputer, "membungkus", pemain)
    else:
       print("Kamu Menang!", pemain, "menghancurkan", komputer)
elif pemain == "Kertas":
    if komputer == "Gunting":
       print("Kamu Kalah!", komputer, "memotong", pemain)
    else:
       print("Kamu Menang!", pemain, "membungkus", komputer)
elif pemain == "Gunting":
    if komputer == "Batu":
       print("Kamu Kalah!", komputer, "menghancurkan", pemain)
    else:
       print("Kamu Menang!", pemain, "momotong", komputer)
else:
        print("Pilihan yang kamu masukan salah...")