from penyimpanan_csv import PenyimpananCsv
from manajer_perpustakaan import ManajerPerpustakaan
from aplikasi_perpustakaan import AplikasiPerpustakaan
if __name__ == "__main__":
    kolom_buku = ["kode_buku", "judul", "penulis", "penerbit", "tahun_terbit", "stok"]
    kolom_petugas = ["id_petugas", "nama", "username", "password"]
    penyimpanan_buku = PenyimpananCsv(
        path_file="data/data_buku.csv",
        fieldnames=kolom_buku,
        key_field="kode_buku",
        jenis="buku",
    )

    penyimpanan_petugas = PenyimpananCsv(
        path_file="data/data_petugas.csv",
        fieldnames=kolom_petugas,
        key_field="username",
        jenis="petugas",
    )

    manajer = ManajerPerpustakaan(penyimpanan_buku, penyimpanan_petugas)
    aplikasi = AplikasiPerpustakaan(manajer)
    aplikasi.jalankan()
