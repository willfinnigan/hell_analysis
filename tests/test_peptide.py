from hell_analysis.peptide.peptide import create_peptide, Peptide
from hell_analysis.peptide.peptide_modification_factory import make_all_modification_combinations


def test_can_create_peptide():
    peptide = create_peptide('MGAP')
    assert isinstance(peptide, Peptide) == True

def test_can_get_correct_peptide_size():
    peptide = create_peptide('MGAP')
    assert peptide.size() == 4

def test_can_create_all_peptide_fragments():
    peptide = create_peptide('MGAP')
    assert [str(f) for f in peptide.all_fragments] == ['M', 'MG', 'MGA', 'P', 'AP', 'GAP']

def test_can_create_all_single_modifications_of_peptide():
    peptide = create_peptide('MGAP')
    modified = make_all_modification_combinations(peptide, 180.1, 1)
    assert [str(f) for f in modified] == ['M(+180.1)GAP', 'MG(+180.1)AP', 'MGA(+180.1)P', 'MGAP(+180.1)', 'MGAP']



