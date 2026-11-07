# Latihan No-1
mahasiswa = ("Maulana Abimanyu Pradana","2605060051","Teknologi Informasi")
print(f"NIM = {mahasiswa[1]}")
print(f"Prodi = {mahasiswa[2]}")
#mahasiswa[2] = "Teknologi Informasi"

nilai_angka = {10, 4, 3, 2, 4, 10, 7, 5}
print(nilai_angka)

# Latihan No-2
data_mahasiswa = {
    "nim": "240101",
    "nama": "Budi Santoso",
    "prodi": "Teknologi Informasi"
}
data_mahasiswa["prodi"] = "Sastra Mesin"
data_mahasiswa["angkatan"] = 2026
data_mahasiswa.pop("nim")
print(data_mahasiswa)

# Latihan No-3
keranjang = {
    "apel": 5000,
    "pisang": 3000,
    "jeruk": 7000,
    "anggur": 15000
}
for key, value in keranjang.items():
    print(f"Harga {key} = Rp {value}")
print(f"Total harga belanjaan = Rp {sum(keranjang.values())}")