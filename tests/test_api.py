from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_sante():
    response = client.get("/sante")
    assert response.status_code == 200
    assert response.json() == {"etat": "ok"}


def test_routes_math_et_erreur():
    assert client.get("/factorielle/5").json()["resultat"] == 120
    assert client.get("/est_premier/1").json()["resultat"] is False
    assert client.get("/pgcd/54/24").json()["resultat"] == 6
    assert client.get("/factorielle/-2").status_code == 400
    assert client.get("/pgcd/a/2").status_code == 400


def test_routes_texte_et_parametre_manquant():
    assert client.get("/est_palindrome", params={"texte_entree": "kayak"}).json()["resultat"]
    assert client.get("/compter_voyelles", params={"texte_entree": "été"}).json()["resultat"] == 2
    assert client.get("/inverser", params={"texte_entree": "abc"}).json()["resultat"] == "cba"
    assert client.get("/inverser").status_code == 400


def test_routes_conversion():
    assert client.get("/celsius_fahrenheit/0").json()["resultat"] == 32
    assert client.get("/km_miles/10").json()["resultat"] == 6.21
    assert client.get("/euros_devise/10", params={"taux": 1.1}).json()["resultat"] == 11
    assert client.get("/km_miles/-1").status_code == 400


def test_routes_validation():
    assert client.get("/email_valide", params={"email": "x@y.fr"}).status_code == 200
    assert client.get("/mdp_robuste", params={"mot_de_passe": "Abcdef1!"}).status_code == 200
    assert client.get("/code_postal/75001").status_code == 200
    assert client.get("/email_valide", params={"email": "pas-un-email"}).status_code == 400
    assert client.get("/mdp_robuste", params={"mot_de_passe": "faible"}).status_code == 400
    assert client.get("/code_postal/75A01").status_code == 400
