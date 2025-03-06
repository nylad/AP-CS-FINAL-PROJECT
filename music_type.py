class MusicType :
    def __init__(self, music_type: int, country: int, rap: int, pop: int, r&b: int):
        self.generes = {
            'country' : country, 
            'rap' : rap, 
            'pop' : pop, 
            'r&b' : r&b 
        }
    def add(self, genere: str) -> None: 
        if genere == 'country': 
            self.genere['country'] = self.genere.get('country') + 1
        if genere == 'rap': 
            self.genere['rap'] = self.genere.get('rap') + 1 
        if genere == 'pop' : 
            self.genere['pop'] = self.genere.get('pop') + 1 
        if genere == 'r&b' :
            self.genere['r&b'] = self.genere.get('r&b') + 1 

    def sort(self) -> str: 
        score = 0
        result = ''
        for genere, points in self .genere.items(): 
            if points > score: 
                result = genere 

        return result 

    def clear(self) -> None: 
        self.genere = {
            'country': 0, 
            'rap': 0, 
            'pop': 0, 
            'r&b': 0,

        }





