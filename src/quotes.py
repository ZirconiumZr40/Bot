# Structure des citations
class Quote:

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



# Création des listes des citations
quotes = []
quotesWeight = []


""" Definition des citations """

# Citations de VVK
Quote("C'est moins simple", "Vincent V.K."),
Quote("C'est moins marrant", "Vincent V.K."),
Quote("On va pas être copain", "Vincent V.K."),
Quote("C'est presque évident", "Vincent V.K."),

# Citations de Stefano
Quote("Le cahier de prépa est à jour", "Stefano S."),
Quote("Reviens dans une heure", "Stefano S."),
Quote("Ne seront lues que les réponses dont les __résultats ou mots importants sont ENCADRÉS__, et dont on a vérifié l'__HOMOGÉNÉITÉ__", "Stefano S."),

# Citations de Baptiste
Quote("Tout seul on va plus vite, ensemble on va plus loin", "Baptiste H. (proverbe africain)"),

# Citations de René
Quote("M. RINGOT, DEVANT !", "René L."),

# Citations anonymes
Quote("Tout est relatif, sauf la vodka, qui est absolute !", "Anonyme", 10)

# Citiations diverses
Quote("We can be do, to do. What we want to do!", "François H.", 10)