import pytest
from debogue_moi import ajouter_apres_dernier as ajouter_apres_dernier

@pytest.mark.parametrize("dict, nom, duree, resultat_attendu",[
    ({"Amélie" : ("08:15","60"), "Hakim" : ("09:30","90"), "Bouchra" : ("11:15","60"), "Jacob" : ("13:45","30") }, 'Pierre', '45', 'Rendez-vous confirmé à 14:30.')
])

def test_ajouter_apres_dernier_1(dict, nom, duree, resultat_attendu):
    #Act
    resultat=ajouter_apres_dernier(dict,nom,duree)

    #Assert
    assert resultat==resultat_attendu