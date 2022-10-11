from urllib import request

import fastapi
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

templates = Jinja2Templates("templates")

router = fastapi.APIRouter()


@router.get('/', include_in_schema=False)
def index(request: Request):
    return templates.TemplateResponse("index.j2", {"request": request, "name": "PyCharm"})
