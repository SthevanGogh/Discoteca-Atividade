from app.models.musica_model import Musica
from app.repository.musica_repository import MusicaRepository
from app.repository.playlist_repository import PlaylistRepository


class MusicaService:
    def __init__(self):
        self.musica_repository = MusicaRepository()
        self.playlist_repository = PlaylistRepository()

    def get_all_musicas(self):
        return self.musica_repository.get_all_musicas()

    def get_musica_by_id(self, id):
        if not isinstance(id, int) or id <= 0:
            raise ValueError("O ID da música deve ser um número inteiro positivo.")
        musica = self.musica_repository.get_musica_by_id(id)
        if not musica:
            raise ValueError("Música não encontrada.")
        return musica

    def add_musica(self, musica: Musica):
        self.__validar_musica(musica)
        self.musica_repository.add_musica(musica)

    def update_musica(self, musica: Musica):
        if not musica.get_id():
            raise ValueError("A música deve ter um ID válido para ser atualizada.")
        self.__validar_musica(musica)
        self.musica_repository.update_musica(musica)

    def delete_musica(self, id):
        if not isinstance(id, int) or id <= 0:
            raise ValueError("O ID da música deve ser um número inteiro positivo.")

        playlists = self.playlist_repository.get_playlists_by_musica_id(id)
        if playlists:
            raise ValueError(
                f"Não é possível excluir a música pois ela está vinculada a playlist '{playlists[0]}'."
            )

        self.musica_repository.delete_musica(id)

    def __validar_musica(self, musica: Musica):
        if not musica.get_titulo() or not musica.get_titulo().strip():
            raise ValueError("O título da música é obrigatório.")
        if len(musica.get_titulo()) < 2:
            raise ValueError("O título da música não pode ter menos de 2 caracteres.")

        if not musica.get_artista() or not musica.get_artista().strip():
            raise ValueError("O artista é obrigatório.")
        if len(musica.get_artista()) < 2:
            raise ValueError("O nome do artista não pode ter menos de 2 caracteres.")
