from flask import Blueprint, jsonify, render_template
from scripts.fetch_tweets import get_user_tweets
from models.sentiment_model import analyze_sentiment

api_bp = Blueprint('api', __name__)

@api_bp.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@api_bp.route('/api/analyze_tweets/<username>', methods=['GET'])
def analyze_tweets(username):
    try:
        tweets = get_user_tweets(username)
        if not tweets:
            return jsonify({"error": "No tweets found"}), 404
        
        results = []
        for tweet in tweets:
            sentiment = analyze_sentiment(tweet['text'])
            results.append({
                'tweet': tweet['text'],
                'sentiment': sentiment['label'],
                'score': sentiment['score']
            })
        
        return jsonify({
            'username': username,
            'results': results
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_bp.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200



# from flask import Blueprint, request, jsonify
# from models.sentiment_model import analyze_sentiment  # Assuming you have a function for sentiment analysis
# from scripts.fetch_tweets import get_tweets  # Function to fetch tweets

# api_blueprint = Blueprint('api', __name__)

# # Route to analyze text sentiment
# @api_blueprint.route('/analyze', methods=['POST'])
# def analyze_text():
#     try:
#         text = request.json.get('text', '')
#         if not text:
#             return jsonify({'error': 'No text provided'}), 400

#         # Run the sentiment analysis function
#         sentiment = analyze_sentiment(text)
#         return jsonify({'text': text, 'sentiment': sentiment})
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# # Route to fetch and analyze tweets
# @api_blueprint.route('/analyze_tweets/<username>', methods=['GET'])
# def analyze_user_tweets(username):
#     try:
#         # Fetch tweets from the Twitter API
#         tweets = get_tweets(username)
#         if tweets is None:
#             return jsonify({'error': 'Could not fetch tweets for user'}), 404

#         # Perform sentiment analysis on each tweet
#         analyzed_tweets = []
#         for tweet in tweets:
#             sentiment = analyze_sentiment(tweet['text'])
#             analyzed_tweets.append({'tweet': tweet['text'], 'sentiment': sentiment})

#         return jsonify(analyzed_tweets)
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500


# @api_blueprint.route('/analyze', methods=['POST'])
# def analyze_text():
#     try:
#         text = request.json.get('text', '')
#         result = analyze_sentiment(text)
#         return jsonify(result)
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500
