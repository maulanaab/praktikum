panjang = 12
lebar = 5
tinggi = 8

print("Hitunglah luas, volume dan keliling dari bangunan tersebut!")
#Rumus luas permukaan balok adalah L = 2 * (p*l + p*t + l*t)
luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi) #Variabel luas akan menyimpan nilai dari operasi dengan rumus diatas
print("Luas Permukaan =", luas) #Hasil operasi diatas akan ditampilkan disini

#Rumus volume balok adalah V = p * l * t
volume = panjang * lebar * tinggi #Variabel volume akan menyimpan nilai dari operasi dengan rumus diatas
print("Volume =", volume) #Hasil operasi diatas akan ditampilkan disini

#Rumus keliling balok adalah K = 4 × (p + l + t)
keliling = 4 * (panjang + lebar + tinggi) #Variabel keliling akan menyimpan nilai dari operasi dengan rumus diatas
print("Keliling =", keliling) #Hasil operasi diatas akan ditampilkan disini

print(" ") #Menampilkan baris kosong, biar rapi aja
print("Apakah luas bangunan tersebut lebih luas dari 50?")
#hasil dari luas sudah kita dapat diatas jadi langsung aja kita komparasikan dengan > 50
print("Jawaban:", luas > 50) #hasilnya akan muncul disini

print(" ") #Lagi, biar rapi aja
print("Apakah volume bangunan tersebut bernilai 480?")
#hasil dari volume juga sudah kita dapat diatas jadi langsung aja kita komparasikan dengan == 480
print("Jawaban:", volume == 480) #hasilnya akan muncul disini