import os
from dotenv import load_dotenv

load_dotenv()  # 👈 THIS LINE

HF_API_TOKEN = os.getenv("HF_API_TOKEN")
HF_MODEL = "meta-llama/Meta-Llama-3-8B-Instruct"

if not HF_API_TOKEN:
    raise RuntimeError("HF_API_TOKEN not set in environment")
