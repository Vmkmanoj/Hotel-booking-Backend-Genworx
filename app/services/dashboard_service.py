from app.repositories.DashboardRepository import DashboardRepository
from app.schema.dashboardSchema import DashboardResponse


class DashboardService:

    def __init__(self, db):
        self.repo = DashboardRepository(db)

    async def get_dashboard(self):

        return  DashboardResponse(
            total_users=await self.repo.total_users(),
            total_customers=await self.repo.total_customers(),
            total_property_owners=await self.repo.total_property_owners(),
            total_admins=await self.repo.total_admins(),
            suspend_properties= await self.repo.suspend_properties(),
            total_properties=await self.repo.total_properties(),
            pending_properties=await self.repo.pending_properties(),
            approved_properties=await self.repo.approved_properties(),
            rejected_properties=await self.repo.rejected_properties(),
        )
