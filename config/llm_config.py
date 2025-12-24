import os
from dotenv import load_dotenv


load_dotenv()


HF_API_KEY = os.getenv("HF_API_KEY")
HF_MODEL = "meta-llama/Meta-Llama-3-8B-Instruct"
HF_ENDPOINT = f"https://api-inference.huggingface.co/models/{HF_MODEL}"


HEADERS = {
"Authorization": f"Bearer {HF_API_KEY}",
"Content-Type": "application/json"
}