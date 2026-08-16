from flask import Flask, render_template
import os

app = Flask(__name__)

livres = {
    1: {
        "titre": "Les bases de l’informatique et de la programmation",
        "auteur": "François Moraine",
        "categorie": "Programmation",
        "disponible": True,
        "lien": "https://www.mcours.net/cours/pdf/hasclic4/hasbnclic904.pdf"
    },
    2: {
        "titre": "Calcul différentiel et intégral",
        "auteur": "Jacques Douchet & Bruno Zwahlen",
        "categorie": "Mathématiques",
        "disponible": True,
        "lien": "https://www.epflpress.org/product/334/9782889155668/calcul-differentiel-et-integral"
    },
    3: {
        "titre": "Introduction à L'astrophysique",
        "auteur": "Frédéric Courbin",
        "categorie": "Physique",
        "disponible": True,
        "lien": "https://www.epflpress.org/product/774/9782832320006/introduction-a-l-astrophysique"
    },
    4: {
        "titre": "Communication numérique : Volume 1",
        "auteur": "Safwan El Assad et Dominique Barba",
        "categorie": "",
        "disponible": True,
        "lien": "https://dokumen.pub/communications-numeriques-volume-1-fondements-et-techniques-1784056693-9781784056698.html"
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
