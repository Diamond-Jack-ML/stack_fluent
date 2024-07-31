from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Replace with your Hugging Face model URL
HF_API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"
HF_API_TOKEN = "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"  # You can set this as an environment variable for better security

headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}


@app.route('/')
def home():
    return "Welcome to the Stack Fluent API. Use the /classify endpoint to classify text."

@app.route('/classify', methods=['POST'])
def classify_text():
    data = request.json
    text = data.get('text')
    candidate_labels = data.get('candidate_labels')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    if not candidate_labels:
        return jsonify({'error': 'No candidate labels provided'}), 400
    
    response = requests.post(HF_API_URL, headers=headers, json={"inputs": text, "parameters": {"candidate_labels": candidate_labels}})
    
    if response.status_code == 200:
        result = response.json()
        predicted_label = result["labels"][0]
        return jsonify({
            'text': text,
            'predicted_label': predicted_label
        })
    else:
        app.logger.error(f'Error in model inference: {response.text}')
        return jsonify({'error': 'Error in model inference'}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
