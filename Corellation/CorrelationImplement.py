from collections import defaultdict

from pandas import DataFrame
from Corellation import Correlation
from utility import utility


class CorrelationImplement(Correlation.Correlation):


    def correlation(self, col_1: str, col_2:str, df: DataFrame):
        '''this functions return the corrrelation between two data series'''
        d=defaultdict()
        series1=df[col_1]
        series2=df[col_2]
        if utility.ValidSeries(series1) and utility.ValidSeries(series2):

            utility.dictionary(f"correlation ({col_1} vs {col_2})",series1.corr(series2),d)
        return d


    def correlationAll(self, colname: str, df: DataFrame):
        '''this functions return the correlations for one series vs all'''

        s = defaultdict()

        for i in df.columns:
            if utility.ValidSeries(df[i]):
                utility.dictionary(f" correlation ({i} vs {colname})",df[i].corr(df[colname]),s)
        return s