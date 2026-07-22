from fastapi import  Depends , APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.services.dashboard_service import DashboardService
from app.schema.dashboardSchema import DashboardResponse


dashboardRouter = APIRouter()

@dashboardRouter.get(
    "/dashboard",
    response_model=DashboardResponse
)
async def dashboard(
    db: AsyncSession = Depends(get_db)
):
    return await db.run_sync(lambda s: DashboardService(s).get_dashboard())
