class ManajerPerpustakaan:
    def __init__(self, penyimpanan_buku, penyimpanan_petugas):
        self.__penyimpanan_buku = penyimpanan_buku
        self.__penyimpanan_petugas = penyimpanan_petugas
        self.__daftar_buku = self.__penyimpanan_buku.muat_semua()
        self.__daftar_petugas = self.__penyimpanan_petugas.muat_semua()
    def login(self, username, password):
        petugas = self.__daftar_petugas.get(username)
        if petugas is not None and petugas.cek_password(password):
            return petugas
        return None
    def tambah_buku(self, buku):
        kode = buku.get_kode_buku()
        if kode in self.__daftar_buku:
            return False
        self.__daftar_buku[kode] = buku
        self.__penyimpanan_buku.simpan_semua(self.__daftar_buku)
        return True
    def cari_buku(self, kode_buku):
        return self.__daftar_buku.get(kode_buku.strip().upper())
    def perbarui_buku(self, kode_buku, judul, penulis, penerbit, tahun, stok):
        kode = kode_buku.strip().upper()
        buku = self.__daftar_buku.get(kode)
        if buku is None:
            return False
        buku.perbarui_detail(judul, penulis, penerbit, tahun, stok)
        self.__penyimpanan_buku.simpan_semua(self.__daftar_buku)
        return True
    def hapus_buku(self, kode_buku):
        kode = kode_buku.strip().upper()
        if kode not in self.__daftar_buku:
            return False
        del self.__daftar_buku[kode]
        self.__penyimpanan_buku.simpan_semua(self.__daftar_buku)
        return True
    def get_semua_buku(self):
        return list(self.__daftar_buku.values())
