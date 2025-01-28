from api.utils import settings
from datetime import datetime
import pytz
from api.v1.schemas import InfoResponse
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


info = APIRouter(prefix="/info", tags=["Info"])



@info.get("/", response_model=InfoResponse)
async def get_info():
    current_datetime = datetime.now(pytz.utc).isoformat()
    return JSONResponse(
        status_code=200,  
        content=jsonable_encoder({      
            "email": settings.EMAIL,
            "current_datetime": current_datetime,
            "github_url": settings.GITHUB_URL
        })
    )
