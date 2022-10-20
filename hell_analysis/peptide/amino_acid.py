from dataclasses import dataclass

"""
http://www.matrixscience.com/help/aa_help.html
To calculate the mass of a neutral peptide or protein, 
sum the residue masses plus the masses of the terminating groups 
(e.g. H at the N-terminus and OH at the C-terminus).

https://proteomicsresource.washington.edu/protocols06/masses.php
"""

aa_weights = {"G": 57.021463735,
              "A": 71.037113805,
              'S': 87.032028435,
              'P': 97.052763875,
              'V': 99.068413945,
              'T': 101.047678505,
              'C': 103.009184505,
              'L': 113.084064015,
              'I': 113.084064015,
              'N': 114.042927470,
              'D': 115.026943065,
              'Q': 128.058577540,
              'K': 128.094963050,
              'E': 129.042593135,
              'M': 131.040484645,
              'H': 137.058911875,
              'F': 147.068413945,
              'R': 156.101111050,
              'Y': 163.063328575,
              'W': 186.079312980}


@dataclass
class AminoAcid():
    letter: str
    fragment_index: int
    modification: float = 0.0

    def mw(self):
        return aa_weights[self.letter] + self.modification

    def as_string(self):
        if self.modification == 0:
            return self.letter
        return f"{self.letter}(+{self.modification})"