import sqlite3
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Song
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        song = request.form.get('song')

        if len(song) < 1:
            flash('Song is too short!', category='error') 
        else:
            new_song = Song(data=song, user_id=current_user.id) 
            db.session.add(new_song) 
            db.session.commit()
            flash('Song added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/my_library')
def my_library():
    return render_template("my_library.html", user=current_user)


@views.route('/all_songs')
def all_songs():
    conn = sqlite3.connect('instance/database.db')
    cursor = conn.cursor()
    # Fetch data from the database
    cursor.execute('SELECT * FROM Song')
    data = cursor.fetchall()
    # Close the database connection
    conn.close()
    # Render the template with the data
    return render_template("all_songs.html", user=current_user, data=data)


@views.route('/add_song', methods=['GET', 'POST'])
def add_song():
    if request.method == 'POST':
        song = request.form.get('song')

        title = request.form.get('title')
        artist = request.form.get('artist')

        if len(song) < 1:
            flash('Song is too short!', category='error')
        elif len(title) < 1:
            flash('There is no title, please include a title!', category='error')
        elif len(artist) < 1:
            flash('There is no artist, please include an artist!', category='error')
        else:
            new_song = Song(data=song, title=title, artist=artist, user_id=current_user.id)
            db.session.add(new_song)
            db.session.commit()
            flash(f'Song added! this song has title: {title} and artist: {artist}', category='success')

    return render_template("add_song.html", user=current_user)


@views.route('/delete-song', methods=['POST'])
def delete_song():  
    song = json.loads(request.data)
    songId = song['songId']
    song = Song.query.get(songId)
    if song:
        if song.user_id == current_user.id:
            db.session.delete(song)
            db.session.commit()

    return jsonify({})


@views.route('/song_details/<int:song_id>', methods=['GET', 'POST'])
def song_details(song_id):
    song = Song.query.get(song_id)
    print(f"hello: {song}")
    return render_template("song_details.html", user=current_user, song=song)


def add_new_song():
    return render_template("home.html", user=current_user)

