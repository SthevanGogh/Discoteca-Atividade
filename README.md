# 🎶 Sistema de Playlists e Músicas  

Este projeto é um CRUD desenvolvido em **Flask + SQLite** para gerenciar **músicas** e organizá-las em **playlists**.  

## 📌 Entidades  

### 🎵 Música (`musica`)  
Representa uma faixa musical cadastrada no sistema.  
- **id** (PK) → Identificador único da música.  
- **titulo** → Nome da música.  
- **artista** → Nome do artista/banda.  
- **album** → Álbum de onde a música faz parte (opcional).  
- **ano_lancamento** → Ano em que a música foi lançada.  

---

### 📂 Playlist (`playlist`)  
Representa uma lista de músicas criada pelo usuário.  
- **id** (PK) → Identificador único da playlist.  
- **nome** → Nome da playlist.  
- **descricao** → Texto descritivo sobre a playlist.  

---

### 🔗 Relacionamento (`playlist_musica`)  
Tabela intermediária que relaciona **músicas e playlists** (muitos-para-muitos).  
- **id_playlist** (FK) → Referência para a playlist.  
- **id_musica** (FK) → Referência para a música.  

---

## 📊 Modelo Relacional  

- Uma **música** pode estar em **várias playlists**.  
- Uma **playlist** pode conter **várias músicas**.  
- O relacionamento é feito através da tabela **playlist_musica**.  

Exemplo:  
- A música *"Coisas Ruins"* pode estar em **Playlist de Tristeza** e também em **Clássicos do Tom Jobim**.  
- A playlist *"Favoritas"* pode ter músicas de vários artistas diferentes.  

---

## 🚀 Funcionalidades  

- ✅ CRUD de Músicas (criar, listar, editar, excluir).  
- ✅ CRUD de Playlists (criar, listar, editar, excluir).  
- ✅ Adição e remoção de músicas em playlists.  


### Rodar o projeto:

1. Criar ambiente virtual
    ```
    python -m venv venv
    ```
2. Ativar ambiente virtual
    ```
    source venv\Scripts\activate
    ```
   2.1. Atualizar o pip
   ```
    pip install --upgrade pip
    ```
3. Instalar o Flask
    ```
    pip install Flask
    ```
4. Executar o arquivo:
    ```
    python run.py
    ```
