import pandas as pd
i_b=2

i=[1,2,3,4,5]
m=[37.7, 38.5, 39.4, 40.0, 41.3]

df= pd.DataFrame()

df['i']=i
df['m']=m

df.set_index('i')
display(df)