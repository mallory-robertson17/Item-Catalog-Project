from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from musicalDBBuilder import Base, Actor, Musical, Character
app = Flask(__name__)

engine = create_engine('sqlite:///broadwaymusicals.db', connect_args={'check_same_thread':False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')

@app.route('/musical/<int:musical_id>/')
def getMusical(musical_id):
    m = session.query(Musical).filter_by(id=musical_id).first()
    c = session.query(Character).filter_by(musical_id=m.id)
    print c
    
    return render_template('musical.html', musical=m, characters=c)


@app.route('/musicals/')
def getAllMusicals():
    musicals = session.query(Musical)
    return render_template('Musicals.html', musicals=musicals)

@app.route('/musicals/new/', methods=['GET','POST'])
def newMusical():
    if request.method == 'POST':
        newMusical = Musical(name = request.form['name'], summary = request.form['summary'], year = request.form['year'])
        session.add(newMusical)
        session.commit()
        return redirect(url_for('newMusical'))
    else:
        return render_template('NewMusical.html')

@app.route('/musicals/edit/<int:musical_id>/', methods=['GET','PUT'])
def editMusical(musical_id):
    m = session.query(Musical).filter_by(id=musical_id).first()
    if request.method == 'PUT':
        m.name=request.form['name']
        m.summary = request.form['summary']
        m.year = request.form['year']
        session.add(m)
        session.commit()
        return redirect(url_for('musical', musical_id=musical_id))
    else:
        return render_template('EditMusical.html', musical=m)


@app.route('/actors/<int:actor_id>/')
def getActor(actor_id):
    a = session.query(Actor).filter_by(id=actor_id).first()
    c = session.query(Character).filter_by(actor_id=actor_id)
    return render_template('actor.html', actor=a, characters=c)


@app.route('/actors/')
def getAllActors():
    actors = session.query(Actor)
    message = ""
    for x in actors:
        message += "<html><body>" + x.name + "</body></html><br>"
    print message
    return message


@app.route('/actors/new/', methods=['GET','POST'])
def newActor():
    if request.method == 'POST':
        newActor = Actor(name = request.form['name'])
        session.add(newActor)
        session.commit()
        return redirect(url_for('newActor'))
    else:
        return render_template('NewActor.html')

@app.route('/characters/new/', methods=['GET','POST'])
def newCharacter():

    if request.method == 'POST':
        m = session.query(Musical).filter_by(id=request.form['musicalId']).first()
        a = session.query(Actor).filter_by(id=request.form['actorId']).first()
        newCharacter = Character(name = request.form['name'], actor=a, actor_id=request.form['actorId'], musical=m, musical_id=request.form['musicalId'])
        session.add(newCharacter)
        session.commit()
        return redirect(url_for('newCharacter'))

    else:
        m = session.query(Musical)
        a = session.query(Actor)
        return render_template('NewCharacter.html', musicals=m, actors=a)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
