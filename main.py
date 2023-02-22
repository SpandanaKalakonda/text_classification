import pandas as pd
import numpy as np
import seaborn as sns
d1 = pd.read_csv("/data/flabel12.csv")
d2 = pd.read_csv("/data/dataairport1.csv")
d3 = pd.read_csv("/data/datachruch1.csv")
d4 = pd.read_csv("/data/datahospital1.csv")
d5 = pd.read_csv("/data/datarestaurant.csv")
d6 = pd.read_csv("/data/datazoo1.csv")
data = pd.concat([d1,d3,d4,d5,d6])
data.shape
