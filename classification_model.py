from turtle import pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fruits = pd.read_table('D:\\R Studio\\fruit_data_with_colors.txt')
fruits.head()
print(fruits)
print(fruits['fruit_name'].unique())
print(fruits.shape)
