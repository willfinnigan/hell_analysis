from typing import List

from hell_analysis.peptide.fragment import Fragment
from hell_analysis.peptide.peptide import Peptide, create_peptide
from mass_matcher import is_mass_in_specta
from hell_analysis.peptide.peptide_modification_factory import make_all_modification_combinations

def get_all_fragments(list_peptides: List[Peptide], only_modified=True) -> List[Fragment]:
    all_fragments = []
    for peptide in list_peptides:
        for fragment in peptide.all_fragments:
            if fragment not in all_fragments:
                all_fragments.append(fragment)

    if not only_modified:
        return all_fragments

    modified_fragments = []
    for fragment in all_fragments:
        if fragment.has_modification():
            modified_fragments.append(fragment)
    return modified_fragments

def get_matching_fragments(list_fragments: List[Fragment], ms_masses: List[float], error=0.002) -> List[Fragment]:
    matches = []
    for fragment in list_fragments:
        mass = fragment.get_mass()
        mass_2plus = fragment.get_2plus_mass()

        if is_mass_in_specta(mass, ms_masses, error=0.002):
            matches.append(fragment)
        elif is_mass_in_specta( mass_2plus, ms_masses, error=0.002):
            matches.append(fragment)
    return matches


if __name__ == '__main__':
    from example.example_masses import example_masses

    peptide = create_peptide('FVNQHLCGSHLVEALYLVCGERGFFYTPKT')
    all_peptides = make_all_modification_combinations(peptide, 182.1671, 3)
    modified_fragments = get_all_fragments(all_peptides, only_modified=True)

    matched_fragments = get_matching_fragments(modified_fragments, example_masses)

    indexes_of_modifications = []

    for fragment in matched_fragments:
        indexes_of_modifications += fragment.get_modification_indexes()

    from collections import Counter
    counter = dict(Counter(indexes_of_modifications))
    print(counter)

    normalised_counts = {}
    max_count = max(list(counter.values()))
    for key, value in counter.items():
        normalised_counts[key] = round(value/max_count,2)

    aa_count_tuple = []
    for aa in peptide.aa_list:
        aa_count_tuple.append((aa.letter, normalised_counts[aa.fragment_index]))

    print(aa_count_tuple)

