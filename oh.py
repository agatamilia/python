"""
{IS: Diberikan Nilai Diagonal 1 dan Diagonal 2}
{FS:Hitung Luas layang-layang}

Kamus: D1,D2,luas :float

Algoritma:
Output("Masukkan nilai diagonal 1(cm): ")
Input(D1)
Output("Masukkan nilai diagonal 2(cm): ")
Input(D2)
luas=(D1*D2)/2
Output("Luas layang-layang: ")
Output(luas)

"""
D1=float(input("Masukkan nilai diagonal 1(cm): "))
D2=float(input("Masukkan nilai diagonal 2(cm): "))
luas=float((D1*D2)/2)
print("Luas layang-layang:{} ".format(luas),"cm")
