from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    # Servicio externo (API pública)
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    # Parsear a JSON
    usuarios = response.json()

    # Enviar datos a la página HTML
    return render_template("index.html", usuarios=usuarios)

if __name__ == "__main__":
    app.run(debug=True)
