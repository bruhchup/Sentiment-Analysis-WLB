import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

df = pd.read_excel('Sentiment-Analysis-WLB/data_cleaning/data/spread_sheet_for_DIB.xlsx', header=[0,1])

print(df)