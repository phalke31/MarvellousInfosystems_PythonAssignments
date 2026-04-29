# K Means - KMeans groups similar students, we label them after.

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

Border = "_"*70

print(Border)
print("Step1 : Load the dataset")
print(Border)

df = pd.read_csv("student-mat.csv", sep=';')

print(Border)
print("Step2 : Select required features")
print(Border)

features = df[['G1', 'G2', 'G3', 'studytime', 'failures', 'absences']]

print(Border)
print("Step3 : Scale the data")
print(Border)

Scaler = StandardScaler()
Scaled_features = Scaler.fit_transform(features)

print(Border)
print("Step4 : Apply K-Means (3 clusters)")
print(Border)

kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(Scaled_features)

print(Border)
print("Step5 : Analyze cluster averages")
print(Border)

print("\n Random Cluster Summary:\n")
print(df.groupby('cluster')[features.columns].mean())

# Map clusters to required format

""" Top Performers (Cluster 0)
Average Students (Cluster 1)
Struggling Students (Cluster 2) """


cluster_mapping = {
    2: 0,  # Top Performer
    0: 1,  # Average Student
    1: 2   # Struggling Student
}

df['cluster'] = df['cluster'].map(cluster_mapping)

print("\nCluster Summary AFTER mapping:\n")
print(df.groupby('cluster')[features.columns].mean())