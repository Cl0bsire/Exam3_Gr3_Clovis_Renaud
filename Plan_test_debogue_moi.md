| Cas                         | Input                                                                                                                         | Résultat attendu               | Résultat obtenu               |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------|--------------------------------|-------------------------------|
| Cas normal                  | {"Amélie" : ("08:15","60"), "Hakim" : ("09:30","90"), "Bouchra" : ("11:15","60"), "Jacob" : ("13:45","30") }, 'Pierre', '45'  | Rendez-vous confirmé à 14:30.  | Rendez-vous confirmé à 14:30. |
| Durée invalide              | {"Amélie" : ("08:15","60"), "Hakim" : ("09:30","90"), "Bouchra" : ("11:15","60"), "Jacob" : ("13:45","30") }, 'Pierre', 'mot' | Informations invalides         | Informations invalides        |
| Nom déjà dans le calendrier | {"Amélie" : ("08:15","60"), "Hakim" : ("09:30","90"), "Bouchra" : ("11:15","60"), "Jacob" : ("13:45","30") }, 'Jacob', '45'   | Nom déjà au calendrier         | Nom déjà au calendrier        |

   rendez_vous = {
        "Amélie" : ("08:15","60"),
        "Hakim" : ("09:30","90"),
        "Bouchra" : ("11:15","60"),
        "Jacob" : ("13:45","30")
    }