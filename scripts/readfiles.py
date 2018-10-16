import pandas as pd
import numpy as np
from sklearn import preprocessing

class ReadFiles(object):

    def __init__(self):
      df = pd.read_csv('data/wdbc.data.csv', header=None, sep=",")
       
      self.labels = df[df.columns[1]]
      self.data = df[df.columns[2:len(df.columns)]].values

    def getData(self):
      return self.data


    def getLabels(self):
      encoder = preprocessing.LabelEncoder()
      encoder.fit(self.labels)
      self.labels = encoder.transform(self.labels)
      
      return self.labels