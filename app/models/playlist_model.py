class Playlist:
    def __init__(self, id, nome, descricao, musicas=None):
        self.__id = id
        self.__nome = nome
        self.__descricao = descricao
        # lista de ids de músicas
        self.__musicas = musicas if musicas is not None else []

    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome
    
    def get_descricao(self):
        return self.__descricao
    
    def get_musicas(self):
        return self.__musicas
    
    def get_musicas_ids(self):
        return [m.get_id() for m in self.__musicas]
    
    def set_nome(self, nome):
        self.__nome = nome

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def set_musicas(self, musicas):
        self.__musicas = musicas
