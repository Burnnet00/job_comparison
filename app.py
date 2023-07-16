import pandas as pd
import requests
import numpy as np
import matplotlib.pyplot as plt

response = requests.get('https://uadata.net/work-positions/cities.json?o=Одеса')
data_json = response.json()
df = pd.DataFrame(data_json["data"])
# print(df.head())
# print(df.shape)
# print(df.columns)
# print(df.dtypes)
df["at"] = pd.to_datetime(df["at"])
# print(df.dtypes)
df = df.rename(columns={"at": "Дата", "val": "Вакансії"})
# print(df.head())
df.set_index("Дата", inplace=True)  # del index
"""create grafic"""
df["Вакансії"] = df["Вакансії"].replace(0, np.nan)  # dell 0 replase on nan
df["Вакансії"] = df["Вакансії"].interpolate()

# df["Вакансії"].plot()
# plt.title("Кількість вакансій по Україні")
# plt.xlabel("Дата")
# plt.ylabel("Вакансії")
# plt.ylim(bottom=0)
# plt.show()

df["rolling_mean"] = df["Вакансії"].rolling(window=7).mean()  # roll on 7 day
df["rolling_mean"].plot()
plt.title("Кількість вакансій по Одесі")
plt.xlabel("Дата")
plt.ylabel("Вакансії")
plt.ylim(bottom=0)
plt.show()
df.describe()
