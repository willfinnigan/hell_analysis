from __future__ import annotations
import copy
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, Optional

from hell_analysis.peptide.amino_acid import AminoAcid

n_term_change = 1.007276
c_term_change = 17.00274
hyd = 1.00784
hyd_uncharged = 1.007825
two_plus_difference = 0.0003
# Detail: the proton mass of 1.007276 u is slightly different from the mass of an uncharged hydrogen atom at 1.007825 u)

class Fragment(ABC):

    @abstractmethod
    def get_mass(self) -> float:
        pass

    @abstractmethod
    def get_2plus_mass(self) -> float:
        pass

    @abstractmethod
    def has_modification(self) -> bool:
        pass

    @abstractmethod
    def get_modification_indexes(self) -> List[int]:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass

@dataclass
class B_Fragment():
    aa_list: List[AminoAcid]
    mass_matches: List[float] = field(default_factory=list)

    def get_mass(self) -> float:
        mass = 0.0
        for aa in self.aa_list:
            mass += aa.mw()

        mass += n_term_change

        return mass

    def get_2plus_mass(self) -> float:
        return (self.get_mass() + n_term_change)/2

    def has_modification(self) -> bool:
        for aa in self.aa_list:
            if aa.modification != 0:
                return True
        return False

    def get_modification_indexes(self) -> List[int]:
        modification_indexes = []
        for aa in self.aa_list:
            if aa.modification != 0:
                modification_indexes.append(aa.fragment_index)
        return modification_indexes

    def __repr__(self) -> str:
        fragment_string = ""
        for aa in self.aa_list:
            fragment_string += aa.as_string()
        return fragment_string

@dataclass
class Y_Fragment():
    aa_list: List[AminoAcid]
    mass_matches: List[float] = field(default_factory=list)

    def get_mass(self) -> float:
        mass = 0.0
        for aa in self.aa_list:
            mass += aa.mw()

        mass += n_term_change
        mass += c_term_change
        mass += hyd
        return mass

    def get_2plus_mass(self) -> float:
        return (self.get_mass() + n_term_change) / 2

    def has_modification(self) -> bool:
        for aa in self.aa_list:
            if aa.modification != 0:
                return True
        return False

    def get_modification_indexes(self) -> List[int]:
        modification_indexes = []
        for aa in self.aa_list:
            if aa.modification != 0:
                modification_indexes.append(aa.fragment_index)
        return modification_indexes

    def __repr__(self) -> str:
        fragment_string = ""
        for aa in self.aa_list:
            fragment_string += aa.as_string()
        return fragment_string


def create_b_fragment(aa_list: List[AminoAcid], start_index: int, end_index: int) -> Optional[B_Fragment]:
    aa_list = copy.deepcopy(aa_list)[start_index:end_index]
    if len(aa_list) == 0:
        return None
    return B_Fragment(aa_list)

def create_y_fragment(aa_list: List[AminoAcid], start_index: int, end_index: int) -> Optional[Y_Fragment]:
    aa_list = copy.deepcopy(aa_list)[start_index:end_index]
    if len(aa_list) == 0:
        return None
    return Y_Fragment(aa_list)

