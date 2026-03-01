from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

# 1. Data: [Annual Income, Spending Score]
data = np.array([
    [15, 39], [15, 81], [16, 6], [16, 77], [17, 40],
    [80, 90], [85, 85], [88, 92], [20, 10], [25, 15]
])

# 2. Create 3 Clusters (Groups)
kmeans = KMeans(n_clusters=3, n_init=10)
kmeans.fit(data)

# 3. Visualize the Groups
plt.scatter(data[:, 0], data[:, 1], c=kmeans.labels_, cmap='rainbow')
plt.title('Customer Groups (K-Means Clustering)')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.show()