from buku import Buku

class AplikasiPerpustakaan:
    def __init__(self, manajer):
        self.__manajer = manajer
        self.__petugas_aktif = None

    def jalankan(self):
        print("=== SISTEM MANAJEMEN PERPUSTAKAAN ===")
        if not self.menu_login():
                print("Login gagal 3 kali. Program dihentikan.")
                return
        
        while True:
            self.tampilkan_menu()
            pilihan = input("Pilih menu (1-6): ").strip()
        
            if pilihan == "1":
                self.menu_tambah()
            elif pilihan == "2":
                self.menu_tampilkan_semua()
            elif pilihan == "3":
                self.menu_cari()
            elif pilihan == "4":
                        self.menu_perbarui()
            elif pilihan == "5":
                        self.menu_hapus()
            elif pilihan == "6":
                        print("Keluar dari aplikasi. Sampai jumpa!")
                        break
            else:
                        print("Pilihan tidak valid. Silakan pilih angka 1-6.")