from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from musicalDBBuilder import Base, Actor, Musical, Character
app = Flask(__name__)

engine = create_engine('sqlite:///broadwaymusicals.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/musicals')
def getMusicals():
    musicals = session.query(Musical)
    message = ""
    for x in musicals:
        message += "<html><body>" + x.name + "</body></html><br>"
    print message
    return message


@app.route('/actors')
def getActors():
    actors = session.query(Actor)
    message = ""
    for x in actors:
        message += "<html><body>" + x.name + "</body></html>"
    print message
    return message


@app.route('/characters')
def getCharacters():
    characters = session.query(Character)
    message = ""
    for x in characters:
        message += "<html><body>" + x.name + "</body></html>"
    print message
    return message


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
