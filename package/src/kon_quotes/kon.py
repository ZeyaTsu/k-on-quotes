import random
import requests
from typing import Literal

class Characters:
    azusa = "characters/azusa"
    jun = "characters/jun"
    mio = "characters/mio"
    ritsu = "characters/ritsu"
    sawako = "characters/sawako"
    tsumugi = "characters/tsumugi"
    yui = "characters/yui"
    general = "characters/general"
    all = "quotes"


class GETquote:
    def __init__(self, character: Literal["azusa", "jun", "mio", "ritsu", "sawako", "tsumugi", "yui", "all"] = "all"):
        self.character = character
        self.quote = self.getting_quote()  # Store the quote in an instance variable
    
    def getting_quote(self):
        character_link = getattr(Characters, self.character, None)
        url = f"https://zeyatsu.github.io/k-on-quotes/{character_link}.json"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            self.author = random.choice(list(data["authors"].keys()))
            quote = random.choice(data["authors"][self.author])
            return quote
        else:
            return "Error: Couldn't reach API or wrong character"
    
    def GETauthor(self):
        return self.author if self.author else "Error : No quote(s) generated yet"
    
    def __str__(self):
        return self.quote