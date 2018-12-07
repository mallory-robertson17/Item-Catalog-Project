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
    
    return render_template('musical.html', musical=m)


@app.route('/musicals/')
def getAllMusicals():
    musicals = session.query(Musical)
    message = ""
    for x in musicals:
        message += "<html><body>" + x.name + "</body></html><br>"
    print message
    return message


@app.route('/actors/<int:actor_id>/')
def getActors(actor_id):
    actors = session.query(Actor)
    message = ""
    for x in actors:
        message += "<html><body>" + x.name + "</body></html>"
    print message
    return message


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
