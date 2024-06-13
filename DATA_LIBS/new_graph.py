import pandas as pd
import plotly.express as px

data = {'Day': [1, 2, 3, 4, 5], 'Sales': [200, 220, 250, 270, 300]}
df = pd.DataFrame(data)
df.head()

fig = px.bar (df, x= 'Day', y= 'Sales')
fig.show()