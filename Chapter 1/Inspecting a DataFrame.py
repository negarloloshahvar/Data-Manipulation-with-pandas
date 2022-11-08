import pandas as pd

homelessnes = pd.read_csv('homelessness.csv', index_col=0)
homelessnes_df = pd.DataFrame(homelessnes)

print(type(homelessnes))
print(type(homelessnes_df))

# Inspection

print(homelessnes.head())
print(homelessnes.info())
print(homelessnes.shape)
print(homelessnes.describe())