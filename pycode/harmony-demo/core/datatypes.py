
import pandas as pd
import typing as t


class xlsSheedDataFrame(object):

   def __init__(self, df: pd.DataFrame, name: str):
      self.df: pd.DataFrame = df
      self.sheet_name: str = name
