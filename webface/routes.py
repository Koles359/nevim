from . import app
from flask import render_template
from flask import request


@app.route('/')
def index():
    pi=3.141519
    e=2.7
    title = 'Index'
    text = "<h1>Nadpis</h1>"
    return render_template('base.html.j2', pi=pi, title=title)


@app.route('/info/')
def info():
    title = 'Info'
    x = request.args.get("x")
    y = request.args.get("y")
    try:
        z = int(x) + int(y)
    except (TypeError, ValueError):
        z = ""
    return render_template('info.html.j2', title=title)


@app.route('/Květák/')
def Květák():
    title = 'Květák'
    return render_template('květák.html.j2', title=title)


@app.route('/Kapusta/')
def Kapusta():
    title = 'Kapusta'
    return render_template('kapusta.html.j2', title=title)


@app.route('/Banány/')
def Banány():
    title = 'Banány'
    return render_template('banány.html.j2', title=title)
