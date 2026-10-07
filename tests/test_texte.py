import pytest

from app.outils.texte import compter_voyelles, est_palindrome, inverser


def test_est_palindrome_cas_normal():
    assert est_palindrome("Ésope reste ici et se repose") is True


def test_est_palindrome_limite():
    assert est_palindrome("") is True


def test_est_palindrome_erreur_type():
    with pytest.raises(ValueError):
        est_palindrome(None)


def test_compter_voyelles_cas_normal():
    assert compter_voyelles("Éléphant") == 3


def test_compter_voyelles_limite():
    assert compter_voyelles("") == 0


def test_compter_voyelles_erreur_type():
    with pytest.raises(ValueError):
        compter_voyelles(4)


def test_inverser_cas_normal():
    assert inverser("salut") == "tulas"


def test_inverser_limite():
    assert inverser("") == ""


def test_inverser_erreur_type():
    with pytest.raises(ValueError):
        inverser([])
