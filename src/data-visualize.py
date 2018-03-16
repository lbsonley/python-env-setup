import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

from data.flowers import getData

dataset = getData()

dataset.plot(kind='box', subplots=False, layout=(2, 2), sharex=False, sharey=False)
plt.show();

dataset.hist();
plt.show();

scatter_matrix(dataset);
plt.show();
