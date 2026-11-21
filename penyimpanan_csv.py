from buku import Buku
from petugas import Petugas


class PenyimpananCsv:
    def __init__(self, path_file, fieldnames, key_field, jenis):
        self.__path_file = path_file
        self.__fieldnames = fieldnames
        self.__key_field = key_field
        self.__jenis = jenis

    def muat_semua(self):
        data_hasil = {}
        try:
            with open(self.__path_file, "r", encoding="utf-8") as file:
                baris_header = file.readline().strip()
                if baris_header == "":
                    return data_hasil

                header = baris_header.split(",")

                for baris in file:
                    baris_bersih = baris.strip()
                    if baris_bersih == "":
                        continue

                    nilai = baris_bersih.split(",")
                    data_dict = {}
                    for i in range(len(header)):
                        data_dict[header[i]] = nilai[i]

                    if self.__jenis == "buku":
                        objek = Buku(
                            data_dict["kode_buku"],
                            data_dict["judul"],
                            data_dict["penulis"],
                            data_dict["penerbit"],
                            int(data_dict["tahun_terbit"]),
                            int(data_dict["stok"]),
                        )
                    elif self.__jenis == "petugas":
                        objek = Petugas(
                            data_dict["id_petugas"],
                            data_dict["nama"],
                            data_dict["username"],
                            data_dict["password"],
                        )

                    key = data_dict[self.__key_field]
                    if self.__jenis == "buku":
                        key = key.upper()
                    data_hasil[key] = objek

        except FileNotFoundError:
            pass

        return data_hasil

    def simpan_semua(self, data):
        with open(self.__path_file, "w", encoding="utf-8") as file:
            header = ",".join(self.__fieldnames)
            file.write(header + "\n")

            for objek in data.values():
                data_dict = objek.to_dict()
                baris_list = []
                for kolom in self.__fieldnames:
                    baris_list.append(str(data_dict[kolom]))

                baris_teks = ",".join(baris_list)
                file.write(baris_teks + "\n")
