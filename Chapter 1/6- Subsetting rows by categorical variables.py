import pandas as pd

homelessnes = pd.read_csv('homelessness.csv', index_col=0)

south_mid_athlantic = homelessnes[(homelessnes['region'] == 'South Atlantic') | (homelessnes['region'] == 'Mid-Atlantic')]
print(south_mid_athlantic)