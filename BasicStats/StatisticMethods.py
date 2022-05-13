from abc import ABC,abstractmethod
from pandas import Series, DataFrame


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

    @abstractmethod
    def mean_and_std_of_each_columns(self, data: DataFrame):
        '''this will return the mean and the standard deviation for all the series in the data frame in dict form'''

    @abstractmethod
    def percentile_of_each_column(self):
        '''this will return the percetile_25,percentile_50,percentile_75 for each series in dataframe'''

    @abstractmethod
    def IQR_for_each_column(self):
        '''this will return the IQR value for the each series in dataframe'''





