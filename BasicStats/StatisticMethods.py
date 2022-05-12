from abc import ABC,abstractmethod
from pandas import Series


class StatisticsMethods(ABC):

    @abstractmethod
    def mean(self,series_data:Series)->float|str:
        '''return mean value for the series passed'''

    @abstractmethod
    def percentile(self,series_data:Series,qvalue:int)->float|str:
        '''return the percentile  value like q1, q2/median,q3'''

    @abstractmethod
    def standard_deviation(self,series_data:Series)-> float|str:
        '''return standard deviation of the series passed'''

    @abstractmethod
    def IQR(self,series_data:Series)->float|str:
        '''return the iqr value for the series passed'''

    @abstractmethod
    def outliers_using_iqr(self,series_data:Series)->list[float]|str:
        '''return the outliers for the series passed in list'''

    @abstractmethod
    def outlier_using_zscore(self,series_data:Series)->list[float]|str:
        '''return the outlier using the z core in list'''




