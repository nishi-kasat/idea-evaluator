from flask import Flask, request, jsonify, render_template
import pickle
from sentence_transformers import SentenceTransformer
from llm import generate_feedback

app = Flask(__name__)

model = pickle.load(open("model/model.pkl", "rb"))
embedder = SentenceTransformer('all-MiniLM-L6-v2')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/evaluate", methods=["POST"])
def evaluate():
    try:
        data = request.get_json(force=True)
        idea = data.get("idea", "")

        if not idea:
            return jsonify({"error": "No idea provided"}), 400

        embedding = embedder.encode([idea])
        scores = model.predict(embedding)[0]

        result = {
            "feasibility": float(scores[0]),
            "innovation": float(scores[1]),
            "market": float(scores[2]),
            "risk": float(scores[3]),
            "feedback": generate_feedback(idea, scores)
        }

        return jsonify(result)

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)