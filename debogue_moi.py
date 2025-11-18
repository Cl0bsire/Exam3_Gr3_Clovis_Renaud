import datetime

def ajouter_apres_dernier(calendrier: dict, nom: str, duree: str) -> str:
    """
    Fonction pour ajouter un rendez-vous au premier moment disponible dans le caledrier
    :param calendrier: Calendrier de rendez-vous professionels
    :param nom: nom du patient
    :param duree: durée du nouveau rendez-vous
    :return: une confirmation avec l'heure du nouveau rendez-vous
    """

    if nom in calendrier:
        return ("Nom déjà au calendrier")
    else:

        try:
            dernier_rv = list(calendrier)[-1]
            duree = datetime.datetime.strptime(duree, "%M")
            # Documentation Python https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
            h = datetime.datetime.strptime(calendrier[dernier_rv][0], "%H:%M")
            d = datetime.timedelta(minutes=int(calendrier[dernier_rv][1])+15)

            nouveau_debut = h + d

            heure_str = nouveau_debut.strftime("%H:%M")
            duree_str = duree.strftime("%M")
            # Documentation Python https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
            calendrier[nom] = (heure_str, duree_str)

            return f"Rendez-vous confirmé à {heure_str}."
        except:
            return "Informations invalides"

if __name__ == "__main__":
    rendez_vous = {
        "Amélie" : ("08:15","60"),
        "Hakim" : ("09:30","90"),
        "Bouchra" : ("11:15","60"),
        "Jacob" : ("13:45","30")
    }
    nom = input("Entrez le nom du patient : ")
    duree = input("Entrez la durée du rendez-vous, en minutes : ")
    print(ajouter_apres_dernier(rendez_vous, nom, duree))

