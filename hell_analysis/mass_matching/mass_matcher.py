from typing import List


def do_masses_match(mass: float, ms_mass: float, error=0.002) -> bool:
    lower = ms_mass - (ms_mass * error)
    upper = ms_mass + (ms_mass * error)
    if mass > lower and mass < upper:
        return True
    return False

def is_mass_in_specta(mass: float, list_ms_masses: List[float], error=0.002) -> bool:
    for ms_mass in list_ms_masses:
        if do_masses_match(mass, ms_mass, error=error):
            return True
    return False