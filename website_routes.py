from fastapi import APIRouter,Depends
from app.schemas import WebsiteURL
from app.scraper import scrapping
from app.auth import get_current_user
from app.models import Users,Websites
from app.database import session,get_db
from sqlalchemy.orm import Session


router = APIRouter()



@router.post("/addurl")
def addurl(data:WebsiteURL,current_user: Users = Depends(get_current_user), db:Session=Depends(get_db)):

    new_web=Websites(
        user_id=current_user.id,
        url=str(data.url),
        status=scrap["status"]
    )

    scrap=scrapping(data.url,new_web.id)


    db.add(new_web)
    db.commit()
    db.refresh(new_web)

    return {f"scrapp : {scrap} user_id : {current_user.id} : url : {data.url} status : {scrap["status"]}"}
