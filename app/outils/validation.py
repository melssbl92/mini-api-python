"""Fonctions de validation d'entrées courantes."""

import re


def email_valide(email: str) -> bool:
    """Valide une adresse email selon une règle simple adaptée au projet."""
    if not isinstance(email, str):
        raise ValueError("email doit être une chaîne")
    return bool(re.fullmatch(r"[^\s@]+@[^\s@]+\.[A-Za-z]{2,}", email))


def mdp_robuste(mot_de_passe: str) -> bool:
    """Exige 8 caractères, une minuscule, une majuscule, un chiffre et un symbole."""
    if not isinstance(mot_de_passe, str):
        raise ValueError("mot_de_passe doit être une chaîne")
    return (
        len(mot_de_passe) >= 8
        and re.search(r"[a-z]", mot_de_passe) is not None
        and re.search(r"[A-Z]", mot_de_passe) is not None
        and re.search(r"\d", mot_de_passe) is not None
        and re.search(r"[^A-Za-z0-9]", mot_de_passe) is not None
    )


def code_postal(code: str) -> bool:
    """Vérifie un code postal français métropolitain (5 chiffres)."""
    if not isinstance(code, str):
        raise ValueError("code doit être une chaîne")
    return bool(re.fullmatch(r"\d{5}", code))
