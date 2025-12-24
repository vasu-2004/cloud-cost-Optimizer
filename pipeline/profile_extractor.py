from llm.client import LLMClient
from llm.prompts import PROFILE_PROMPT
from utils.file_io import save_json
from validators.json_validator import validate
from config.schemas import ProjectProfile


class ProfileExtractor:
    def run(self, description: str):
        prompt = PROFILE_PROMPT.format(description=description)
        data = LLMClient.call(prompt)
        validate(ProjectProfile, data)
        save_json("data/project_profile.json", data)
        return data