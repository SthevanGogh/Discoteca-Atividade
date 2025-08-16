from app.models.playlist_model import Playlist
from app.repository.playlist_repository import PlaylistRepository
from app.repository.musica_repository import MusicaRepository


class PlaylistService:
    def __init__(self):
        self.playlist_repository = PlaylistRepository()
        self.musica_repository = MusicaRepository()

    def get_all_playlists(self):
        return self.playlist_repository.get_all_playlists()

    def get_playlist_by_id(self, id):
        if not isinstance(id, int) or id <= 0:
            raise ValueError("O ID da playlist deve ser um número inteiro positivo.")
        playlist = self.playlist_repository.get_playlist_by_id(id)
        if not playlist:
            raise ValueError("Playlist não encontrada.")
        return playlist

    def add_playlist(self, playlist, musicas_ids):
        if not musicas_ids:
            raise ValueError("A playlist deve ter pelo menos uma música.")
        self.playlist_repository.add_playlist(playlist, [int(mid) for mid in musicas_ids])


    def update_playlist(self, playlist: Playlist, musicas_ids):
        if not playlist.get_id():
            raise ValueError("A playlist deve ter um ID válido para ser atualizada.")
        
        # garante que as músicas da request sejam refletidas no objeto
        playlist.set_musicas(musicas_ids)

        # valida dados
        self.__validar_playlist(playlist)

        # atualiza no banco
        self.playlist_repository.update_playlist(playlist, [int(mid) for mid in musicas_ids])



    def delete_playlist(self, id):
        if not isinstance(id, int) or id <= 0:
            raise ValueError("O ID da playlist deve ser um número inteiro positivo.")
        self.playlist_repository.delete_playlist(id)

    def __validar_playlist(self, playlist: Playlist):
        if not playlist.get_nome() or not playlist.get_nome().strip():
            raise ValueError("O nome da playlist é obrigatório.")
        if len(playlist.get_nome()) < 3:
            raise ValueError("O nome da playlist não pode ter menos de 3 caracteres.")

        # ✅ Agora validamos uma lista de músicas
        if not playlist.get_musicas() or len(playlist.get_musicas()) == 0:
            raise ValueError("A playlist deve conter pelo menos uma música.")

        for musica_id in playlist.get_musicas():
            if not isinstance(musica_id, int) or musica_id <= 0:
                raise ValueError(f"O id {musica_id} de música é inválido.")
            musica = self.musica_repository.get_musica_by_id(musica_id)
            if not musica:
                raise ValueError(f"A música com id {musica_id} não existe.")
