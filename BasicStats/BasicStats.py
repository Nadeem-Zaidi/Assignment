from collections import defaultdict

import numpy as np
from pandas import Series, DataFrame
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

    def mean_and_std_of_each_columns(self ,data :DataFrame)->dict[str:any]:
        '''this will return the mean and the standard deviation for all the series in the data frame in dict form
        :type data: object
        '''
        md = defaultdict()
        mean_dict = defaultdict()
        std_dict = defaultdict()
        for c in data.columns:
            if utility.ValidSeries(data[c]):
                mean = self.mean(data[c])
                std = self.standard_deviation(data[c])
                utility.dictionary(c, mean, mean_dict)
                utility.dictionary(c, std, std_dict)

        utility.dictionary("mean", mean_dict, md)
        utility.dictionary("standard_deviation", std_dict, md)
        return md

    def percentile_of_each_column(self,data:DataFrame)->dict:
        percentile=defaultdict()
        q1=defaultdict()
        q2=defaultdict()
        q3=defaultdict()
        for c in data:
            if utility.ValidSeries(data[c]):
                series=data[c]
                percentile_q1=self.percentile(series,25)
                percentile_q2=self.percentile(series,50)
                percentile_q3=self.percentile(series,75)
                utility.dictionary(c,percentile_q1,q1)
                utility.dictionary(c, percentile_q2, q2)
                utility.dictionary(c, percentile_q3, q3)
        utility.dictionary("percentile_q1",q1,percentile)
        utility.dictionary("percentile_q2", q2, percentile)
        utility.dictionary("percentile_q3", q3, percentile)
        return percentile

    def IQR_for_each_column(self,data:DataFrame):
        iqr_dict = defaultdict()
        final_iqr_dict=defaultdict()
        for c in data.columns:
            if utility.ValidSeries(data[c]):
                series = data[c]
                iqr = self.IQR(series)
                utility.dictionary(c, iqr, iqr_dict)
        utility.dictionary("IQR",iqr_dict,final_iqr_dict)
        return(final_iqr_dict)
