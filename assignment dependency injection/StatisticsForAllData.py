from abc import ABC,abstractmethod


class StatisticsForAllData(ABC):

    @abstractmethod
    def mean_and_std_of_each_columns(self):
        ''' calculate the mean  for all columns in a dataframe'''
    @abstractmethod
    def percentile_of_each_column(self):
        '''calculate percentile for all the columns in a data frame'''
    @abstractmethod
    def IQR_for_each_column(self):
        '''calculate IQR for all columns in a data frame'''