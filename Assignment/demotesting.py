import pandas as pd
from sklearn import preprocessing
from Assignment.ReadCSV import LoadCSV
from BasicStats import BasicStats
from Corellation import CorrelationImplement
from plot import DataPlot
import pprint

basicstats= BasicStats.BasicStatistics()
correlation= CorrelationImplement.CorrelationImplement()
plot= DataPlot.DataPlot()
data=LoadCSV("../csv_files/car.csv", basicstats, correlation,plot)
df=data.get_dataframe
print(df['CarName'].value_counts())
# enc=preprocessing.OneHotEncoder()
# enc.fit(df[['']])
# print(enc.categories)

