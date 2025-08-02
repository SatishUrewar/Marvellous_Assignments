import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    df=pd.read_csv("student-mat.csv",sep=";")
    
    features = ['G1', 'G2', 'G3', 'studytime', 'failures', 'absences']
    x=df[features].copy()

    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)

    wcss = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=42)
        kmeans.fit(x_scaled)
        wcss.append(kmeans.inertia_)

    plt.figure(figsize=(10, 5))
    plt.plot(range(1, 11), wcss, marker='o', linestyle='--')
    plt.title('Elbow Method for Optimal k')
    plt.xlabel('Number of Clusters k')
    plt.ylabel('WCSS')
    plt.show()

    model = KMeans(n_clusters=3, init='k-means++',n_init=10, random_state=42)
    clusters = model.fit_predict(x)

    df['cluster'] = clusters

    cluster_analysis = df.groupby('cluster')[features].mean()
    print("--- Cluster Analysis (Average values per cluster) ---")
    print(cluster_analysis)

    cluster_map = {
        0: 'Top Performers',      
        1: 'Struggling Students',  
        2: 'Average Students'     
    }
    df['performance_group'] = df['cluster'].map(cluster_map)

    print(df[['G1', 'G2', 'G3', 'failures', 'studytime', 'performance_group']].head(10))

    df['performance_group'] = df['cluster'].map(cluster_map)
    plt.figure(figsize=(12, 8))
    sns.scatterplot(data=df, x='G3', y='failures', style='performance_group', 
                    hue='performance_group', s=120, alpha=0.8)
    plt.title('Student Performance Clusters')
    plt.xlabel('Final Grade (G3)')
    plt.ylabel('Number of Past Failures')
    plt.legend(title='Performance Group')
    plt.show()


if __name__=="__main__":
    main()