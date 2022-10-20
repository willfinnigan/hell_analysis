from dataclasses import dataclass, field
from typing import List

from hell_analysis.peptide.amino_acid import AminoAcid
from hell_analysis.peptide.fragment import B_Fragment, Fragment, Y_Fragment, create_y_fragment, create_b_fragment


@dataclass
class Peptide():
    aa_list: List[AminoAcid]
    b_fragments: List[B_Fragment] = field(default_factory=list)
    y_fragments: List[Y_Fragment] = field(default_factory=list)
    all_fragments: List[Fragment] = field(default_factory=list)
    num_matches: int = 0
    num_matches_with_modification: int = 0

    def size(self):
        return len(self.aa_list)

    def create_fragments(self):
        self.b_fragments = self._create_b_fragments()
        self.y_fragments = self._create_y_fragments()
        self.all_fragments = self.b_fragments + self.y_fragments
        return self.all_fragments

    def get_fragment_masses(self):
        masses = []
        for fragment in self.all_fragments:
            masses.append(fragment.get_mass())
        return masses

    def get_fragment_masses_plus2(self):
        masses = []
        for fragment in self.all_fragments:
            masses.append(fragment.get_2plus_mass())
        return masses

    def theoretical_ms2_spectra(self):
        masses = self.get_fragment_masses() + self.get_fragment_masses_plus2()
        masses.sort()
        return masses

    def _create_b_fragments(self) -> List[B_Fragment]:
        list_of_fragments = []
        for i in range(self.size()):
            new_fragment = create_b_fragment(self.aa_list, 0, i)
            if new_fragment is not None:
                list_of_fragments.append(new_fragment)
        return list_of_fragments

    def _create_y_fragments(self) -> List[Y_Fragment]:
        list_of_fragments = []
        for i in range(self.size(), 0, -1):
            new_fragment = create_y_fragment(self.aa_list, i, self.size())
            if new_fragment is not None:
                list_of_fragments.append(new_fragment)
        return list_of_fragments

    def __repr__(self):
        fragment_string = ""
        for aa in self.aa_list:
            fragment_string += aa.as_string()
        return fragment_string

    def __lt__(self, other):
        return self.num_matches < other.num_matches



def create_peptide(seq_str: str) -> Peptide:
    aa_list = []
    for i, l in enumerate(seq_str):
        aa_list.append(AminoAcid(l, i))
    peptide = Peptide(aa_list)
    peptide.create_fragments()
    return peptide