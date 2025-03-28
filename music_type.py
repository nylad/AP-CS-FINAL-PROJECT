class MusicType:
    def __init__(self, country: int, rap: int, pop: int, r_and_b: int):
        self.genre = {
            'country' : country, 
            'rap' : rap, 
            'pop' : pop, 
            'r&b' : r_and_b,
        }
    def add(self, genre: str) -> None: 
        if genre == 'country': 
            self.genre['country'] = self.genre.get('country') + 1
        if genre == 'rap': 
            self.genre['rap'] = self.genre.get('rap') + 1 
        if genre == 'pop' : 
            self.genre['pop'] = self.genre.get('pop') + 1 
        if genre == 'r&b' :
            self.genre['r&b'] = self.genre.get('r&b') + 1 

    def sort(self) -> str: 
        score =0
        result = ''
    
        for music, points in self.genre.items(): 
            if points > score: 
                score = points
                result = music

        return result 

    def clear(self) -> None: 
        self.genre = {
            'country': 0, 
            'rap': 0, 
            'pop': 0, 
            'r&b': 0,

        }





