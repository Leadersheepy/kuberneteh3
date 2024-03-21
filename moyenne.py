def calcul_moyenne(valeurs):
    if len(valeurs) == 0:
        return 0
    return sum(valeurs) / len(valeurs)


# Tests unitaires avec pytest
import pytest

def test_calcul_moyenne():
    assert calcul_moyenne([1, 2, 3, 4, 5]) == 3
    assert calcul_moyenne([0, 0, 0, 0, 0]) == 0
    assert calcul_moyenne([10, 20, 30, 40, 50]) == 30
    assert calcul_moyenne([]) == 0  # Test avec une liste vide
