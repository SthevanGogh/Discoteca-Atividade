from app.database.connection import get_db
from app.models.musica_model import Musica


class MusicaRepository:
    
    def get_all_musicas(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT id, titulo, artista, album, ano_lancamento FROM musica")
        rows = cursor.fetchall()
        return [{"id": row[0], "titulo": row[1], "artista": row[2], "album": row[3], "ano_lancamento": row[4]}
                for row in rows]


        
    def get_musica_by_id(self, id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM musica WHERE id = ?", (id,))
        row = cursor.fetchone()
        if row:
            return Musica(*row)
        return None
    
    def add_musica(self, musica):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO musica (titulo, artista, album, ano_lancamento) VALUES (?, ?, ?, ?)",
                       (musica.get_titulo(), musica.get_artista(), musica.get_album(), musica.get_ano_lancamento()))
        db.commit()
        # se precisar guardar o ID no objeto
        # musica.set_id(cursor.lastrowid)  # só funciona se você implementar um set_id no model
        return musica
    
    def update_musica(self, musica):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""UPDATE musica 
                          SET titulo = ?, artista = ?, album = ?, ano_lancamento = ? 
                          WHERE id = ?""",
                       (musica.get_titulo(), musica.get_artista(), musica.get_album(), musica.get_ano_lancamento(), musica.get_id()))
        db.commit()
        return musica
    
    def delete_musica(self, id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM musica WHERE id = ?", (id,))
        db.commit()
