def calculer_moyenne(liste):
    if not liste:
        return 0
    return sum(liste) / len(liste)

def test_calculer_moyenne():
    assert calculer_moyenne([1, 2, 3, 4, 5]) == 3
    assert calculer_moyenne([]) == 0
    assert calculer_moyenne([0, 0, 0, 0]) == 0
    assert calculer_moyenne([-1, 1]) == 0

if __name__ == "__main__":
    test_calculer_moyenne()
    print("Tous les tests ont réussi.")