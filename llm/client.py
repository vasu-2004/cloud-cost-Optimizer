import requests
import json
from config.llm_config import HEADERS, HF_ENDPOINT


class LLMClient:
    @staticmethod
    def call(prompt: str) -> dict:
        payload = {
            "inputs": prompt,
            "parameters": {
                "temperature": 0.2,
                "max_new_tokens": 1200
            }
        }


        response = requests.post(HF_ENDPOINT, headers=HEADERS, json=payload)
        response.raise_for_status()


        text = response.json()[0]["generated_text"]
        start = text.find("{")
        end = text.rfind("}") + 1


        return json.loads(text[start:end])