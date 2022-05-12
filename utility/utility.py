from collections import defaultdict

from pandas import Series


def ValidSeries(series: Series) -> bool:
    if series.dtype in ['int64', 'float64']:
        return True
    else:
        return False


def message(method: str) -> str:
    return f"data type of the series is not int64 or float64 .Hence can not calculate {method}"

def dictionary(key,value,d:defaultdict):
    d[key]=value
