from typing import List


def do_masses_match(mass: float, ms_mass: float, ppm=20) -> bool:
    error_pc = ppm/1000000
    error = (ms_mass * error_pc)
    lower = ms_mass - error
    upper = ms_mass + error
    #print(f"Range = {lower} to {upper} with an error of {error}")
    if mass > lower and mass < upper:
        return True
    return False

def is_mass_in_specta(mass: float, list_ms_masses: List[float], ppm=20) -> bool:
    for ms_mass in list_ms_masses:
        if do_masses_match(mass, ms_mass, ppm=ppm):
            return True
    return False



if __name__ == '__main__':
    test_mass = 353.1568
    actual = 353.1456

    result = do_masses_match(test_mass, actual)
    print(result)