'''
{IS: diberikan nilai a, b, dan c}
{FS: hitung penjumlahan a dan b, kemudian dikurangi c}

Kamus: A,B,C,nilai:int

Algoritma:
Output("Masukkan nilai A")
Input(A)
Output("Masukkan nilai B")
Input(B)
Output("Masukkan nilai C")
Input(C)
nilai= (A+B)-C
Output("Hasil nilai (A+B)-C adalah ")
Output(nilai)
'''

A= int(input("Masukan nilai A= "))
B= int(input("Masukan nilai B= "))
C= int(input("Masukan nilai C= "))
nilai= (A+B)-C
print("Hasil nilai (A+B)-C adalah:{}" .format(nilai))