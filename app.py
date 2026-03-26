from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

catalogo = [
    {"id": 1, "titulo": "Back to the Future", "director": "Robert Zemeckis", "año": 1985},
    {"id": 2, "titulo": "The Matrix", "director": "Wachowskis", "año": 1999}
]

@app.route('/')
def index():
    return render_template('index.html', peliculas=catalogo)

# --- NUEVA RUTA PARA CREAR ---
@app.route('/agregar', methods=['POST'])
def agregar():
    # Calculamos un ID nuevo falso sumando 1 al tamaño de la lista
    nuevo_id = len(catalogo) + 1 
    # Atrapamos los datos del formulario HTML
    titulo = request.form['titulo']
    director = request.form['director']
    año = request.form['año']
    
    # Armamos el nuevo diccionario y lo metemos a la lista
    nueva_peli = {"id": nuevo_id, "titulo": titulo, "director": director, "año": año}
    catalogo.append(nueva_peli)
    
    # Recargamos la página de inicio para ver los cambios
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)