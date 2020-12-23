from flask import Flask, redirect, url_for, render_template
from datetime import datetime

app = Flask(__name__)

# Context processors
@app.context_processor
def date_now():
    return {
        'now': datetime.utcnow()
    }

@app.route('/')
def index():

    edad = 30

    return render_template('index.html', 
                            edad=edad,
                            dato1='valor', 
                            dato2='valor2', 
                            lista= ["uno", "dos", "tres"])


@app.route('/informacion')
@app.route('/informacion/<string:nombre>')
@app.route('/informacion/<string:nombre>/<string:apellidos>')
def informacion(nombre = None, apellidos = None):

    texto = ""
    if nombre != None and apellidos != None:
        texto = f"Bienvenid@, {nombre} {apellidos}"

    return render_template('informacion.html', texto=texto)

@app.route('/contacto')
@app.route('/contacto/<redireccion>')
def contacto(redireccion = None):

    if redireccion is not None:
        return redirect(url_for('lenguajes'))

    return render_template('contacto.html')

@app.route('/lenguajes-de-programacion')
def lenguajes():
    return render_template('lenguajes.html')

if __name__ == '__main__':
    app.run(debug=True)
