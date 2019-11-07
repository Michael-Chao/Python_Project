import pandas as pd
import PCA

df = pd.read_excel('test.xlsx')
df_handle = PCA.loadDataSet(df)