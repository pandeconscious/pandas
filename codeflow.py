import pandas as pd

import pdb; pdb.set_trace()

filename = "test_float.csv"
data2 = pd.read_csv(filename)
print(data2.dtypes)
