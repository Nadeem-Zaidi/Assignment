from collections import defaultdict

import StatisticsForAllData
class StatisticsForDataFrame(StatisticsForAllData.StatisticsForAllData):

    def mean_and_std_of_each_columns(self):
        ''' calculate the mean  for all columns in a dataframe'''
        md = defaultdict()
        mean_dict = defaultdict()
        std_dict = defaultdict()
        data = self.read_csv_data()
        for c in data.columns:
            if data[c].dtype in ['int64', 'float64']:
                mean = self.mean(c)
                std = self.standard_deviation(c)
                mean_dict[c] = mean
                std_dict[c] = std
                md["mean"] = mean_dict
                md["standard_deviations"] = std_dict
        return md


    def percentile_of_each_column(self):
        '''calculate percentile for all the columns in a data frame'''


    def IQR_for_each_column(self):
        '''calculate IQR for all columns in a data frame'''