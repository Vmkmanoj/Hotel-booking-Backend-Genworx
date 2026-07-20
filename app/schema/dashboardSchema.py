from pydantic import BaseModel

class DashboardResponse(BaseModel):
    total_users: int
    total_customers: int
    total_property_owners: int
    total_admins: int

    total_properties: int
    pending_properties: int
    approved_properties: int
    rejected_properties: int