from google import genai
from google.genai import types

class AIService:
    def __init__(self, gemini_key: str, model: str):
        self.gemini_key = gemini_key
        self.model_name = model

        self.client = genai.Client(api_key=gemini_key)

    def define_tools(self):
        grounding_tool = types.Tool(
            google_search = types.GoogleSearch()
        )

        config = types.GenerateContentConfig(
            tools=[grounding_tool]
        )

        return config

    def generate_response(self, prompt: str) -> str:

        tool_config = self.define_tools()

        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt,
                config=tool_config
            )

            if not response or not response.text:
                raise Exception("Response not recevied from Gemini")

            return response.text
        except Exception as e:
            print(f"error generating response: {e}")
            raise
