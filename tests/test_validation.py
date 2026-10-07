import pytest

from app.outils.validation import code_postal, email_valide, mdp_robuste


def test_email_valide_cas_normal():
    assert email_valide("lea@example.fr") is True


def test_email_valide_limite():
    assert email_valide("x@y.io") is True


def test_email_valide_erreur_type():
    with pytest.raises(ValueError):
        email_valide(None)


def test_mdp_robuste_cas_normal():
    assert mdp_robuste("BonMotDePasse1!") is True


def test_mdp_robuste_limite():
    assert mdp_robuste("Abcdef1!") is True


def test_mdp_robuste_erreur_faible():
    assert mdp_robuste("faible") is False


def test_code_postal_cas_normal():
    assert code_postal("75001") is True


def test_code_postal_limite():
    assert code_postal("00000") is True


def test_code_postal_erreur_format():
    assert code_postal("7500A") is False
