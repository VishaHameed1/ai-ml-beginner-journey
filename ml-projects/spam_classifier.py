from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# 1. Sample Data
emails = ["Win free money now", "Meeting at 5pm", "Claim your prize", "Hello, how are you?"]
labels = [1, 0, 1, 0] # 1 = Spam, 0 = Not Spam

# 2. Convert text to numbers (Vectorization)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)

# 3. Train Model
model = LogisticRegression()
model.fit(X, labels)

# 4. Test a new email
test_email = ["Get free prizes now"]
test_vec = vectorizer.transform(test_email)
prediction = model.predict(test_vec)

print(f"Prediction for '{test_email[0]}': {'Spam' if prediction[0] == 1 else 'Not Spam'}")