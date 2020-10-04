# Import du random
from random import choices

# Structure des citations
class Quote:

    # Initialisation d'une variable de classe, pour définir des poids cumulatifs
    currentTotalWeight = 0

    def __init__(self, text, author, weight = 80):
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
    # On return une citation au hasard
    return choices(quotes, cum_weights = quotesWeight, k = 1)[0]

# Création des listes des citations
quotes = []
quotesWeight = []


""" Definition des citations """

# Guide pour pondérer les citations :
# Vide si c'est une citation commune/emblématique d'un prof
# 40 si elle est un peu plus rare
# 60 si elle vient d'un philosophe/auteur ...
# 20 si c'est plus une blague qu'autre chose

# Citations de VVK
Quote("C'est moins simple", "Vincent V.K.")
Quote("C'est moins marrant", "Vincent V.K.")
Quote("On va pas être copain", "Vincent V.K.")
Quote("C'est presque évident", "Vincent V.K.")

# Citations de Stefano
Quote("Le cahier de prépa est à jour", "Stefano S.")
Quote("Reviens dans une heure", "Stefano S.")
Quote("Ne seront lues que les réponses dont les __résultats ou mots importants sont ENCADRÉS__, et dont on a vérifié l'__HOMOGÉNÉITÉ__", "Stefano S.")

# Citations de Baptiste
Quote("Tout seul on va plus vite, ensemble on va plus loin", "Baptiste H. (proverbe africain)")

# Citations de René
Quote("M. RINGOT, **DEVANT !**", "René L.")
Quote("Toi, cours jusqu'à la salle des profs et fait moi 15 photocopies du sujet!", "René L.", 40)

# Citations philosophes/auteurs
Quote("Quiconque lutte contre des monstres devrait prendre garde, dans le combat, à ne pas devenir monstre lui-même.\n" + \
      "Et quant à celui qui scrute le fond de l'abysse, l'abysse le scrute à son tour.", "Friedrich N.", 60)

# Citations anonymes
Quote("Tout est relatif, sauf la vodka, qui est absolute !", "Anonyme", 20)

# Citiations diverses
Quote("We can be do, to do. What we want to do!", "François H.", 20)
Quote("Yes, **WE CAN!**", "Barrack O.", 20)