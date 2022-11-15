import pandas as pd

homelessnes = pd.read_csv('homelessness.csv', index_col=0)

homelessnes_ind = homelessnes.sort_values('individuals')
# print(homelessnes_ind.head())

homelessnes_fam = homelessnes.sort_values('family_members', ascending= False)
# print(homelessnes_fam.head())

homelessnes_reg_fam = homelessnes.sort_values(['region', 'family_members'], ascending= [True, False])
print(homelessnes_reg_fam.head())