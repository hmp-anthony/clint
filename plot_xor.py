import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def xor(x1, x2):
    """returns XOR"""
    return bool(x1) != bool(x2)

inputs = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([xor(*x) for x in inputs])

sns.set()

data = pd.DataFrame(inputs, columns=['x1', 'x2'])
data['xor'] = y
sns.scatterplot(data=data, x='x1', y='x2', style='xor', hue='xor', s=100)

plt.show()
