import numpy as np

#x1 = np.random.uniform(-1, 1, 11)
x1 = np.linspace(-5, 5, 11)

print(x1)

y = x1 ** 2

print(y)

import matplotlib.pyplot as plt

plt.plot(x1, y, 'r--')
plt.scatter(x1, y)
plt.show()

import pandas as pd

df = pd.DataFrame({
    "X": x1,
    "Y": y
})

df.to_csv("datasets/test1.csv", index=False)
