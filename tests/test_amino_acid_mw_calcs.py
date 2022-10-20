from hell_analysis.peptide.amino_acid import AminoAcid


def test_aa_mw_is_correct():
    aa = AminoAcid('M', 0, modification=0.0)
    assert aa.mw() == 131.040484645

def test_aa_mw_is_correct_with_modification():
    aa = AminoAcid('M', 0, modification=180.01)
    assert aa.mw() == 131.040484645 + 180.01