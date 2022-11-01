from hell_analysis.mass_matching.load_masses import load_masses
from hell_analysis.mass_matching.psm_score import get_peptide_mass_matches
from hell_analysis.peptide.peptide import create_peptide
from hell_analysis.peptide.peptide_modification_factory import make_all_modification_combinations

peptide_str = 'FVNQHLCGSHLVEALYLVCGERGFFYTPKT'
modification_mass = 182.1671
max_modifications = 1
path_to_excel = "lauric acid - peak 1.xlsx"

peptide = create_peptide(peptide_str)
all_peptides = make_all_modification_combinations(peptide, modification_mass, max_modifications)
masses = load_masses(path_to_excel)
peptide_matches = get_peptide_mass_matches(all_peptides, masses, ppm=20)

for (peptide, num_matches) in peptide_matches:
    print(f"{peptide} - {num_matches}")