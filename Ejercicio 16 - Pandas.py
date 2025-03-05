import pandas as pd
datos = [12,13,15,17,111,131,171,191,231,291]
pf =pd.Series(datos)
print (pf)
print (pf.std())
print (pf.mean())
print (pf.min())
print (pf.max())


