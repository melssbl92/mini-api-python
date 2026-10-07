import pytest

from app.outils.math import est_premier, factorielle, pgcd


def test_factorielle_cas_normal():
    assert factorielle(5) == 120


def test_factorielle_limite_zero():
    assert factorielle(0) == 1


def test_factorielle_erreur_negatif():
    with pytest.raises(ValueError):
        factorielle(-1)


def test_est_premier_cas_normal():
    assert est_premier(13) is True


def test_est_premier_limite():
    assert est_premier(1) is False


def test_est_premier_erreur_type():
    with pytest.raises(ValueError):
        est_premier(3.2)


def test_pgcd_cas_normal():
    assert pgcd(54, 24) == 6


def test_pgcd_limite_zero():
    assert pgcd(0, 7) == 7


def test_pgcd_erreur_negatif():
    with pytest.raises(ValueError):
        pgcd(-1, 2)
