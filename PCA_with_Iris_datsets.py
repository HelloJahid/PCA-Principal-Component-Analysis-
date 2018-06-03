'''
		 Iris dataset used in this part of the code is 4 dimensional. 
		 Here used PCA to reduce that 4 dimensional data into 2 dimensions 
		 and plot the data and hopefully understand the data better.

'''

# Import required module
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

#load iris data
iris = load_iris()

X = iris.data   # feature of iris datasets
y = iris.target  # target of iris datasets

# scale the data
X = StandardScaler().fit_transform(X)

# create instance of  PCA(principle components analysis)
pca = PCA(n_components = 2)

# reduce the dimension of the data --> 4D to 2D
pricipleComponents = pca.fit_transform(X)

# split the the data
x = pricipleComponents[:, [0]]
y = pricipleComponents[:, [1]]

# data for iris-setosa
x0 = x[:50]
y0 = y[:50]

# data for iris-versicolor
x1 = x[50:100]
y1 = y[50:100]

# data for iris-virginica
x2 = x[100:150]
y2 = y[100:150]

# visualize the reduction data
fig = plt.figure(figsize = (8, 8))
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('Principle Components 1', fontsize = 15)
ax.set_ylabel('Principle Components 2', fontsize = 15)
ax.set_title('2 Component PCA', fontsize = 20)
targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

ax.scatter(x0, y0, c='r')   #plot iris-setosa
ax.scatter(x1, y1, c='g')	#plot iris-versicolor
ax.scatter(x2, y2, c='b') 	# plot iris-virginica

ax.legend(targets)
ax.grid()
plt.show()
