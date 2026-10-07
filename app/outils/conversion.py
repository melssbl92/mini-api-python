"""Fonctions de conversion."""

import math


def _valider_nombre(valeur: float, nom: str) -> float:
    if isinstance(valeur, bool) or not isinstance(valeur, (int, float)):
        raise ValueError(f"{nom} doit être un nombre")
    if not math.isfinite(valeur):
        raise ValueError(f"{nom} doit être fini")
    return float(valeur)


def celsius_fahrenheit(celsius: float) -> float:
    """Convertit une température Celsius en Fahrenheit."""
    celsius = _valider_nombre(celsius, "celsius")
    return round(celsius * 9 / 5 + 32, 2)


def km_miles(kilometres: float) -> float:
    """Convertit des kilomètres en miles."""
    kilometres = _valider_nombre(kilometres, "kilometres")
    if kilometres < 0:
        raise ValueError("kilometres doit être positif ou nul")
    return round(kilometres * 0.621371, 2)


def euros_devise(euros: float, taux: float) -> float:
    """Convertit des euros selon le taux fourni (unités de devise par euro)."""
    euros = _valider_nombre(euros, "euros")
    taux = _valider_nombre(taux, "taux")
    if euros < 0:
        raise ValueError("euros doit être positif ou nul")
    if taux <= 0:
        raise ValueError("taux doit être strictement positif")
    return round(euros * taux, 2)
