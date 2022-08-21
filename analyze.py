import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# データの読み込み
df = pd.read_csv('loto6_data.csv', encoding='shift_jis')

# SepalLength列をndarrayに変換
data = np.array(df['ボーナス数字'])

# ヒストグラム
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.hist(data, bins=43, histtype='barstacked', ec='black')
plt.xticks(np.arange(1,43,1))
plt.show()