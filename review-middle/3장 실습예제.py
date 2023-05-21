import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
b=pd.read_csv('population.csv')
print(b)
print(np.mean(b['population']))
