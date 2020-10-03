# Structure des citations
class Quote:
    def __init__(self, text, author):
        self.text = text
        self.author = author

# Définition des citations
quotes = [
    # Citations de VVK
    Quote("C'est moins simple", "Vincent V.K."),
    Quote("C'est moins marrant", "Vincent V.K."),
    Quote("On va pas être copain", "Vincent V.K."),
    Quote("C'est presque évident", "Vincent V.K."),

    # Citations de Stefano
    Quote("Le cahier de prépa est à jour", "Stefano S."),
    Quote("Reviens dans une heure", "Stefano S."),
    Quote("Ne seront lues que les réponses dont les _résultats ou mots importants sont ENCADRÉS_, et dont on a vérifié l'_HOMOGÉNÉIRÉ_", "Stefano S."),

    # Citations de Baptiste
    Quote("Tout seul on va plus vite, ensemble on va plus loin", "Baptiste H. (proverbe africain)"),

    # Citations de René
    Quote("M. RINGOT, DEVANT !", "René L."),
]
