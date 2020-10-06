# Import du random
from random import choices


# Structure des citations
class Quote:
    """
    L'objet Quote est utilisé pour représenter une citation d'un professeur, ou autre.\n
    Il est composé de plusieurs attributs :
     - text : Cela représente le texte de la citation, qui sera affiché à l'écran, cela doit être un string
     - author : Cela représente l'auteur de la citation, ce sera affiché en dessous du texte de la citation
     - weight : Cela représente la pondération de la citation, ses chances d'être choisie. Valeur si non fourni : 100
    Finalement, il existe une variable de classe currentTotalWeight, qui est utilisée pour calculer les poids cumulés.\n
    Cette variable contient la somme des poids de tout les poids des citations.
    """

    # Initialisation d'une variable de classe, pour définir des poids cumulatifs
    currentTotalWeight = 0

    def __init__(self, text, author, weight = 100):
        # Initialisation de attributs
        self.text = text
        self.author = author

        # Gestion des poids
        Quote.currentTotalWeight += weight

        # Ajout dans les listes
        quotes.append(self)
        quotesWeight.append(Quote.currentTotalWeight)



# Tirage d'une citation
def random_quote():
    """ Tire une citation au hasard dans la liste pondéré des citations """
    # On return une citation au hasard
    return choices(quotes, cum_weights = quotesWeight, k = 1)[0]

# Création des listes des citations
quotes = []
quotesWeight = []



""" Definition des citations """

# Guide pour pondérer les citations :
# Vide si c'est une citation commune/emblématique d'un prof
# 80 si elle est un peu plus rare
# 70 si elle vient d'un philosophe/auteur ...
# 30 si c'est plus une blague qu'autre chose

# Citations de VVK
Quote("C'est moins simple.", "Vincent V.K.")
Quote("C'est moins marrant.", "Vincent V.K.")
Quote("On va pas être copain.", "Vincent V.K.")
Quote("C'est presque évident.", "Vincent V.K.")
Quote("Je ressemble plus à une vache que vous à des scientifiques.", "Vincent V.K.")
Quote("C'est **tragique !**", "Vincent V.K.")
Quote("Ça, c'est tout à fait remarquable.", "Vincent V.K.")
Quote("Tout le reste, c'est une question d'échelle.", "Vincent V.K.", 80)
Quote("Pôle Emploi va vous recevoir ... vous aurez pas de travail, mais il va vous recevoir !", "Vincent V.K.", 80)

# Citations de Stefano
Quote("Le cahier de prépa est à jour.", "Stefano S.")
Quote("Reviens dans une heure.", "Stefano S.")
Quote("Ne seront lues que les réponses dont les __résultats ou mots importants sont ENCADRÉS__, et dont on a vérifié l'__HOMOGÉNÉITÉ__.", "Stefano S.")
Quote("On connait une tension, on cherche une tension.", "Stefano S.")
Quote("On passe au plat de résistance ?", "Stefano S.")
Quote("Les notes, on s'en fout ! Si tu veux, je te met un 20.", "Stefano S.")

# Citations de Baptiste
Quote("Tout seul on va plus vite, ensemble on va plus loin.", "Baptiste H. (proverbe africain)")
Quote("Il y a des normes.", "Baptiste H.", 80)

# Citations de René
Quote("M. RINGOT, **DEVANT !**", "René L.")
Quote("Toi, cours jusqu'à la salle des profs et fait moi 15 photocopies du sujet !", "René L.", 80)

# Citations de Claire
Quote("Ok guys!", "Claire T.B.")

# Citations philosophes/auteurs
Quote("Quiconque lutte contre des monstres devrait prendre garde, dans le combat, à ne pas devenir monstre lui-même.\n" + \
      "Et quant à celui qui scrute le fond de l'abysse, l'abysse le scrute à son tour.", "Friedrich N.", 70)
Quote("Dieu est mort ! Dieu reste mort ! Et c'est nous qui l'avons tué ! Comment nous consoler, nous les meurtriers des meurtriers ?", "Friedrich N.", 70)

# Citations anonymes
Quote("Tout est relatif, sauf la vodka, qui est absolute !", "Anonyme", 30)

# Citiations diverses
Quote("We can be do, to do. What we want to do!", "François H.", 30)
Quote("Yes, **WE CAN!**", "Barrack O.", 30)