from fastapi import  Depends , APIRouter
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.dashboard_service import DashboardService
from app.schema.dashboardSchema import DashboardResponse


dashboardRouter = APIRouter()

@dashboardRouter.get(
    "/dashboard",
    response_model=DashboardResponse
)
def dashboard(
    db: Session = Depends(get_db)
):
    service = DashboardService(db)
    return service.get_dashboard()