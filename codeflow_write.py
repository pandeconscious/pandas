import pandas as pd

filename = "test_write.csv"
data = pd.DataFrame([1+2j,2+3j,3+4j],columns=['a'])
print(data.dtypes)
import pdb; pdb.set_trace()
data.to_csv(filename)
