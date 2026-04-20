# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import hashlib

app = Flask(__name__)

def chiffrer(texte, cle):
    res = ""
    cle = ((cle % 26) + 26) % 26
    for c in texte:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            res += chr((ord(c) - base + cle) % 26 + base)
        else:
            res += c
    return res

def dechiffrer(texte, cle):
    return chiffrer(texte, -cle)

def sha256(texte):
    return hashlib.sha256(texte.encode()).hexdigest()

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""

    if request.method == "POST":
        texte1 = request.form.get("texte1")
        texte2 = request.form.get("texte2")
        cle = request.form.get("cle")
        action = request.form.get("action")

        if action == "chiffrer1":
            result = "Texte 1 chiffré : " + chiffrer(texte1, int(cle))

        elif action == "chiffrer2":
            result = "Texte 2 chiffré : " + chiffrer(texte2, int(cle))

        elif action == "sha1":
            result = "SHA-256 Texte 1 : " + sha256(texte1)

        elif action == "sha2":
            result = "SHA-256 Texte 2 : " + sha256(texte2)

        elif action == "comparer":
            if sha256(texte1) == sha256(texte2):
                result = "Identiques"
            else:
                result = " Différents"

        elif action == "chiffrer_both":
            r1 = chiffrer(texte1, int(cle))
            r2 = chiffrer(texte2, int(cle))

            result = f"""
            Texte 1 chiffré : {r1}<br>
            Texte 2 chiffré : {r2}
            """

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)