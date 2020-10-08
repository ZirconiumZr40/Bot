# Import des ressources
import pytest
from quotes import random_quote

# Test du tirage d'une citation
def test_random_quote():
    # On tire une douzaine de quotes et check chacune d'entre elle
    for i in range(12):
        quote = random_quote()
        assert(quote.text and quote.author)