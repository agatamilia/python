#AMILIA AGATA

'''
ronde= int(input('banyak ronde?'))
kesempatan =0
ah=0
bh=0
while ronde > kesempatan:
    a= input("a: ")
    b= input("b: ")
    if a.lower() == "gunting":
        if b.lower() == "batu":
            kesempatan += 1
            ah += 1
        else:
            kesempatan += 1
            bh += 1
    elif a.lower() == "batu":
        if b.lower() == "kertas":
            kesempatan += 1
            ah += 1
        else:
            kesempatan += 1
            bh += 1
    elif a.lower() == "kertas":
        if b.lower() == "gunting":
            kesempatan += 1
            ah += 1
        else:
            kesempatan += 1
            bh += 1
    else:
        print('input salah!')
print('a sebanyak: ', ah, ' dan b sebanyak: ',bh )

ronde = int(input("Banyak ronde? "))
i = 0
scoretami = 0
scoreboi = 0
while i<ronde :
    Tami = str(input("Tami pilih apa? (B/G/K) "))
    Boi = str(input("Boi pilih apa? (B/G/K) "))
    
    if Tami == "B" and Boi == "B": 
        break 
    elif Tami == "B" and Boi == "G":
        scoretami +=1
    elif Tami == "B" and Boi == "K":
        scoreboi +=1
    elif Tami == "G" and Boi == "B":
        scoreboi +=1
    elif Tami == "G" and Boi == "G":
        break
    elif Tami == "G" and Boi == "K":
        scoretami +=1
    elif Tami == "K" and Boi == "B":
        scoretami +=1
    elif Tami == "K" and Boi == "G":
        scoreboi +=1
    elif Tami == "K" and Boi == "K":
        break
    i +=1

if scoretami > scoreboi:
    print("Selamat Tami menang sebanyak {} ronde".format(scoretami))
elif scoreboi > scoretami:
    print("Selamat Boi menang sebanyak {} Ronde".format(scoreboi))
else :
    print("Skor boi dan tami seri")
    
########
for m in range (1,11):
    print('atlet ke {}'. format(m))

########
for it in range(5,1,-1):
    print(it)
print('stop')

print("== COUNTDOWN SIMPLE ==")
angka= int(input())
while angka >2:
    print(angka-1)
    angka -= 1
print("it's enough")

##########
for x in range (1, 10, 2):
    for y in range (x):
        #i+0
        print(x, end='')
    print('')
########

total=0
ronde= int(input('banyak: '))
awal= 0
while awal < ronde:
    a=int(input('harga:'))
    if total >= 75000:        
        diskon= a-(a * 0.10)
        awal +=1
        total += diskon
    else:
        awal+=1
        total= a
print(total)

jumlah = int(input("Masukkan banyak barang belanjaan : "))

i = 0
total = []
while i<jumlah :
    barang = int(input("Masukkan harga barang : "))
    i +=1
    total.append(barang)

for j in total :
    final = sum(total)


if final > 75000:
    diskon = 0.2 * final
    final2 = sum(total) - diskon
    print("Total belanjaan sebelum diskon Rp. {}".format(final))
    print("Total belanjaan yang harus dibayar Rp. {}".format(final2))
else :
    print("Total belanjaan yang harus dibayar Rp.{}".format(final))
'''
