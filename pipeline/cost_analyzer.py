from llm.client import LLMClient
from llm.prompts import ANALYSIS_PROMPT
from utils.file_io import save_json


class CostAnalyzer:
    def run(self, profile, billing):
        prompt = ANALYSIS_PROMPT.format(profile=profile, billing=billing)
        data = LLMClient.call(prompt)
        save_json("data/cost_optimization_report.json", data)
        return data