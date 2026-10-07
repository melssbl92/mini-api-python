"""Fonctions mathématiques de l'API."""


def factorielle(n: int) -> int:
    """Calcule n! pour un entier positif ou nul."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise ValueError("n doit être un entier")
    if n < 0:
        raise ValueError("n doit être positif ou nul")
    resultat = 1
    for valeur in range(2, n + 1):
        resultat *= valeur
    return resultat


def est_premier(n: int) -> bool:
    """Indique si n est un nombre premier."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise ValueError("n doit être un entier")
    if n < 2:
        return False
    diviseur = 2
    while diviseur * diviseur <= n:
        if n % diviseur == 0:
            return False
        diviseur += 1
    return True


def pgcd(a: int, b: int) -> int:
    """Calcule le plus grand commun diviseur de deux entiers."""
    if any(isinstance(x, bool) or not isinstance(x, int) for x in (a, b)):
        raise ValueError("a et b doivent être des entiers")
    if a < 0 or b < 0:
        raise ValueError("a et b doivent être positifs ou nuls")
    while b:
        a, b = b, a % b
    return a
