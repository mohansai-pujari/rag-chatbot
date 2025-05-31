import google.generativeai as genai


class LLMModel:
    def __init__(self, gemini_api_key: str, model_name: str, temperature: float = 0):
        genai.configure(api_key=gemini_api_key)
        self.model = genai.GenerativeModel(model_name)
        self.temperature = temperature

    def get_response(self, prompt: str) -> str:
        # for model in genai.list_models():
        #     print(model.name, model.supported_generation_methods)
        response = self.model.generate_content(prompt)
        return response.text
