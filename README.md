# PCA-Principal-Component-Analysis-
Principal Component Analysis (PCA) is by far the most popular dimensionality reduction algorithm. First it identifies the hyperplane that lies closest to the data, and then it projects the data onto it.

PCA is used to decompose a multivariate dataset in a set of successive orthogonal components that explain a maximum amount of the variance. In scikit-learn, PCA is implemented as a transformer object that learns n components in its fit method, and can be used on
new data to project it on these components.

If your learning algorithm is too slow because the input dimension is too high, then using PCA to speed it up can be a reasonable choice. This is probably the most common application of PCA. 

#Another common application of PCA is for data visualization.

'''
		 Iris dataset used in this part of the code is 4 dimensional. 
		 here used PCA to reduce that 4 dimensional data into 2 or 3 dimensions 
		 so that data can plot and hopefully understand the data better.

'''
https://en.wikipedia.org/wiki/Principal_component_analysis


http://scikit-learn.org/stable/modules/decomposition.html#pca
