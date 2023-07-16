import pandas as pd
import requests
import numpy as np
import matplotlib.pyplot as plt

response = requests.get('https://uadata.net/work-positions/cities.json?o=Одеса')
data_json = response.json()

df_odessa = pd.DataFrame(data_json['data'])#response data on pandas
# print(df_odessa)
df_odessa ['at'] = pd.to_datetime(df_odessa ['at'])
df_odessa = df_odessa.rename(columns={"at": "Дата", "val": "Вакансії"})#rename at val
df_odessa.set_index("Дата", inplace=True) #dell num
df_odessa["Вакансії"] = df_odessa["Вакансії"].replace(0, np.nan)  # dell 0 replase on nan
df_odessa["Вакансії"] = df_odessa["Вакансії"].interpolate()
df_odessa["rolling_mean"] = df_odessa["Вакансії"].rolling(window=7).mean()  # roll on 7 day



response = requests.get('https://uadata.net/work-positions/cities.json?o=Київ')
data_json = response.json()

df_kyiv = pd.DataFrame(data_json['data'])#response data on pandas
# print(df_kyiv)
df_kyiv ['at'] = pd.to_datetime(df_kyiv ['at'])
df_kyiv = df_kyiv.rename(columns={"at": "Дата", "val": "Вакансії"})#rename at val
df_kyiv.set_index("Дата", inplace=True) #dell num
df_kyiv["Вакансії"] = df_kyiv["Вакансії"].replace(0, np.nan)  # dell 0 replase on nan
df_kyiv["Вакансії"] = df_kyiv["Вакансії"].interpolate()
df_kyiv["rolling_mean"] = df_kyiv["Вакансії"].rolling(window=7).mean()  # roll on 7 day

fig, axs = plt.subplots()
axs.plot(df_odessa.index, df_odessa["rolling_mean"], label="Одеса")
axs.plot(df_kyiv.index, df_kyiv["rolling_mean"], label="Київ")

plt.title("Кількість вакансій Одеса-Київ", fontsize=16)
plt.xlabel("Дата")
plt.ylabel("Вакансії")
plt.ylim(bottom=0)
plt.legend()
plt.show()


