
import pandas as pd


df = pd.read_csv("glosario.csv")

url = 'https://drive.google.com/uc?id=1MqW2EpcIAnmffzu64-bq4kBv-07y9ILT'
df = pd.read_csv(url)

print (df)


import pandas as pd
import gdown


url = 'https://drive.google.com/file/d/1MqW2EpcIAnmffzu64-bq4kBv-07y9ILT/view?usp=drive_link'


output = 'glosario.csv'

gdown.download(url, output, quiet=False)


df = pd.read_csv('glosario.csv')
print(df)

print(df.head())
print(df.describe())
print(df.info())

