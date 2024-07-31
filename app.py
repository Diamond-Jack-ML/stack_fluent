from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your Hugging Face model URL
HF_API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"
HF_API_TOKEN = "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"  # You can set this as an environment variable for better security

headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}

@app.route('/classify', methods=['POST'])
def classify_text():
    data = request.json
    text = data.get('text')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    response = requests.post(HF_API_URL, headers=headers, json={"inputs": text})
    
    if response.status_code == 200:
        result = response.json()
        predicted_label = result[0]["label"]
        return jsonify({
            'text': text,
            'predicted_label': predicted_label
        })
    else:
        return jsonify({'error': 'Error in model inference'}), 500

if __name__ == '__main__':
    app.run(debug=True)
