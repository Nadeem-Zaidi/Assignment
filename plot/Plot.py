from abc import ABC,abstractmethod
from pandas import Series, DataFrame


class Plot(ABC):
    @abstractmethod
    def scatterplot(self,c1:str,c2:str,df:DataFrame,s:str):
        '''this function will help in ploting the series '''

    @abstractmethod
    def BoxPlot(self,col:str):
        '''this function will help in calculating the box plot'''

