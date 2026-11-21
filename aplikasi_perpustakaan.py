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

    def menu_login(self):
        percobaan = 0
        while percobaan < 3:
            print("\n--- LOGIN PETUGAS ---")
            username = input("Username : ").strip()
            password = input("Password : ").strip()
    
            petugas = self.__manajer.login(username, password)
            if petugas is not None:
                self.__petugas_aktif = petugas
                print(f"Login berhasil! Selamat datang, {petugas.get_nama()}.")
                return True
    
            percobaan += 1
            print(f"Username atau password salah. Sisa percobaan: {3 - percobaan}")
    
        return False
    
    def tampilkan_menu(self):
               print(f"\n=== MENU UTAMA (Petugas: {self.__petugas_aktif.get_nama()}) ===")
               print("1. Tambah Data Buku")
               print("2. Tampilkan Semua Buku")
               print("3. Cari Buku (berdasarkan Kode)")
               print("4. Perbarui Data Buku")
               print("5. Hapus Data Buku")
               print("6. Keluar")

