
from services.ai_service import AIService
import dotenv
import os


def main():
    dotenv.load_dotenv()

    gemini_key = os.getenv("GEMINI_API_KEY")
    if not gemini_key:
        raise Exception("Not able to load gemini key")

    ai = AIService(
        gemini_key=gemini_key,
        model="gemini-2.5-flash"
    )

    res = ai.generate_response("Tell me a joke")

    print(f"Print Result: \n{res}")

if __name__ == "__main__":
    main()
