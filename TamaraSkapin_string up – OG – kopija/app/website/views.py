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
