from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from musicalDBBuilder import Base, Actor, Musical, Character
app = Flask(__name__)

engine = create_engine('sqlite:///broadwaymusicals.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')

@app.route('/musicals/<int:musical_id>/')
def getMusical(musical_id):
    m = session.query(Musical).filter_by(id=musical_id).first()
    c = session.query(Character).filter_by(musical_id=m.id)
    print c
    
    return render_template('musical.html', musical=m, characters=c)


@app.route('/musicals/')
def getAllMusicals():
    musicals = session.query(Musical)
    message = ""
    for x in musicals:
        message += "<html><body>" + x.name + "</body></html><br>"
    print message
    return message


@app.route('/actors/<int:actor_id>/')
def getActor(actor_id):
    a = session.query(Actor).filter_by(id=actor_id)
    c = session.query(Character).filter_by(actor_id=actor_id)
    return render_template('actor.html', actor=a, characters=c)


@app.route('/characters/<int:character_id>/')
def getCharacters(character_id):
    characters = session.query(Character)
    message = ""
    for x in characters:
        message += "<html><body>" + x.name + "</body></html>"
    print message
    return message


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
