print("====== Program Pengategorian Usia ======")

usia = int(input("Masukan usia anda : ")) #pake int biar inputnya angka dan bisa dioperasikan dengan operator komparasi

anak_anak = usia > 0 and usia <= 12 #jika usia lebih dari 0 dan kurang dari sama dengan 12 maka dikategorikan sebagai anak-anak
remaja = usia >= 13 and usia <= 17 #jika usia lebih dari sama dengan 13 dan kurang dari sama dengan 17 maka dikategorikan sebagai remaja
dewasa = usia >= 18 and usia <= 59 #jika usia lebih dari sama dengan 18 dan kurang dari sama dengan 59 maka dikategorikan sebagai dewasa
#untuk lansia kita bakal pake else aja karena lansia itu usia 60 keatas, jadi ngga perlu pake operator komparasi lagi
usia_minus = usia < 0 #jika ada yg iseng input angka minus kita bakal kasih peringatan aja nantinya

print("========================================")

if anak_anak == True : #kondisi 1
    print("Anda dikategorikan sebagai anak-anak") #aksi 1
elif remaja == True: #kondisi 2
    print("Anda dikategorikan sebagai remaja") #aksi 2
elif dewasa == True: #kondisi 3
    print("Anda dikategorikan sebagai dewasa") #aksi 3
elif usia_minus == True: #kondisi 4
    print("Usia tidak bisa minus") #aksi 4
    print("Silahkan input usia yang valid") #aksi 5
else: #kondisi false
    print("Anda dikategorikan sebagai lansia") #aksi false
print("========== Akhir dari program ==========")