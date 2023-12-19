print("============PILIH MENU========")
print("1.Tambah")
print("2.Kurang")
print("3.Kali")
print("4.Bagi")
billpertama = int(input("Masukan Angka Pertama:"))
billkedua = int(input("Masukan Angka Kedua:"))
print ("pilihan anda:1")
print("hasil", billpertama+billkedua)

print("============PILIH MENU========")
print("1.Tambah")
print("2.Kurang")
print("3.Kali")
print("4.Bagi")
billpertama = int(input("Masukan Angka Pertama:"))
billkedua = int(input("Masukan Angka Kedua:"))
print ("pilihan anda:2")
print("hasil", billpertama-billkedua)

print("============PILIH MENU========")
print("1.Tambah")
print("2.Kurang")
print("3.Kali")
print("4.Bagi")
billpertama = int(input("Masukan Angka Pertama:"))
billkedua = int(input("Masukan Angka Kedua:"))
print ("pilihan anda:3")
print("hasil", billpertama*billkedua)

print("============PILIH MENU========")
print("1.Tambah")
print("2.Kurang")
print("3.Kali")
print("4.Bagi")
billpertama = int(input("Masukan Angka Pertama:"))
billkedua = int(input("Masukan Angka Kedua:"))
print ("pilihan anda:4")
print("hasil", billpertama/billkedua)




MULAI SEKO IKI 
class Node:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia
        self.left = None
        self.right = None

def tambah_penduduk(root, nama, usia):
    if root is None:
        return Node(nama, usia)
    else:
        if nama < root.nama:
            root.left = tambah_penduduk(root.left, nama, usia)
        else:
            root.right = tambah_penduduk(root.right, nama, usia)
    return root

def tampilkan_urut_nama(root):
    if root:
        tampilkan_urut_nama(root.left)
        print(root.nama, "-", root.usia, "tahun")
        tampilkan_urut_nama(root.right)

def tampilkan_urut_usia(root):
    if root:
        tampilkan_urut_usia(root.left)
        print(root.nama, "-", root.usia, "tahun")
        tampilkan_urut_usia(root.right)

# Inisialisasi root
root = None

while True:
    print("\nPilih Menu:")
    print("1. Tambah Penduduk\n2. Tampilkan Urut Nama\n3. Tampilkan Urut Usia")
    pilihan = int(input("Pilihan Anda: "))

    if pilihan == 1:
        nama = input("Masukkan Nama: ")
        usia = int(input("Masukkan Usia: "))
        root = tambah_penduduk(root, nama, usia)
        print("Data berhasil ditambahkan!")

    elif pilihan == 2:
        print("Daftar Penduduk:")
        tampilkan_urut_nama(root)

    elif pilihan == 3:
        print("Daftar Penduduk:")
        tampilkan_urut_usia(root)

    else:
        print("Pilihan tidak valid. Silakan pilih kembali.")







