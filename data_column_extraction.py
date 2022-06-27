import pandas as pd
m_data= pd.read_csv('filename.csv')
x = m_data.drop(columns=['data'])
y=m_data['data']
df=pd.DataFrame(y)
df.to_csv("new_fiename.csv")



