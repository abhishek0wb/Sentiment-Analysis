# from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer

# model_name = "WooHoo86/tweets-text-generation-sentiment-analysis-uploaded0519"
# model = AutoModelForSequenceClassification.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# sentiment_analysis = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

# def analyze_sentiment(text):
#     return sentiment_analysis(text)





from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer

# Load the pre-trained model and tokenizer from Hugging Face
model_name = "WooHoo86/tweets-text-generation-sentiment-analysis-uploaded0519"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Create a sentiment analysis pipeline
sentiment_analyzer = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

def analyze_sentiment(text):
    try:
        # Ensure text is valid
        if not text or not isinstance(text, str):
            raise ValueError("Invalid input text")
        
        # Perform sentiment analysis
        result = sentiment_analyzer(text)[0]
        
        return {
            'label': result['label'],
            'score': float(result['score'])
        }
    except Exception as e:
        raise Exception(f"Error analyzing sentiment: {str(e)}")

