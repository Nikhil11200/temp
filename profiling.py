import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Load collected data
with open('backend/user_behavior.json') as file:
    user_behavior = json.load(file)

# Prepare data for clustering
conversation_data = [" ".join(v["keywords"]) for v in user_behavior.values()]

# Create DataFrame
df = pd.DataFrame({'text': conversation_data})

# Vectorize the conversation data
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['text'])

# Cluster users based on conversation patterns
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)

# Assign clusters to data
df['cluster'] = kmeans.labels_

# Print cluster results
print(df)
