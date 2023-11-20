#amilia agata
nama=input("Nama: ")
umur=input("Umur: ")
alamat=input("Alamat: ")

teks="\nNama: {}\nUmur: {}\nAlamat: {}\n---".format(nama, umur, alamat)
nama_file=input("Masukkan nama file penyimpanan: ")
f=open(nama_file,'w')
f.write(teks)
f.close

print("Menampilkan data dari file")
nama_file=input("Masukkan Nama File: ")
try:
    f=open(nama_file)
    while True:
        baris=f.readline()
        if len(baris)==0:
            break
        print(baris)
    f.close
except:
    print("File yang diminta tidak ada.")




try:
    data= int(input("Berapa Followers facebook anda? \n"))
    print('Followers facebook anda sebanyak',data)
except:
    print('maaf, input yang diisi salah harus berupa angka.')
else:
    print('inputan yang diisi sudah benar,terimakasih atas infonya.')
