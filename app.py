from flask import Flask, render_template

app = Flask(__name__)

# Base de datos simulada (Lista de diccionarios)
catalogo = [
    {"id": 1, "titulo": "Back to the Future", "director": "Robert Zemeckis", "año": 1985},
    {"id": 2, "titulo": "The Matrix", "director": "Wachowskis", "año": 1999}
]

@app.route('/')
def index():
    # Mandamos el catálogo al HTML usando Jinja2
    return render_template('index.html', peliculas=catalogo)

if __name__ == '__main__':
    app.run(debug=True)