import copy
from typing import Optional, List

from hell_analysis.peptide.peptide import Peptide


def create_modified_peptide(peptide: Peptide, modification: float, modification_index: int) -> Optional[Peptide]:
    aa_list = copy.deepcopy(peptide.aa_list)[0:peptide.size()]
    if aa_list[modification_index].modification != 0:
        return None
    aa_list[modification_index].modification = modification
    peptide = Peptide(aa_list)
    peptide.create_fragments()
    return peptide

def make_modified_peptides(peptide: Peptide, modification: float) -> List[Peptide]:
    modified_peptides = []
    for i, aa in enumerate(peptide.aa_list):
        new_peptide = create_modified_peptide(peptide, modification, i)
        if new_peptide is not None:
            modified_peptides.append(new_peptide)
    return modified_peptides

def deduplicate(list_peptides: List[Peptide]) -> List[Peptide]:
    not_duplicate = []
    not_duplicate_strs = []
    for peptide in list_peptides:
        if str(peptide) not in not_duplicate_strs:
            not_duplicate.append(peptide)
            not_duplicate_strs.append(str(peptide))
    return not_duplicate

def make_all_modification_combinations(peptide: Peptide, modification: float, maximum_modifications: int) -> List[Peptide]:
    if maximum_modifications == 0:
        return [peptide]

    list_varients = make_modified_peptides(peptide, modification)

    if maximum_modifications == 1:
        return list_varients + [peptide]

    for i in range(maximum_modifications-1):
        new_varients = []
        for varient in list_varients:
            new_varients += make_modified_peptides(varient, modification)
        list_varients += new_varients

    list_varients = list_varients + [peptide]
    list_varients = deduplicate(list_varients)

    return list_varients