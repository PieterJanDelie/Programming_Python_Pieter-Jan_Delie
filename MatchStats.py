class MatchStats:
    def __init__(self, speler_nummer, matchnummer, gespeelde_minuten, gescoorde_punten):
        self.speler_nummer = speler_nummer
        self.matchnummer = matchnummer
        self.gespeelde_minuten = gespeelde_minuten
        self.gescoorde_punten = gescoorde_punten

    def to_tuple(self):
        return (self.speler_nummer, self.matchnummer, self.gespeelde_minuten, self.gescoorde_punten)

    def __str__(self):
        return f"MatchStats (Speler {self.speler_nummer}, Match {self.matchnummer}): {self.gespeelde_minuten} minuten gespeeld, {self.gescoorde_punten} punten gescoord"
