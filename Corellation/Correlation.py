from abc import ABC,abstractmethod

from pandas import Series, DataFrame


class Correlation(ABC):

    @abstractmethod
    def correlation(self,col_1:str,col_2:str,df:DataFrame)->dict[str:str]:
      '''this functions return the corrrelation between two data series'''

    @abstractmethod
    def correlationAll(self,colname:str,df:DataFrame)->dict[str:str]:
        '''this functions return the correlations for one series vs all'''
