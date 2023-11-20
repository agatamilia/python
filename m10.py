print("=== PROGRAM PEMILIHAN  ===")
print("\n== Calon ==")
calon= ["ani", "bani", "ujang"]
no_urut = 1
for x in calon:
    print(f'{no_urut}. {x}')
    no_urut += 1

p_suara_1 = 0
p_suara_2 = 0
p_suara_3 = 0

while True:
    pilih = int(input("Masukkan nomor pilihan anda (1/2/3): "))
    if pilih == 1:
        p_suara_1 += 1
    elif pilih == 2:
        p_suara_2 += 1
    elif pilih == 3:
        p_suara_3 += 1
    lanjut= input("Apakah anda ingin lanjut memilih (y/n): ")
    if lanjut == 'y':
        pass
    elif lanjut == 'n':
        break

print("\n ==PEROLEHAN SUARA==")
print(f'1. ani =sebanyak {p_suara_1} suara')
print(f'1. bani =sebanyak {p_suara_2} suara')
print(f'1. ujang =  memperoleh sebanyak {p_suara_3} suara')