class Speler:
    def __init__(self, voornaam, familienaam, nummer):
        self.voornaam = voornaam
        self.familienaam = familienaam
        self.nummer = nummer

    def to_tuple(self):
        return (self.nummer, self.voornaam, self.familienaam)

    def __str__(self):
        return f"Speler {self.nummer}: {self.voornaam} {self.familienaam}"