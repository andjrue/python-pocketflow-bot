
from services.ai_service import AIService
import dotenv
import os
from utils.prompt import prompt


def main():
    dotenv.load_dotenv()

    gemini_key = os.getenv("GEMINI_API_KEY")
    if not gemini_key:
        raise Exception("Not able to load gemini key")

    ai = AIService(
        gemini_key=gemini_key,
        model="gemini-2.5-flash"
    )

    system_prompt = prompt
    user_prompt = "Who is the current leader in batting average in major league baseball?"

    final_prompt = system_prompt + "\n\n\n\nUser Prompt:\n" + user_prompt

    res = ai.generate_response(final_prompt)

    print(f"Print Result: \n{res}")

if __name__ == "__main__":
    main()
