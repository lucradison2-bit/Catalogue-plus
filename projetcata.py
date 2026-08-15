from flask import Flask, render_template
import os

app = Flask(__name__)

livres = {
    1: {
        "titre": "Automate the Boring Stuff",
        "auteur": "Al Sweigart",
        "categorie": "Programmation",
        "disponible": True,
        "lien": "https://automatetheboringstuff.com/"
    },
    2: {
        "titre": "Khan Academy — Mathématiques",
        "auteur": "Khan Academy",
        "categorie": "Mathématiques",
        "disponible": True,
        "lien": "https://www.khanacademy.org/math"
    },
    3: {
        "titre": "Khan Academy — Physique",
        "auteur": "Khan Academy",
        "categorie": "Physique",
        "disponible": True,
        "lien": "https://www.khanacademy.org/science/physics"
    },
    4: {
        "titre": "All About Circuits",
        "auteur": "AllAboutCircuits.com",
        "categorie": "Électricité",
        "disponible": True,
        "lien": "https://www.allaboutcircuits.com/textbook/"
    },
}

@app.route("/")
def accueil():
    return render_template("catalogue.html", livres=livres)

@app.route("/livre/<int:id_livre>")
def fiche_livre(id_livre):
    livre = livres.get(id_livre)
    if livre is None:
        return "Livre introuvable", 404
    return render_template("fiche.html", livre=livre, id_livre=id_livre)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
