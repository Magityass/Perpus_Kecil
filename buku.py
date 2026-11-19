class Buku:
    def __init__(self, kode_buku, judul, penulis, penerbit, tahun_terbit, stok):
        self.__kode_buku = kode_buku.strip().upper()
        self.__judul = judul
        self.__penulis = penulis
        self.__penerbit = penerbit
        self.__tahun_terbit = int(tahun_terbit)
        self.__stok = int(stok)

    def get_kode_buku(self):
        return self.__kode_buku

    def get_judul(self):
        return self.__judul

    def get_penulis(self):
        return self.__penulis

    def get_penerbit(self):
        return self.__penerbit

    def get_tahun_terbit(self):
        return self.__tahun_terbit

    def get_stok(self):
        return self.__stok

    def tambah_stok(self, jumlah):
        if jumlah > 0:
            self.__stok += jumlah

    def kurangi_stok(self, jumlah):
        if 0 < jumlah <= self.__stok:
            self.__stok -= jumlah
            return True
        return False

    def perbarui_detail(self, judul, penulis, penerbit, tahun_terbit, stok):
        self.__judul = judul
        self.__penulis = penulis
        self.__penerbit = penerbit
        self.__tahun_terbit = int(tahun_terbit)
        self.__stok = int(stok)

    def to_dict(self):
        return {
            "kode_buku": self.__kode_buku,
            "judul": self.__judul.replace(",", " "),
            "penulis": self.__penulis.replace(",", " "),
            "penerbit": self.__penerbit.replace(",", " "),
            "tahun_terbit": self.__tahun_terbit,
            "stok": self.__stok,
        }
