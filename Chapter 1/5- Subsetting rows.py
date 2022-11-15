import pandas as pd

homelessnes = pd.read_csv('homelessness.csv', index_col=0)

print(homelessnes.head())

ind_gt_10k = homelessnes[homelessnes['individuals'] > 10000]