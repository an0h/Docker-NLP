from flask import Flask, request, jsonify
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
nltk.download('vader_lexicon')
nltk.download('punkt')

def perform_semantic_analysis(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_score = sid.polarity_scores(text)

    if sentiment_score['compound'] >= 0.05:
        return "Positive"
    elif sentiment_score['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
    return jsonify({"status": "ok"})

@app.route('/', methods=['POST'])
def post():
    content = request.json.get('content', None)
    if content is None:
        return jsonify({"error": "No content provided"}), 400

    result = perform_semantic_analysis(content)
    return jsonify({"Sentiment": result})


if __name__ == "__main__":
    app.run(debug=True)

