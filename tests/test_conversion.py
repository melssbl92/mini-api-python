import pytest

from app.outils.conversion import celsius_fahrenheit, euros_devise, km_miles


def test_celsius_fahrenheit_cas_normal():
    assert celsius_fahrenheit(20) == 68


def test_celsius_fahrenheit_limite():
    assert celsius_fahrenheit(-40) == -40


def test_celsius_fahrenheit_erreur_non_fini():
    with pytest.raises(ValueError):
        celsius_fahrenheit(float("inf"))


def test_km_miles_cas_normal():
    assert km_miles(10) == 6.21


def test_km_miles_limite_zero():
    assert km_miles(0) == 0


def test_km_miles_erreur_negatif():
    with pytest.raises(ValueError):
        km_miles(-0.1)


def test_euros_devise_cas_normal():
    assert euros_devise(10, 1.1) == 11


def test_euros_devise_limite_zero():
    assert euros_devise(0, 1.1) == 0


def test_euros_devise_erreur_taux():
    with pytest.raises(ValueError):
        euros_devise(10, 0)
