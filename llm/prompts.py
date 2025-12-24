PROFILE_PROMPT = """
You are an expert cloud architect.


Extract a STRICT JSON object with:
name, budget_inr_per_month, description, tech_stack, non_functional_requirements.


NO explanations. ONLY valid JSON.


Project Description:
{description}
"""


BILLING_PROMPT = """
Generate 12–20 realistic monthly cloud billing records as JSON array.


Rules:
- Cloud agnostic
- Budget aware
- Include compute, DB, storage, networking, monitoring
- STRICT JSON ONLY


Project Profile:
{profile}
"""


ANALYSIS_PROMPT = """
Analyze cloud costs and generate optimization recommendations.


Return STRICT JSON with:
analysis, recommendations, summary.


Rules:
- Multi-cloud (AWS, Azure, GCP, Open Source)
- Include risks, savings, effort
- STRICT JSON ONLY


Project Profile:
{profile}


Billing Data:
{billing}
"""