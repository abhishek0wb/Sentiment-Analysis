# from flask import Flask, request, jsonify, render_template
# from transformers import AutoTokenizer, AutoModelForSequenceClassification
# import torch
# import logging
# from scripts.fetch_tweets import get_tweets
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)
# logging.basicConfig(level=logging.INFO)
# CORS(app, resources={r"/*": {"origins": "https://2b44-2405-201-6830-9e-a8c5-8ca5-c296-1126.ngrok-free.app/auth/twitter/callback"}})

# model_name = "WooHoo86/tweets-text-generation-sentiment-analysis-uploaded0519"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForSequenceClassification.from_pretrained(model_name)

# def analyze_sentiment(text):
#     inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
#     outputs = model(**inputs)
#     logits = outputs.logits
#     sentiment = torch.argmax(logits, dim=-1).item()
#     sentiment_mapping = {0: "Negative", 1: "Neutral", 2: "Positive"}
#     return sentiment_mapping[sentiment]

# @app.route("/", methods=["GET", "POST"])
# def home():
#     if request.method == "POST":
#         text = request.form.get("text")
#         if not text:
#             return render_template("index.html", error="Please enter text for sentiment analysis.")
#         result = analyze_sentiment(text)
#         return render_template("index.html", sentiment=result, text=text)
#     return render_template("index.html")

# @app.route("/analyze", methods=["POST"])
# def analyze():
#     try:
#         data = request.get_json()
#         if "text" not in data:
#             logging.error("Text field missing in the request")
#             return jsonify({"error": "Text field is missing"}), 400
        
#         text = data["text"]
#         logging.info(f"Received text for analysis: {text}")
#         result = {"sentiment": analyze_sentiment(text)}
#         logging.info(f"Sentiment analysis result: {result['sentiment']}")
#         return jsonify(result)
    
#     except Exception as e:
#         logging.error(f"Error during sentiment analysis: {str(e)}")
#         return jsonify({"error": str(e)}), 500

# @app.route('/analyze_tweets/<username>', methods=['GET'])
# def analyze_user_tweets(username):
#     try:
#         tweets = get_tweets(username)
#         if not tweets:
#             return jsonify({"error": "No tweets found or unable to fetch tweets"}), 404
#         sentiment_results = [{"tweet": tweet, "sentiment": analyze_sentiment(tweet)} for tweet in tweets]
#         return jsonify(sentiment_results)
#     except Exception as e:
#         logging.error(f"Error during tweet analysis: {str(e)}")
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True)









# from flask import Flask, request, jsonify, render_template
# from transformers import AutoTokenizer, AutoModelForSequenceClassification
# import torch
# import logging
# from scripts.fetch_tweets import get_tweets
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)
# logging.basicConfig(level=logging.INFO)

# # Add your ngrok URL for CORS if necessary
# CORS(app, resources={r"/*": {"origins": "https://2b44-2405-201-6830-9e-a8c5-8ca5-c296-1126.ngrok-free.app"}})

# # Load the Hugging Face sentiment model
# model_name = "WooHoo86/tweets-text-generation-sentiment-analysis-uploaded0519"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForSequenceClassification.from_pretrained(model_name)

# # Sentiment analysis function
# def analyze_sentiment(text):
#     inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
#     outputs = model(**inputs)
#     logits = outputs.logits
#     sentiment = torch.argmax(logits, dim=-1).item()
#     sentiment_mapping = {0: "Negative", 1: "Neutral", 2: "Positive"}
#     return sentiment_mapping[sentiment]

# # Homepage with form for sentiment analysis
# @app.route("/", methods=["GET", "POST"])
# def home():
#     if request.method == "POST":
#         text = request.form.get("text")
#         if not text:
#             return render_template("index.html", error="Please enter text for sentiment analysis.")
#         result = analyze_sentiment(text)
#         return render_template("index.html", sentiment=result, text=text)
#     return render_template("index.html")

# # API for analyzing sentiment from a text input (JSON-based)
# @app.route("/analyze", methods=["POST"])
# def analyze():
#     try:
#         data = request.get_json()
#         if "text" not in data:
#             logging.error("Text field missing in the request")
#             return jsonify({"error": "Text field is missing"}), 400
        
#         text = data["text"]
#         logging.info(f"Received text for analysis: {text}")
#         result = {"sentiment": analyze_sentiment(text)}
#         logging.info(f"Sentiment analysis result: {result['sentiment']}")
#         return jsonify(result)
    
#     except Exception as e:
#         logging.error(f"Error during sentiment analysis: {str(e)}")
#         return jsonify({"error": str(e)}), 500

# # API for analyzing tweets from a specific username
# @app.route('/analyze_tweets/<username>', methods=['GET'])
# def analyze_user_tweets(username):
#     try:
#         tweets = get_tweets(username)
#         if not tweets:
#             return jsonify({"error": "No tweets found or unable to fetch tweets"}), 404
#         sentiment_results = [{"tweet": tweet, "sentiment": analyze_sentiment(tweet)} for tweet in tweets]
#         return jsonify(sentiment_results)
#     except Exception as e:
#         logging.error(f"Error during tweet analysis: {str(e)}")
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True)



from flask import Flask
from api.routes import api_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_bp)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
