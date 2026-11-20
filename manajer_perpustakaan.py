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
