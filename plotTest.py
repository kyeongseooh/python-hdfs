#%%
import pandas as pd
import matplotlib.pyplot as plt

item1 = ['10', '20']
item2 = ['20', '30']
df = pd.DataFrame(data={0: item1, 1: item2})
print(df[0])
x = df[0]
y = df[1]

plt.plot(x, y, 'g^') 
plt.show()
# %%
