import openai
import os

class GPTEnhancer:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        openai.api_key = self.api_key

    def suggest_alt_text(self, image_context):
        prompt = f"Suggest a descriptive alt text for this image context: {image_context}"
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message['content'].strip()
        except Exception as e:
            print(f"OpenAI error: {e}")
            return None

if __name__ == "__main__":
    enhancer = GPTEnhancer()
    print(enhancer.suggest_alt_text("A government building with the Indian flag.")) 