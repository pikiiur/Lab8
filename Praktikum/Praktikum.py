class DaftarNilaiMahasiswa:
    def __init__(self):
        self.daftar_nilai = {}  # Membuat dictionary untuk menyimpan nilai mahasiswa

    def tambah(self, nama, nilai):
        self.daftar_nilai[nama] = nilai  # Menambahkan data nilai mahasiswa ke dictionary

    def tampilkan(self):
        if self.daftar_nilai:
            print("Daftar Nilai Mahasiswa:")
            for nama, nilai in self.daftar_nilai.items():
                print(f"{nama}: {nilai}")
        else:
            print("Daftar nilai mahasiswa kosong.")

    def hapus(self, nama):
        if nama in self.daftar_nilai:
            del self.daftar_nilai[nama]
            print(f"Data nilai untuk {nama} telah dihapus.")
        else:
            print(f"Data untuk {nama} tidak ditemukan.")

    def ubah(self, nama, nilai_baru):
        if nama in self.daftar_nilai:
            self.daftar_nilai[nama] = nilai_baru
            print(f"Data nilai untuk {nama} telah diubah menjadi {nilai_baru}.")
        else:
            print(f"Data untuk {nama} tidak ditemukan.")

# daftar mahasiswa:
daftar_nilai_mahasiswa = DaftarNilaiMahasiswa()
daftar_nilai_mahasiswa.tambah("Pikii", 85)
daftar_nilai_mahasiswa.tambah("Dikii", 90)
daftar_nilai_mahasiswa.tambah("Abim", 75)

daftar_nilai_mahasiswa.tampilkan()

daftar_nilai_mahasiswa.hapus("Abim")
daftar_nilai_mahasiswa.tampilkan()

daftar_nilai_mahasiswa.ubah("Pikii", 95)
daftar_nilai_mahasiswa.tampilkan()

