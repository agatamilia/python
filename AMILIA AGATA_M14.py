#AMILIA AGATA SI4505
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('bmh')
df= pd.read_csv('D:\MiLia\0telkom\semester2\ALPRO\data-jumlah-kapal-yang-diperiksa-dan-jumlah-pelanggaran-di-perairan-jakarta-tahun-2018-semester-i.csv')
x= df['bulan']
y= df['jumlah_kapal_yang_diperiksa']
plt.xlabel('bulan')
plt.ylabel('Jumlah kapal')
plt.bar(x,y)
'''
negara = [ "Brunei","Malaysia", "Filiphina", "Singapura", "Thailand", "Vietnam", "Myanmar", "ASEAN lainnya"]
# Sumber: Biro Pusat Statistik, Kementerian Hukum dan HAM (Direktorat Jendral Imigrasi) dan Hasil MPD
t2018 = [17279, 2503344, 217874, 1768744, 124153, 75816, 28616, 717508]
t2019 = [19278, 2980753, 260980, 1934445, 13699, 96024, 46381, 682630]
t2020 = [2701, 980118, 50413, 280492, 21303, 19608, 12669, 154143]

#line chart
plt.plot(negara, t2018, label='2018', color='red')
plt.plot(negara, t2019, label='2019', color='green')
plt.plot(negara, t2020, label='2020', color='blue')

#bar chart
plt.bar(negara, t2019, label='2019', color='lightcoral')
plt.bar(negara, t2018, label='2018', color='lightgreen')
plt.bar(negara, t2020, label='2020', color='steelblue')

#scatter plot
plt.scatter(negara, t2018, c ="red",linewidths = 2,marker ="*")
plt.scatter(negara, t2019, c ="green",linewidths = 2,marker ="*")
plt.scatter(negara, t2020, c ="blue",linewidths = 2,marker ="*")

plt.ylim(top=3000000)
plt.xlabel('Negara ASEAN')
plt.xticks(rotation=45)
plt.ylabel('Jumlah kunjungan')
plt.ticklabel_format(style='plain', axis='y')
plt.title('Jumlah kunjungan Wisatawan ASEAN ke Indonesia 2018-2019-2020')
plt.legend()
plt.show()
'''

