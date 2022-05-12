import numpy as np
from pandas import Series
from BasicStats import StatisticMethods
from scipy import stats
from utility import utility


class BasicStatistics(StatisticMethods.StatisticsMethods):

    def mean(self, series_data: Series) -> float | str:
        if series_data.dtype in ['int64', 'float64']:
            m = np.mean(series_data)
            return m
        else:
            return utility.message("mean")

    def percentile(self, series_data: Series, qvalue: int) -> float | str:
        '''return the percentile  value like q1, q2/median,q3'''
        if utility.ValidSeries(series_data) is True:
            p = np.percentile(series_data, qvalue)
            return p
        else:
            return utility.message("percentile")

    def standard_deviation(self, series_data: Series) -> float | str:
        '''return standard deviation of the series passed'''
        if utility.ValidSeries(series_data) is True:
            std = np.std(series_data)
            return std
        else:
            return utility.message()

    def IQR(self, series_data: Series) -> float | str:
        '''return the iqr value for the series passed'''
        if utility.ValidSeries(series_data) is True:
            iqr = stats.iqr(series_data)
            return iqr
        else:
            return utility.message("IQR")

    def outliers_using_iqr(self, series_data: Series) -> list[float] | str:
        '''return the outliers for the series passed in list'''

        o = []
        if utility.ValidSeries(series_data) is True:
            iqr = self.IQR(series_data)
            q1 = self.percentile(series_data, 25)
            q3 = self.percentile(series_data, 75)
            lower_limit = q1 - (1.5 * iqr)
            upper_limit = q3 + (1.5 * iqr)
            print("upper limit")
            for i in series_data.tolist():
                if (i < lower_limit) or (i > upper_limit):
                    o.append(i)
            return o
        else:
            return utility.message("outlier")

    def outlier_using_zscore(self, series_data: Series) -> list[float] | str:
        '''return the outlier using the z core in list'''

        threshold = 3
        outlier = []
        if utility.ValidSeries(series_data):
            mean = self.mean(series_data)
            std = self.standard_deviation(series_data)
            for i in series_data.tolist():
                z = (i - mean) / std
                if z > threshold:
                    outlier.append(i)
                if z < -threshold:
                    outlier.append(i)

            return outlier
        else:
            return utility.message("outlier")
