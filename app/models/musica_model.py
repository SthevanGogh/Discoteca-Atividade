class Musica:
    def __init__(self, id, titulo, artista, album, ano_lancamento):
        self.__id = id
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album
        self.__ano_lancamento = ano_lancamento

    # GETTERS
    def get_id(self):
        return self.__id

    def get_titulo(self):
        return self.__titulo
    
    def get_artista(self):
        return self.__artista

    def get_album(self):
        return self.__album

    def get_ano_lancamento(self):
        return self.__ano_lancamento

    # SETTERS
    def set_id(self, id):
        self.__id = id

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_artista(self, artista):
        self.__artista = artista

    def set_album(self, album):
        self.__album = album

    def set_ano_lancamento(self, ano_lancamento):
        self.__ano_lancamento = ano_lancamento
