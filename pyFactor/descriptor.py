# -*- coding: utf-8 -*-
"""
Created on 2017-05-31 00:31:00

@author: XavierXIEXIN
"""

import numpy as np
import pandas as pd

class Descriptor(object):
    """
    Descriptor of data with form of Series or Dataframe.
    Data must be preprocessed to fixed interval like day/week/month ...
    
    e.g.
    
            | 000001 | 000002 | 000007 | ...
    ---------------------------------------
    20170101| 12.95  | 11.30  | 10.20  | ...
    20170201| 11.05  | 07.30  | 10.10  | ...    
    20170301| 12.11  | 09.30  | 10.00  | ...
    ...
    
    
    """
    def __init__(self, data):
        self.data = data
        
    def momentum(self, period=12, lag=1):
        """
        Momentum descriptor, calculation period default 12, lag 1.
        """
        data = self.data.fillna(method='ffill')
        ret = data / data.shift(period) - 1
        mom = ret.shif(lag)
        return mom
        