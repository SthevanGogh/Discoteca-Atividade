from app import app
from flask import render_template, request, redirect, url_for

from app.service.musica_service import MusicaService
from app.models.musica_model import Musica
from app.service.playlist_service import PlaylistService
from app.models.playlist_model import Playlist

musica_service = MusicaService()
playlist_service = PlaylistService()

# ---------------------------
# ROTAS MÚSICAS
# ---------------------------

@app.route('/')
def index():
    return redirect(url_for('listar_musicas'))


@app.route('/musicas')
def listar_musicas():
    musicas = musica_service.get_all_musicas()
    return render_template('musicas/lista_musicas.html', musicas=musicas)


@app.route('/musicas/novo', methods=['GET', 'POST'])
def criar_musica():
    if request.method == 'POST':
        titulo = request.form['titulo']
        artista = request.form['artista']
        album = request.form['album']
        ano_lancamento = request.form['ano_lancamento']

        musica = Musica(None, titulo, artista, album, ano_lancamento)
        musica_service.add_musica(musica)

        return redirect(url_for('listar_musicas'))

    return render_template('musicas/formulario_musicas.html')


@app.route('/musicas/editar/<int:id>', methods=['GET', 'POST'])
def editar_musica(id):
    musica = musica_service.get_musica_by_id(id)
    if request.method == 'POST':
        musica.set_titulo(request.form['titulo'])
        musica.set_artista(request.form['artista'])
        musica.set_album(request.form['album'])
        musica.set_ano_lancamento(request.form['ano_lancamento'])

        musica_service.update_musica(musica)

        return redirect(url_for('listar_musicas'))

    return render_template('musicas/formulario_musicas.html', musica=musica)


@app.route('/musicas/excluir/<int:id>')
def deletar_musica(id):
    musica_service.delete_musica(id)
    return redirect(url_for('listar_musicas'))

# ---------------------------
# ROTAS PLAYLISTS
# ---------------------------

@app.route('/playlists')
def listar_playlists():
    playlists = playlist_service.get_all_playlists()
    return render_template('playlists/lista_playlists.html', playlists=playlists)


@app.route("/playlists/novo", methods=["GET", "POST"])
def criar_playlist():
    if request.method == "POST":
        nome = request.form["nome"]
        descricao = request.form["descricao"]
        musicas_ids = request.form.getlist("musicas")

        playlist = Playlist(id=None, nome=nome, descricao=descricao)
        playlist_service.add_playlist(playlist, musicas_ids)

        return redirect(url_for("listar_playlists"))

    musicas = musica_service.get_all_musicas()
    return render_template("playlists/formulario_playlists.html", 
                           playlist=None, 
                           musicas=musicas, 
                           musicas_selecionadas=[])  # ✅


@app.route('/playlists/editar/<int:id>', methods=['GET', 'POST'])
def editar_playlist(id):
    playlist = playlist_service.get_playlist_by_id(id)
    if request.method == 'POST':
        playlist.set_nome(request.form['nome'])
        playlist.set_descricao(request.form['descricao'])
        musicas_ids = [int(m) for m in request.form.getlist('musicas')]
        playlist_service.update_playlist(playlist, musicas_ids)
        return redirect(url_for('listar_playlists'))

    musicas = musica_service.get_all_musicas()
    # garante que a lista seja de ints
    musicas_selecionadas = [m.get_id() for m in playlist.get_musicas()]
    return render_template('playlists/formulario_playlists.html',
                           playlist=playlist,
                           musicas=musicas,
                           musicas_selecionadas=musicas_selecionadas)



@app.route('/playlists/excluir/<int:id>')
def deletar_playlist(id):
    playlist_service.delete_playlist(id)
    return redirect(url_for('listar_playlists'))
