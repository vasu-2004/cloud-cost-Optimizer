from llm.client import LLMClient
from llm.prompts import BILLING_PROMPT
from utils.file_io import save_json


class BillingGenerator:
    def run(self, profile):
        prompt = BILLING_PROMPT.format(profile=profile)
        data = LLMClient.call(prompt)
        save_json("data/mock_billing.json", data)
        return data