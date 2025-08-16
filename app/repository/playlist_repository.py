from app.database.connection import get_db
from app.models.playlist_model import Playlist
from app.models.musica_model import Musica


class PlaylistRepository:

    def get_all_playlists(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
            SELECT p.id, p.nome, p.descricao
            FROM playlist p
        """)
        rows = cursor.fetchall()
        playlists = []
        for row in rows:
            playlist = Playlist(id=row[0], nome=row[1], descricao=row[2])
            # buscar músicas associadas
            playlist.musicas = self.get_musicas_by_playlist(row[0])
            playlists.append(playlist)
        return playlists


    def get_playlist_by_id(self, id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
            SELECT p.id, p.nome, p.descricao
            FROM playlist p
            WHERE p.id = ?
        """, (id,))
        row = cursor.fetchone()
        if row:
            playlist = Playlist(id=row[0], nome=row[1], descricao=row[2])
            playlist.set_musicas(self.get_musicas_by_playlist(row[0]))
            return playlist
        return None

    def add_playlist(self, playlist, musicas_ids):
        db = get_db()
        cursor = db.cursor()

        # cria a playlist
        cursor.execute(
            "INSERT INTO playlist (nome, descricao) VALUES (?, ?)",
            (playlist.get_nome(), playlist.get_descricao())
        )
        playlist_id = cursor.lastrowid

        # associa músicas selecionadas
        for musica_id in musicas_ids:
            cursor.execute(
                "INSERT INTO playlist_musicas (id_playlist, id_musica) VALUES (?, ?)",
                (playlist_id, musica_id)
            )

        db.commit()

    def update_playlist(self, playlist, musicas_ids):
        db = get_db()
        cursor = db.cursor()

        # atualiza dados básicos da playlist
        cursor.execute("""
            UPDATE playlist 
            SET nome = ?, descricao = ?
            WHERE id = ?
        """, (playlist.get_nome(), playlist.get_descricao(), playlist.get_id()))

        # remove vínculos antigos
        cursor.execute("DELETE FROM playlist_musicas WHERE id_playlist = ?", (playlist.get_id(),))

        # adiciona novos vínculos
        for musica_id in musicas_ids:
            cursor.execute(
                "INSERT INTO playlist_musicas (id_playlist, id_musica) VALUES (?, ?)",
                (playlist.get_id(), musica_id)
            )

        db.commit()

    def delete_playlist(self, id):
        db = get_db()
        cursor = db.cursor()
        # primeiro remove vínculos
        cursor.execute("DELETE FROM playlist_musicas WHERE id_playlist = ?", (id,))
        # depois remove a playlist
        cursor.execute("DELETE FROM playlist WHERE id = ?", (id,))
        db.commit()

    def get_playlists_by_musica_id(self, id_musica):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
            SELECT p.nome
            FROM playlist p
            JOIN playlist_musicas pm ON p.id = pm.id_playlist
            WHERE pm.id_musica = ?
        """, (id_musica,))
        rows = cursor.fetchall()
        return [row[0] for row in rows] if rows else []

    def add_musica_to_playlist(self, playlist_id, musica_id):
        query = "INSERT INTO playlist_musicas (id_playlist, id_musica) VALUES (?, ?)"
        conn = get_db()
        conn.execute(query, (playlist_id, musica_id))
        conn.commit()

    def get_musicas_by_playlist(self, playlist_id):
        query = """
            SELECT m.id, m.titulo, m.artista, m.album, m.ano_lancamento
            FROM musica m
            JOIN playlist_musicas pm ON m.id = pm.id_musica
            WHERE pm.id_playlist = ?
        """
        cur = get_db().cursor()
        cur.execute(query, (playlist_id,))
        rows = cur.fetchall()
        return [Musica(id=row[0], titulo=row[1], artista=row[2], album=row[3], ano_lancamento=row[4]) for row in rows]
