import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
datsets=load_breast_cancer()
sns.set_style('dark')
import matplotlib as mlp
mlp.style.use(['https://gist.githubusercontent.com/BrendanMartin/01e71bb9550774e2ccff3af7574c0020/raw/6fa9681c7d0232d34c9271de9be150e584e606fe/lds_default.mplstyle'])
mlp.rcParams.update({"figure.figsize":(8,6), "axes.titlepad":22.0})
print('Target variables :',datsets['target_names'])
(unique,counts)=np.unique(datsets['target'],return_counts=True)
print('unique values of target available',unique)
print('counts:',counts)
sns.barplot(x=datsets['target_names'],y= counts)
plt.title('Target variable count in dataset')
plt.show()