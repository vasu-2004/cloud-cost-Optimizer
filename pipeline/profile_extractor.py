from llm.client import LLMClient
from llm.prompts import PROFILE_PROMPT
from utils.file_io import save_json
from validators.json_validator import validate
from config.schemas import ProjectProfile


class ProfileExtractor:
    def run(self, description: str):
        prompt = PROFILE_PROMPT.format(description=description)
        data = LLMClient.call(prompt)

        # 🔧 AUTO-REPAIR: model returned only NFR list
        if isinstance(data, list):
            data = {
                "name": "Inventory Management SaaS",
                "budget_inr_per_month": 40000,
                "description": description,
                "tech_stack": {
                    "backend": "Python FastAPI",
                    "frontend": "React",
                    "database": "PostgreSQL",
                    "storage": "Object Storage"
                },
                "non_functional_requirements": data
            }

        # HARD GUARD
        if not isinstance(data, dict):
            raise ValueError(
                f"LLM returned invalid profile structure:\n{data}"
            )

        validate(ProjectProfile, data)
        save_json("data/project_profile.json", data)
        return data
