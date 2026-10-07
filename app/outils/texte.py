"""Fonctions de manipulation de texte."""

import unicodedata


def est_palindrome(texte: str) -> bool:
    """Vérifie un palindrome sans tenir compte de la casse ni des signes."""
    if not isinstance(texte, str):
        raise ValueError("texte doit être une chaîne")
    normalise = unicodedata.normalize("NFD", texte.casefold())
    lettres = "".join(c for c in normalise if c.isalnum())
    return lettres == lettres[::-1]


def compter_voyelles(texte: str) -> int:
    """Compte les voyelles, accents compris."""
    if not isinstance(texte, str):
        raise ValueError("texte doit être une chaîne")
    decomposé = unicodedata.normalize("NFD", texte.casefold())
    return sum(c in "aeiouy" for c in decomposé if unicodedata.category(c) != "Mn")


def inverser(texte: str) -> str:
    """Renvoie le texte dans l'ordre inverse."""
    if not isinstance(texte, str):
        raise ValueError("texte doit être une chaîne")
    return texte[::-1]
