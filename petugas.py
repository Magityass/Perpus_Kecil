class Petugas:
    def __init__(self, id_petugas, nama, username, password):
        self.__id_petugas = id_petugas
        self.__nama = nama
        self.__username = username
        self.__password = password

    def get_nama(self):
        return self.__nama

    def get_username(self):
        return self.__username

    def cek_password(self, password):
        return self.__password == password

    def to_dict(self):
        return {
            "id_petugas": self.__id_petugas,
            "nama": self.__nama.replace(",", " "),
            "username": self.__username,
            "password": self.__password,
        }
