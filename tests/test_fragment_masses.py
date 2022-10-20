import pytest

from hell_analysis.peptide.amino_acid import AminoAcid
from hell_analysis.peptide.fragment import Y_Fragment, B_Fragment


@pytest.mark.parametrize('aa_str, expected_mass', [('C', 122.0270),
                                                   ('HLC', 372.1700),
                                                   ('HLCQ', 500.2286),
                                                   ('HLCQN', 614.2715),
                                                   ('HLCQNV', 713.3399)])
def test_y_fragment_mass_is_correct(aa_str, expected_mass):
    aa_list = []
    for i, l in enumerate(aa_str):
        aa_list.append(AminoAcid(l, i))
    fragment = Y_Fragment(aa_list)
    assert round(fragment.get_mass(),4) == expected_mass


@pytest.mark.parametrize('aa_str, expected_mass', [('HLC', 186.5886),
                                                   ('HLCQ', 250.6179),
                                                   ('HLCQN', 307.6394),
                                                   ('HLCQNV', 357.1736)])
def test_y_fragment_mass_2plus_is_correct(aa_str, expected_mass):
    aa_list = []
    for i, l in enumerate(aa_str):
        aa_list.append(AminoAcid(l, i))
    fragment = Y_Fragment(aa_list)
    assert round(fragment.get_2plus_mass(),4) == expected_mass

@pytest.mark.parametrize('aa_str, expected_mass', [('FV', 247.1441),
                                                   ('FVN', 361.1870),
                                                   ('FVNQ', 489.2456),
                                                   ('FVNQH', 626.3045),
                                                   ('FVNQHL', 739.3886)])
def test_b_fragment_mass_is_correct(aa_str, expected_mass):
    aa_list = []
    for i, l in enumerate(aa_str):
        aa_list.append(AminoAcid(l, i))
    fragment = B_Fragment(aa_list)
    assert round(fragment.get_mass(),4) == expected_mass

@pytest.mark.parametrize('aa_str, expected_mass', [('FVNQH', 313.6559),
                                                   ('FVNQHL', 370.1979)])
def test_b_fragment_mass_2plus_is_correct(aa_str, expected_mass):
    aa_list = []
    for i, l in enumerate(aa_str):
        aa_list.append(AminoAcid(l, i))
    fragment = B_Fragment(aa_list)
    assert round(fragment.get_2plus_mass(),4) == expected_mass
