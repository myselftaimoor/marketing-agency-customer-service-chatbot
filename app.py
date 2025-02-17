from flask import Flask, request, jsonify
import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import string
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Initialize Flask app
app = Flask(__name__)

# Download necessary NLTK resources
nltk.download('punkt')

# Load FAQ data
faq_df = pd.read_csv('FAQ.csv')

# Preprocessing function
def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

# Preprocess the questions and answers
faq_df['Processed_Questions'] = faq_df['Question'].apply(preprocess_text)
faq_df['Processed_Answers'] = faq_df['Answer']

# Initialize the TF-IDF Vectorizer
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(faq_df['Processed_Questions'])

# Train the Nearest Neighbors model
knn_model = NearestNeighbors(n_neighbors=1, metric='cosine')
knn_model.fit(X)

# Function to get the answer
def get_answer(user_query):
    user_query_processed = preprocess_text(user_query)
    
    # First try fuzzy matching
    best_match = process.extractOne(
        user_query_processed,
        faq_df['Processed_Questions'].tolist(),
        scorer=fuzz.token_sort_ratio
    )
    
    if best_match[1] >= 80:  # If fuzzy match score is above 80%
        matched_index = faq_df[faq_df['Processed_Questions'] == best_match[0]].index[0]
        return faq_df.iloc[matched_index]['Processed_Answers']
    
    # If fuzzy matching doesn't find a good match, use TF-IDF and KNN
    user_query_vec = vectorizer.transform([user_query_processed])
    _, indices = knn_model.kneighbors(user_query_vec)
    
    answer = faq_df.iloc[indices[0][0]]['Processed_Answers']
    return answer

# API route to handle chatbot queries
@app.route('/chatbot', methods=['POST'])
def chatbot():
    try:
        if not request.is_json:
            return jsonify({"error": "Request must be JSON"}), 400
            
        data = request.get_json()
        if not isinstance(data, dict):
            return jsonify({"error": "Invalid JSON format"}), 400
            
        user_query = data.get("query", "")
        if not user_query:
            return jsonify({"error": "Query is required"}), 400
        
        answer = get_answer(user_query)
        return jsonify({"answer": answer})  # Excluding the query from the response
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)