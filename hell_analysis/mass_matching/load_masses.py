import pandas as pd

def load_masses(path_to_excel):
    df = pd.read_excel(path_to_excel)
    masses = list(df['m/z'])
    return masses

if __name__ == '__main__':
    path_to_excel = "/lauric acid - peak 1.xlsx"
    masses = load_masses(path_to_excel)
    print(masses)

