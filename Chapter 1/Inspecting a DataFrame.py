import pandas as pd
import numpy as np

homelessnes = pd.read_csv('homelessness.csv')
homelessnes_df = pd.DataFrame(homelessnes)


print(homelessnes_df.shape)
print(homelessnes.shape)