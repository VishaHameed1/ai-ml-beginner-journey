import google.generativeai as genai
import os

# 1. Setup your API Key
# Replace the text below with your actual key from Google AI Studio
os.environ["GEMINI_API_KEY"] = "AIzaSyBp5tQPcujnd0zstyoIutcfzlrBiep2Fdg"
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# 2. Initialize the model
model = genai.GenerativeModel('gemini-2.5-flash')
chat = model.start_chat(history=[])

print("--- 🤖 Your Personal AI Chatbot (Type 'quit' to exit) ---")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'quit':
        print("AI: Goodbye! Have a great day.")
        break
        
    try:
        # 3. Generate response
        response = chat.send_message(user_input)
        print(f"AI: {response.text}")
        
    except Exception as e:
        print(f"❌ Error: {e}")