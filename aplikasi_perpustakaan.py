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

    def menu_tambah(self):
        print("\n--- TAMBAH DATA BUKU ---")
        kode = input("Kode Buku    : ").strip()
        if kode == "":
            print("Kode buku tidak boleh kosong.")
            return
    
        if self.__manajer.cari_buku(kode) is not None:
            print(f"Gagal! Buku dengan kode '{kode.upper()}' sudah terdaftar.")
            return
    
        judul = input("Judul Buku   : ").strip()
        penulis = input("Penulis      : ").strip()
        penerbit = input("Penerbit     : ").strip()
    
        try:
            tahun = int(input("Tahun Terbit : ").strip())
            stok = int(input("Jumlah Stok  : ").strip())
        except ValueError:
            print("Gagal! Tahun terbit dan stok harus berupa angka.")
            return
    
        buku_baru = Buku(kode, judul, penulis, penerbit, tahun, stok)
        if self.__manajer.tambah_buku(buku_baru):
            print("Data buku berhasil ditambahkan dan disimpan.")
        else:
            print("Gagal menambahkan data buku.")

    def menu_tampilkan_semua(self):
        print("\n--- DAFTAR KOLEKSI BUKU ---")
        daftar = self.__manajer.get_semua_buku()
        if len(daftar) == 0:
            print("Belum ada data buku tersimpan.")
            return

        w_no = max(2, len(str(len(daftar))))
        w_kode = 4
        w_judul = 5
        w_penulis = 7
        w_penerbit = 8
        w_tahun = 5
        w_stok = 4

        for buku in daftar:
            w_kode = max(w_kode, len(buku.get_kode_buku()))
            w_judul = max(w_judul, len(buku.get_judul()))
            w_penulis = max(w_penulis, len(buku.get_penulis()))
            w_penerbit = max(w_penerbit, len(buku.get_penerbit()))
            w_stok = max(w_stok, len(str(buku.get_stok())))

        header = (
            f"| {'No':<{w_no}} | {'Kode':<{w_kode}} | {'Judul':<{w_judul}} | "
            f"{'Penulis':<{w_penulis}} | {'Penerbit':<{w_penerbit}} | "
            f"{'Tahun':<{w_tahun}} | {'Stok':<{w_stok}} |"
        )
        garis = "-" * len(header)

        print(garis)
        print(header)
        print(garis)

        nomor = 1
        for buku in daftar:
            print(
                f"| {nomor:<{w_no}} | {buku.get_kode_buku():<{w_kode}} | "
                f"{buku.get_judul():<{w_judul}} | {buku.get_penulis():<{w_penulis}} | "
                f"{buku.get_penerbit():<{w_penerbit}} | {buku.get_tahun_terbit():>{w_tahun}} | "
                f"{buku.get_stok():>{w_stok}} |"
            )
            nomor += 1

        print(garis)

def menu_cari(self):
        print("\n--- CARI DATA BUKU ---")
        kode = input("Masukkan Kode Buku: ").strip()
        buku = self.__manajer.cari_buku(kode)

        if buku is None:
            print(f"Buku dengan kode '{kode.upper()}' tidak ditemukan.")
        else:
            garis = "-" * 49
            print(garis)
            print(f"| {'Kode Buku':<12} : {buku.get_kode_buku():<30} |")
            print(f"| {'Judul':<12} : {buku.get_judul():<30} |")
            print(f"| {'Penulis':<12} : {buku.get_penulis():<30} |")
            print(f"| {'Penerbit':<12} : {buku.get_penerbit():<30} |")
            print(f"| {'Tahun Terbit':<12} : {buku.get_tahun_terbit():<30} |")
            print(f"| {'Stok':<12} : {buku.get_stok():<30} |")
            print(garis)