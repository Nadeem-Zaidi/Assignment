from typing import Optional
import pandas as pd
from collections import defaultdict
from utility import utility
from pandas import DataFrame
from BasicStats import BasicStats,StatisticMethods
from Corellation import Correlation,CorrelationImplement
from plot import Plot,DataPlot
import pprint


class LoadCSV:

    def __init__(self, filename, st: StatisticMethods.StatisticsMethods, corr: Correlation.Correlation,plot:Optional[
        Plot.Plot]=None):
        self.__filename=filename
        self.__df=pd.read_csv(filename)
        self.__st=st
        self.__corr=corr
        if plot is not None:
            self.plot=plot


    def csv_file(self):
        return self.__filename

    def check_for_null_value(self):
        nullvalue=defaultdict()
        df=self.__df
        for c in df.columns:
            if df[c].isna().any():
                utility.dictionary(c,df[c].isna().sum(),nullvalue)
        return nullvalue

    @property
    def get_dataframe(self):
        return self.__df

    def describe_data(self):
        return self.get_dataframe.describe()

    @property
    def data_shape(self):
        return self.__df.shape

    @property
    def columns_present(self):
        columns= self.get_dataframe.columns
        return columns

    def columns_present_number(self):
        return len(self.get_dataframe.columns)

    def mean(self,column_name:str)->float:
        series=self.get_dataframe[column_name]
        return self.__st.mean(series)

    def standard_deviation(self,column_name:str)->float:
        series = self.get_dataframe[column_name]
        return self.__st.standard_deviation(series)

    def percentile(self,column_name:str,n:int)->float:
        series = self.get_dataframe[column_name]
        return self.__st.percentile(series,n)

    def IQR(self,column_name:str)->float:
        series = self.get_dataframe[column_name]
        return self.__st.IQR(series)

    def outlier_using_iqr(self,column_name:str)->list:
        series = self.get_dataframe[column_name]
        return self.__st.outliers_using_iqr(series)

    def outlier_using_zscore(self, column_name:str)->list:
        series = self.get_dataframe[column_name]
        return self.__st.outlier_using_zscore(series)

    def mean_and_std_of_each_columns(self):
        return self.__st.mean_and_std_of_each_columns(self.get_dataframe)

    def percentile_each_column(self):
        return self.__st.percentile_of_each_column(self.get_dataframe)

    def IQR_each_column(self):
        return self.__st.IQR_for_each_column(self.get_dataframe)


    def Correlation(self,col_1:str,col_2:str):

        c=self.__corr.correlation(col_1,col_2,self.get_dataframe)
        return c

    def CorrelationVsAll(self,colname:str):
        c=self.__corr.correlationAll(colname,self.get_dataframe)
        return c

    def scatterplot(self,c1:str,c2:str,s:str):
        df=self.get_dataframe
        self.plot.scatterplot(c1,c2,df,s)

    def bxplot(self,col:str):
        df=self.get_dataframe
        self.plot.BoxPlot(col,df)


basicstats= BasicStats.BasicStatistics()
correlation= CorrelationImplement.CorrelationImplement()
plot= DataPlot.DataPlot()

c=LoadCSV("./csv_files/car.csv", basicstats, correlation,plot)

print(c.data_shape)
print(c.columns_present)
print(f"Mean {c.mean('price')}")
print(f"standard deviation {c.standard_deviation('price')}")
print(f"Median {c.percentile('price',50)}")
print(f"IQR {c.IQR('price')}")
print("outlier using iqr",c.outlier_using_iqr('price'))
print("outlier using zscore",c.outlier_using_zscore('price'))
pprint.pprint(c.mean_and_std_of_each_columns())
pprint.pprint(c.percentile_each_column())
pprint.pprint(c.IQR_each_column())
print(c.Correlation("peakrpm","price"))
pprint.pprint(f"{c.CorrelationVsAll('price')}")
c.scatterplot('price','citympg','fivethirtyeight')
c.scatterplot('price','citympg','fivethirtyeight')
c.bxplot('price')









