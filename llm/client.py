import json
from huggingface_hub import InferenceClient
from config.llm_config import HF_API_TOKEN, HF_MODEL
from utils.retry import retry


class LLMClient:
    _client = InferenceClient(api_key=HF_API_TOKEN)

    @staticmethod
    def parse_json_safe(content: str):
        """
        Parse a complete JSON value.
        If JSON is truncated, raise a clear error.
        """
        content = content.strip()

        # Quick truncation detection
        if content.count("{") > content.count("}") or content.count("[") > content.count("]"):
            raise ValueError("Truncated JSON detected")

        decoder = json.JSONDecoder()
        obj, _ = decoder.raw_decode(content)
        return obj

    @staticmethod
    def call(prompt: str):
        def _call_once():
            messages = [
                {
                    "role": "system",
                    "content": (
                        "You MUST return ONLY valid JSON.\n"
                        "Do NOT explain.\n"
                        "Do NOT use markdown.\n"
                        "Return a SINGLE JSON array or object."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]

            response = LLMClient._client.chat.completions.create(
                model=HF_MODEL,
                messages=messages,
                temperature=0.1,
                max_tokens=2000,   # 🔑 increased
                top_p=0.9
            )

            content = response.choices[0].message.content
            return LLMClient.parse_json_safe(content)

        return retry(_call_once, attempts=3)
