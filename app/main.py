"""Application FastAPI des petits outils."""

from __future__ import annotations

from fastapi import FastAPI

from app.erreurs import enregistrer_gestionnaires
from app.outils import conversion, math, texte, validation

app = FastAPI(
    title="Mini API Python",
    description="Petits outils de mathématiques, texte, conversion et validation.",
    version="1.0.0",
)
enregistrer_gestionnaires(app)


@app.get("/sante")
def sante() -> dict:
    """Retourne l'état de fonctionnement de l'API."""
    return {"etat": "ok"}


@app.get("/factorielle/{n}")
def route_factorielle(n: int) -> dict:
    return {"n": n, "resultat": math.factorielle(n)}


@app.get("/est_premier/{n}")
def route_est_premier(n: int) -> dict:
    return {"n": n, "resultat": math.est_premier(n)}


@app.get("/pgcd/{a}/{b}")
def route_pgcd(a: int, b: int) -> dict:
    return {"a": a, "b": b, "resultat": math.pgcd(a, b)}


@app.get("/est_palindrome")
def route_est_palindrome(texte_entree: str) -> dict:
    return {"texte": texte_entree, "resultat": texte.est_palindrome(texte_entree)}


@app.get("/compter_voyelles")
def route_compter_voyelles(texte_entree: str) -> dict:
    return {"texte": texte_entree, "resultat": texte.compter_voyelles(texte_entree)}


@app.get("/inverser")
def route_inverser(texte_entree: str) -> dict:
    return {"texte": texte_entree, "resultat": texte.inverser(texte_entree)}


@app.get("/celsius_fahrenheit/{celsius}")
def route_celsius_fahrenheit(celsius: float) -> dict:
    return {"celsius": celsius, "resultat": conversion.celsius_fahrenheit(celsius)}


@app.get("/km_miles/{kilometres}")
def route_km_miles(kilometres: float) -> dict:
    return {"kilometres": kilometres, "resultat": conversion.km_miles(kilometres)}


@app.get("/euros_devise/{euros}")
def route_euros_devise(euros: float, taux: float) -> dict:
    return {"euros": euros, "taux": taux, "resultat": conversion.euros_devise(euros, taux)}


@app.get("/email_valide")
def route_email_valide(email: str) -> dict:
    valide = validation.email_valide(email)
    if not valide:
        raise ValueError("email invalide")
    return {"email": email, "resultat": True}


@app.get("/mdp_robuste")
def route_mdp_robuste(mot_de_passe: str) -> dict:
    robuste = validation.mdp_robuste(mot_de_passe)
    if not robuste:
        raise ValueError("mot de passe trop faible")
    return {"resultat": True}


@app.get("/code_postal/{code}")
def route_code_postal(code: str) -> dict:
    valide = validation.code_postal(code)
    if not valide:
        raise ValueError("code postal invalide (5 chiffres attendus)")
    return {"code": code, "resultat": True}
