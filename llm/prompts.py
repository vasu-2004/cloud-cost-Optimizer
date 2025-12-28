
PROFILE_PROMPT = """
You are an expert cloud architect.

You MUST return ONE JSON OBJECT.
Do NOT return a list.
Do NOT return partial data.

The JSON object MUST contain ALL of the following fields:

{{
  "name": string,
  "budget_inr_per_month": number,
  "description": string,
  "tech_stack": object,
  "non_functional_requirements": array
}}

Rules:
- Return exactly ONE JSON object
- tech_stack MUST be a JSON object (key-value pairs)
- non_functional_requirements MUST be an array of strings
- budget_inr_per_month MUST be a number
- NO explanations
- NO markdown
- JSON ONLY

Project Description:
{description}
"""





BILLING_PROMPT = """
You are generating synthetic cloud billing data.

Rules:
- Output ONLY valid JSON (no text, no markdown)
- Output a JSON ARRAY
- Total records: between 12 and 20
- Cover 3 to 4 months
- Cloud-agnostic services (Compute, Database, Storage, Networking, Monitoring)
- Monthly total cost should stay close to the project budget
- Costs must be realistic for India (INR)
- Use realistic regions (e.g., ap-south-1, ap-southeast-1, eu-central-1)

Each record MUST contain:
- month (YYYY-MM)
- service
- resource_id
- region
- usage_type
- usage_quantity (number)
- unit
- cost_inr (number)
- desc

Project profile:
{profile}

Return ONLY the JSON array.

"""


ANALYSIS_PROMPT = """
You are a cloud cost optimization expert.

TASK:
Analyze the billing data and generate a cost optimization report.

OUTPUT FORMAT (STRICT JSON ONLY):
{{
  "project_name": string,
  "analysis": {{
    "total_monthly_cost": number,
    "budget": number,
    "budget_variance": number,
    "service_costs": object,
    "high_cost_services": object,
    "is_over_budget": boolean
  }},
  "recommendations": array,
  "summary": {{
    "total_potential_savings": number,
    "savings_percentage": number,
    "recommendations_count": number,
    "high_impact_recommendations": number
  }}
}}

RECOMMENDATIONS RULES:
- Generate 6–10 recommendations
- Each recommendation MUST include:
  - title
  - service
  - current_cost
  - potential_savings
  - recommendation_type
  - description
  - implementation_effort (low/medium/high)
  - risk_level (low/medium/high)
  - steps (array of strings)
  - cloud_providers (array)
- Recommendations must be multi-cloud:
  AWS, Azure, GCP, and open-source / free-tier options
- NO explanations
- NO markdown
- STRICT JSON ONLY

Project Profile:
{profile}

Billing Data:
{billing}
"""
