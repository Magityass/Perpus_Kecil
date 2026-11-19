from buku import Buku
from petugas import Petugas

class PenyimpananCsv:
    def __init__(self, path_file, fieldnames, key_field, jenis):
        self.__path_file = path_file
        self.__fieldnames = fieldnames
        self.__key_field = key_field
        self.__jenis = jenis
