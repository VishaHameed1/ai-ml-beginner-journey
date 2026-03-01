from google import genai
from PIL import Image
import os

# 1. Setup your API Key
API_KEY = "."
client = genai.Client(api_key=API_KEY)

def analyze_image(image_path, user_prompt):
    try:
        # 2. Open the image file
        img = Image.open(image_path)
        
        print("🤖 AI is analyzing the visual details...")
        # 3. Use the powerful 2.5 Flash model
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[user_prompt, img]
        )
        
        print(f"\nAI Insight:\n{response.text}")
        
    except FileNotFoundError:
        print("❌ Error: I can't find that image file. Make sure it's in the 'projects' folder!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    # Ensure you have a 'test.jpg' in your projects folder!
    path = input("Enter image path (e.g., projects/test.jpg): ")
    prompt = input("Ask me anything about this photo: ")
    
    analyze_image(path, prompt)