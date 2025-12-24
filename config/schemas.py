from pydantic import BaseModel
from typing import List, Dict


class ProjectProfile(BaseModel):
    name: str
    budget_inr_per_month: int
    description: str
    tech_stack: Dict[str, str]
    non_functional_requirements: List[str]


class BillingRecord(BaseModel):
    month: str
    service: str
    resource_id: str
    region: str
    usage_type: str
    usage_quantity: float
    unit: str
    cost_inr: float
    desc: str


class Recommendation(BaseModel):
    title: str
    service: str
    current_cost: float
    potential_savings: float
    recommendation_type: str
    description: str
    implementation_effort: str
    risk_level: str
    steps: List[str]
    cloud_providers: List[str]