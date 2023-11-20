#AMILIA AGATA

print('\nData Jumlah Karyawan PT.sukses per-Divisi')
karyawan = {
"Produksi": "239", 
"Pemasaran": "278", 
"Administrasi": "214",
"Personalia": "123"}
try:
    divisi= str(input("Sebutkan Nama Divisi: "))
    #untuk tidak dibedakan huruf besar huruf kecil
    divisi1= divisi.lower()
    divisi2= divisi1.capitalize()
    print (f"jumlah karyawan pada Divisi {divisi2} adalah sebanyak {karyawan[divisi2]} karyawan.")  
except KeyError:  
    print (f"Divisi {divisi2} tidak ada di dalam data")    
finally:
    print('\nTerimakasih telah menggunakan program')