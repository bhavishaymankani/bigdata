import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

fruits = pd.read_table('D:\\R Studio\\fruit_data_with_colors.txt')
a = fruits.groupby("fruit_name").size()
print(a)

a["fruit_name"] = a.index
sns.countplot(x="fruit_name", data=fruits)
plt.show()