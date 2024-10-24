
import typing as t
import pandas as pd


class xlsOps(object):

   def __init__(self, fname: str):
      self.fname: str = fname
      self.pdxlf: pd.ExcelFile = t.Any

   def load(self) -> bool:
      self.pdxlf = pd.ExcelFile(self.fname)
      return self.pdxlf != t.Any

   def get_sheets(self, sheet_names: ()):
      pass
