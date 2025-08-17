from google import genai

class AIService:
    def __init__(self, gemini_key: str, model: str):
        self.gemini_key = gemini_key
        self.model_name = model

        self.client = genai.Client(api_key=gemini_key)

    def generate_response(self, prompt: str) -> str:
        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt
            )

            if not response or not response.text:
                raise Exception("Response not recevied from Gemini")

            return response.text
        except Exception as e:
            print(f"error generating response: {e}")
            raise
