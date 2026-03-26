from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Base de datos simulada (Lista de diccionarios)
catalogo = [
    {"id": 1, "titulo": "Back to the Future", "director": "Robert Zemeckis", "año": 1985},
    {"id": 2, "titulo": "The Matrix", "director": "Wachowskis", "año": 1999}
]

# --- R (Read): MOSTRAR EL CATÁLOGO ---
@app.route('/')
def index():
    return render_template('index.html', peliculas=catalogo)

# --- C (Create): AGREGAR PELÍCULA ---
@app.route('/agregar', methods=['POST'])
def agregar():
    nuevo_id = 1 if len(catalogo) == 0 else max(peli['id'] for peli in catalogo) + 1 
    titulo = request.form['titulo']
    director = request.form['director']
    año = request.form['año']
    
    nueva_peli = {"id": nuevo_id, "titulo": titulo, "director": director, "año": año}
    catalogo.append(nueva_peli)
    return redirect(url_for('index'))

# --- D (Delete): BORRAR PELÍCULA ---
@app.route('/eliminar/<int:id>')
def eliminar(id):
    global catalogo
    catalogo = [peli for peli in catalogo if peli['id'] != id]
    return redirect(url_for('index'))

# --- U (Update): MOSTRAR FORMULARIO DE EDICIÓN ---
@app.route('/editar/<int:id>')
def editar(id):
    peli_a_editar = None
    for peli in catalogo:
        if peli['id'] == id:
            peli_a_editar = peli
            break
            
    if peli_a_editar:
        return render_template('editar.html', peli=peli_a_editar)
    return redirect(url_for('index'))

# --- U (Update): GUARDAR CAMBIOS ---
@app.route('/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
    for peli in catalogo:
        if peli['id'] == id:
            peli['titulo'] = request.form['titulo']
            peli['director'] = request.form['director']
            peli['año'] = request.form['año']
            break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)