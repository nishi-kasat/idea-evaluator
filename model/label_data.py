import pandas as pd

df = pd.read_csv("data/startups.csv")

def generate_labels(pitch):
    pitch = str(pitch).lower()

    # Base scores
    feasibility = 5
    innovation = 5
    market = 5
    risk = 5

    # 🔹 Innovation rules
    if any(word in pitch for word in ["ai", "machine learning", "blockchain", "automation"]):
        innovation += 2
    if "platform" in pitch or "smart" in pitch:
        innovation += 1

    # 🔹 Market rules
    if any(word in pitch for word in ["students", "business", "travel", "health", "finance"]):
        market += 2

    # 🔹 Feasibility rules
    if any(word in pitch for word in ["app", "platform", "solution"]):
        feasibility += 2
    if "real-time" in pitch:
        feasibility -= 1

    # 🔹 Risk rules
    if "fintech" in pitch or "finance" in pitch:
        risk += 2
    if "health" in pitch:
        risk += 1

    # Clamp values (0–10)
    feasibility = min(max(feasibility, 0), 10)
    innovation = min(max(innovation, 0), 10)
    market = min(max(market, 0), 10)
    risk = min(max(risk, 0), 10)

    return {
        "feasibility": feasibility,
        "innovation": innovation,
        "market": market,
        "risk": risk
    }

labels = df["pitch"].apply(generate_labels)
labels_df = pd.DataFrame(labels.tolist())

df_final = pd.concat([df, labels_df], axis=1)
df_final.to_csv("data/labeled_data.csv", index=False)

print("✅ Smart labels generated")