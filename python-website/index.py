from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import database

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    #database.createDataBase()
    if request.method == 'POST':
        nombre = request.form['nombre']
        tema = request.form['fecha']
        fecha = request.form['tema']
        meet = request.form['meet']
        database.insertResults(nombre, tema, fecha,  meet)
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('about'))
    return render_template('home.html', test='Prueba')

@app.route('/about')
def about():
    nombre = database.consulta("NOMBRE")
    tema = database.consulta("TEMA")
    fecha = database.consulta("FECHA")
    meet = database.consulta("MEET")
    eventos = {'Nombre' : nombre, 'Tema' : tema, 'Fecha' : fecha, 'Meet' : meet}
    df = pd.DataFrame(data=eventos)
    #df = pd.DataFrame(data=eventos, index=indices)
    eventTable = str(df.to_html())
    eventTable = eventTable.replace('dataframe', 'tablepers')
    eventTable = eventTable.replace('right', 'center')
    return render_template('about.html', itinerario=eventTable)

if __name__ == '__main__':
    app.run(debug=True)