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

    def __init__(self, filename, st: StatisticMethods.StatisticsMethods, corr: Correlation.Correlation, plot:Optional[
        Plot.Plot]=None):
        self.__filename=filename
        self.__df=pd.read_csv(filename)
        self.st=st
        self.corr=corr
        if plot is not None:
            self.plot=plot


    def csv_file(self):
        return self.__filename

    def get_dataframe(self):

        return self.__df

    def describe_data(self):
        return self.get_dataframe().describe()

    @property
    def data_shape(self):
        return self.__df.shape

    @property
    def columns_present(self):
        columns= self.get_dataframe().columns
        return columns

    def columns_present_number(self):
        return len(self.get_dataframe().columns)

    def mean(self,column_name:str)->float:
        series=self.get_dataframe()[column_name]
        return self.st.mean(series)

    def standard_deviation(self,column_name:str)->float:
        series = self.get_dataframe()[column_name]
        return self.st.standard_deviation(series)

    def percentile(self,column_name:str,n:int)->float:
        series = self.get_dataframe()[column_name]
        return self.st.percentile(series,n)

    def IQR(self,column_name:str)->float:
        series = self.get_dataframe()[column_name]
        return self.st.IQR(series)

    def outlier_using_iqr(self,column_name:str)->list:
        series = self.get_dataframe()[column_name]
        return self.st.outliers_using_iqr(series)

    def outlier_using_zscore(self, column_name:str)->list:
        series = self.get_dataframe()[column_name]
        return self.st.outlier_using_zscore(series)

    def mean_and_std_of_each_columns(self):
        md=defaultdict()
        mean_dict=defaultdict()
        std_dict=defaultdict()
        data=self.get_dataframe()
        for c in data.columns:
            if utility.ValidSeries(data[c]):
                mean=self.st.mean(data[c])
                std=self.st.standard_deviation(data[c])
                utility.dictionary(c,mean,mean_dict)
                utility.dictionary(c,std,std_dict)

        utility.dictionary("mean",mean_dict,md)
        utility.dictionary("standard_deviation", std_dict, md)

        return md

    def percentile_of_each_column(self):
        percentile=defaultdict()
        q1=defaultdict()
        q2=defaultdict()
        q3=defaultdict()
        data=self.get_dataframe()
        for c in data:
            if utility.ValidSeries(data[c]):
                series=data[c]
                percentile_q1=self.st.percentile(series,25)
                percentile_q2=self.st.percentile(series,50)
                percentile_q3=self.st.percentile(series,75)
                utility.dictionary(c,percentile_q1,q1)
                utility.dictionary(c, percentile_q2, q2)
                utility.dictionary(c, percentile_q3, q3)
        utility.dictionary("percentile_q1",q1,percentile)
        utility.dictionary("percentile_q2", q2, percentile)
        utility.dictionary("percentile_q3", q3, percentile)
        return percentile

    def IQR_for_each_column(self):
        iqr_dict=defaultdict()
        data=self.get_dataframe()
        for c in data.columns:
            if utility.ValidSeries(data[c]):
                series=data[c]
                iqr=self.st.IQR(series)
                utility.dictionary(c,iqr,iqr_dict)
        return iqr_dict

    def Correlation(self,col_1:str,col_2:str,df:DataFrame):
        c=self.corr.correlation(col_1,col_2,df)
        return c

    def CorrelationVsAll(self,colname:str,df:DataFrame):
        c=self.corr.correlationAll(colname,df)
        return c

    def scatterplot(self,c1:str,c2:str,s:str):
        df=self.get_dataframe()
        self.plot.scatterplot(c1,c2,df,s)








basicstats= BasicStats.BasicStatistics()
correlation= CorrelationImplement.CorrelationImplement()
plot= DataPlot.DataPlot()
c=LoadCSV("../csv_files/car.csv", basicstats, correlation, plot)
print(c.data_shape)
print(c.columns_present)
print(c.mean('price'))
print(c.standard_deviation('price'))
print(c.percentile('price',50))
print(c.IQR('price'))
print("outlier",c.outlier_using_iqr('price'))
print("outlier using zscore",c.outlier_using_zscore('price'))
pprint.pprint(c.mean_and_std_of_each_columns())
pprint.pprint(c.percentile_of_each_column())
pprint.pprint(c.IQR_for_each_column())
print(c.Correlation("peakrpm","price",c.get_dataframe()))
c.scatterplot('price','citympg','fivethirtyeight')
c.scatterplot('price','citympg','fivethirtyeight')




