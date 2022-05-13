from pandas import DataFrame
from utility import utility
from plot import Plot
import matplotlib.pyplot as plt


class DataPlot(Plot.Plot):
    def scatterplot(self, c1: str, c2: str,df:DataFrame,s:str):
        series1=df[c1]
        series2=df[c2]
        if utility.ValidSeries(series1) and utility.ValidSeries(series2):
            plt.style.use(s)
            plt.xlabel(series1.name)
            plt.ylabel(series2.name)
            plt.title(f"Plot of {series1.name} vs {series2.name}")
            plt.scatter(series1,series2)
            plt.show()

    def BoxPlot(self,col:str,data:DataFrame):
        '''this function will help in calculating the box plot'''
        series=data[col]
        if utility.ValidSeries(series):
            plt.title(f"Box plot for {col}")
            plt.boxplot(series)
            plt.show()
