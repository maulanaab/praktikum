# 1. Buat program yang menampilkan bilangan ganjil dan genap dari 1 sampai 50 menggunakan perulangan!

angka = range(1,51)

for i in angka:
    if i % 2 != 0: #jika angka % 2 != 0, maka angka adl ganjil
        print(f"Angka {i} adalah ganjil")
    else: #kalau kondisi tadi tidak terpenuhi maka angka adl genap
        print(f"Angka {i} adalah genap")
print("Selesai")

# 2. Buat program yang menampilkan semua bilangan prima antara 1 sampai 100 menggunakan perulangan!

angka = range(2,101)

for num in angka:
    for dif in range(2,num):
        if num % dif == 0:
            break
    else:
        print(f"{num} adalah bilangan prima")