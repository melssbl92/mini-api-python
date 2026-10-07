# Mini API Python

API REST de petits outils en Python : mathématiques, texte, conversions et validations. Les entrées invalides renvoient HTTP 400.

[![CI](https://github.com/melssbl92/mini-api-python/actions/workflows/ci.yml/badge.svg)](https://github.com/melssbl92/mini-api-python/actions/workflows/ci.yml)

## Prérequis

- Python 3.12 ou supérieur
- pip
- Docker (facultatif, pour lancer l'image)

## Installation et lancement local

```bash
git clone https://github.com/melssbl92/mini-api-python.git
cd mini-api-python
python -m venv .venv
source .venv/bin/activate        # Windows : .venv\Scripts\activate
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

L'API est disponible sur <http://127.0.0.1:8000>. La documentation interactive se trouve sur <http://127.0.0.1:8000/docs>.

## Routes

Toutes les réponses réussies sont des objets JSON avec le résultat dans `resultat`.

| Fonction | Requête exemple | Résultat |
|---|---|---|
| Factorielle | `GET /factorielle/5` | `120` |
| Nombre premier | `GET /est_premier/13` | `true` |
| PGCD | `GET /pgcd/54/24` | `6` |
| Palindrome | `GET /est_palindrome?texte_entree=kayak` | `true` |
| Compter les voyelles | `GET /compter_voyelles?texte_entree=bonjour` | `3` |
| Inverser | `GET /inverser?texte_entree=salut` | `tulas` |
| Celsius vers Fahrenheit | `GET /celsius_fahrenheit/20` | `68.0` |
| Kilomètres vers miles | `GET /km_miles/10` | `6.21` |
| Euros vers une devise | `GET /euros_devise/10?taux=1.1` | `11.0` |
| Valider un email | `GET /email_valide?email=lea%40example.fr` | `true` |
| Robustesse d'un mot de passe | `GET /mdp_robuste?mot_de_passe=BonMotDePasse1%21` | `true` |
| Code postal français | `GET /code_postal/75001` | `true` |
| Santé | `GET /sante` | `{"etat":"ok"}` |

La conversion euros/devise utilise le paramètre `taux` fourni par l'appelant (unités de devise pour un euro) ; aucun taux externe n'est récupéré. Le vérificateur de mot de passe exige au moins 8 caractères, une minuscule, une majuscule, un chiffre et un symbole. Le code postal accepte cinq chiffres.

Une valeur mal formée, manquante ou invalide renvoie HTTP 400 avec un champ `detail`.

## Lancer avec Docker

```bash
docker build -t mini-api-python .
docker run --rm -p 8000:8000 mini-api-python
```

Au tag `v*`, GitHub Actions construit et publie l'image sur `ghcr.io/<propriétaire>/mini-api-python:<tag>`. Pour publier la version du sujet :

```bash
git tag v1.0.0
git push origin v1.0.0
```

Le workflow nécessite l'autorisation `packages: write` (déjà déclarée) et publie avec `GITHUB_TOKEN`.

## Tests et qualité

```bash
ruff check .
pytest --cov=app --cov-report=term-missing --cov-fail-under=80
```

GitHub Actions exécute ces vérifications pour chaque push et pull request ; la couverture minimale est de 80 %.

## Contribuer

Suivre GitHub Flow : ouvrir une issue, créer une branche `type/numero-description` depuis `main`, faire des commits atomiques au format Conventional Commits, pousser la branche et ouvrir une pull request vers `main`. Demander une revue à une autre personne et attendre la CI verte avant la fusion. Le modèle de PR et le modèle d'issue sont dans `.github/`.

Pour un dépôt d'équipe, activer dans GitHub les règles de protection de `main` (PR obligatoire, approbation, CI verte, branche à jour, interdiction du force push et de la suppression). Les avis de revue et contributions doivent être réalisés par les membres concernés.

## Licence

Distribué sous licence MIT ; voir [LICENSE](LICENSE).
