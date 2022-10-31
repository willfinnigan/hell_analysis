from typing import List

from hell_analysis.mass_matching.mass_matcher import is_mass_in_specta
from hell_analysis.peptide.peptide import Peptide, create_peptide
from hell_analysis.peptide.peptide_modification_factory import make_all_modification_combinations


def match_spectra(peptide: Peptide, ms_masses: List[float]):
    matches = []
    no_matches = []
    for mass in peptide.theoretical_ms2_spectra():
        if is_mass_in_specta(mass, ms_masses, error=0.002):
            matches.append(mass)
        else:
            no_matches.append(mass)
    return matches, no_matches

def score_psm(peptide: Peptide, ms_masses: List[float]):
    matches, no_matches = match_spectra(peptide, ms_masses)
    score = round((len(matches) / (len(matches) + len(no_matches)) ) * 100,1)
    return score

def get_peptide_mass_matches(list_peptides: List[Peptide], ms_masses: List[float]):
    peptide_matches = []
    for peptide in list_peptides:
        num_matches = score_psm(peptide, ms_masses)
        peptide_matches.append((peptide, num_matches))

    return sorted(peptide_matches, key=lambda t: t[1], reverse=True)


if __name__ == '__main__':
    from example.example_masses import example_masses

    peptide = create_peptide('FVNQHLCGSHLVEALYLVCGERGFFYTPKT')
    all_peptides = make_all_modification_combinations(peptide, 182.1671, 2)

    peptide_matches = get_peptide_mass_matches(all_peptides, example_masses)

    for (peptide, num_matches) in peptide_matches:
        print(f"{peptide} - {num_matches}")
