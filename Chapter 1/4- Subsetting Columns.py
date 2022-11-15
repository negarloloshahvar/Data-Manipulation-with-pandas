import pandas as pd

homelessnes = pd.read_csv('homelessness.csv', index_col=0)

print(homelessnes[['region', 'family_members']])