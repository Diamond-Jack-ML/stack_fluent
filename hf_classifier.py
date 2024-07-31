from transformers import pipeline, set_seed
import pandas as pd

# Mock data
data = [
    {"text": "I need information about the new product line.", "category": "Inquiry", "subcategory": "Product Information"},
    {"text": "How much does this product cost?", "category": "Inquiry", "subcategory": "Pricing"},
    {"text": "When will the product be available?", "category": "Inquiry", "subcategory": "Availability"},
    {"text": "The product I received is defective.", "category": "Complaint", "subcategory": "Product Issue"},
    {"text": "I'm unhappy with the customer service.", "category": "Complaint", "subcategory": "Service Issue"},
    {"text": "I was overcharged on my bill.", "category": "Complaint", "subcategory": "Billing Issue"},
    {"text": "Great job on the latest update!", "category": "Feedback", "subcategory": "Positive"},
    {"text": "I'm not satisfied with the new features.", "category": "Feedback", "subcategory": "Negative"},
    {"text": "The update is okay, but it could be better.", "category": "Feedback", "subcategory": "Neutral"}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Simple classification pipeline using a pre-trained model (e.g., GPT-3)
classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')

# Define labels
labels = ["Inquiry:Product Information", "Inquiry:Pricing", "Inquiry:Availability",
          "Complaint:Product Issue", "Complaint:Service Issue", "Complaint:Billing Issue",
          "Feedback:Positive", "Feedback:Negative", "Feedback:Neutral"]

# Classify text
for index, row in df.iterrows():
    result = classifier(row['text'], labels)
    df.at[index, 'predicted_category'] = result['labels'][0].split(":")[0]
    df.at[index, 'predicted_subcategory'] = result['labels'][0].split(":")[1]

print(df)
