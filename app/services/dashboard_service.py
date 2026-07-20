from app.repositories.DashboardRepository import DashboardRepository
from app.schema.dashboardSchema import DashboardResponse


class DashboardService:

    def __init__(self, db):
        self.repo = DashboardRepository(db)

    def get_dashboard(self):

        return DashboardResponse(
            total_users=self.repo.total_users(),
            total_customers=self.repo.total_customers(),
            total_property_owners=self.repo.total_property_owners(),
            total_admins=self.repo.total_admins(),

            total_properties=self.repo.total_properties(),
            pending_properties=self.repo.pending_properties(),
            approved_properties=self.repo.approved_properties(),
            rejected_properties=self.repo.rejected_properties(),
        )