-- Criação da tabela de músicas
CREATE TABLE musica (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    artista TEXT NOT NULL,
    album TEXT,
    ano_lancamento INTEGER NOT NULL
);

-- Criação da tabela de playlists
CREATE TABLE playlist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT
);

CREATE TABLE playlist_musicas (
    id_playlist INTEGER,
    id_musica INTEGER,
    FOREIGN KEY (id_playlist) REFERENCES playlist (id) ON DELETE CASCADE,
    FOREIGN KEY (id_musica) REFERENCES musica (id) ON DELETE CASCADE,
    PRIMARY KEY (id_playlist, id_musica)
);

