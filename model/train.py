import pandas as pd
import pickle
from sentence_transformers import SentenceTransformer
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("data/labeled_data.csv")

embedder = SentenceTransformer('all-MiniLM-L6-v2')

print("🔄 Generating embeddings...")
X = embedder.encode(df["One Line Pitch"].tolist())

y = df[["feasibility", "innovation", "market", "risk"]]

model = RandomForestRegressor(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

model.fit(X, y)

pickle.dump(model, open("model/model.pkl", "wb"))

print("✅ Model trained with meaningful patterns")